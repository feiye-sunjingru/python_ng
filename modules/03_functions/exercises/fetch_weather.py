import textwrap
from datetime import datetime
from xml.etree import ElementTree as ET

import requests


def fetch_weather(city):
    """获取天气数据"""
    url = f"http://ws.webxml.com.cn/WebServices/WeatherWebService.asmx/getWeatherbyCityName?theCityName={city}"
    res = requests.get(url=url)
    root = ET.XML(res.text)
    return [node.text for node in root]


def parse_time(time_str):
    """解析时间，支持多种格式"""
    formats = [
        "%Y-%m-%d %H:%M:%S",
        "%Y/%m/%d %H:%M:%S",
        "%Y-%m-%d",
    ]
    for fmt in formats:
        try:
            return datetime.strptime(time_str, fmt)
        except ValueError:
            continue
    return None


def parse_weather_info(info_text):
    """解析天气实况信息"""
    if not info_text or "今日天气实况" not in info_text:
        return None

    # 移除前缀
    info_text = info_text.replace("今日天气实况：", "")

    # 按分号分割
    parts = info_text.split("；")

    result = {}
    for part in parts:
        if "：" in part or ":" in part:
            # 分离键和值
            key, value = part.replace("：", ":").split(":", 1)
            result[key.strip()] = value.strip()

    return result


def format_weather(data_list):
    """格式化天气数据输出"""
    if not data_list or len(data_list) < 22:
        print("数据格式异常")
        return

    # 提取关键信息
    province = data_list[0]
    city = data_list[1]
    update_time = parse_time(data_list[4])
    current_temp = data_list[5]
    today_weather = data_list[6]
    today_wind = data_list[7]
    today_info = data_list[10]
    life_index = data_list[11]

    # 明天预报
    tomorrow_temp = data_list[12]
    tomorrow_weather = data_list[13]
    tomorrow_wind = data_list[14]

    # 后天预报
    day3_temp = data_list[17]
    day3_weather = data_list[18]
    day3_wind = data_list[19]

    # 其他城市信息
    city_info = data_list[22]

    # 美化输出
    print("=" * 60)
    print(f"🌤️  {province}·{city} 天气预报")
    print("=" * 60)

    print(f"\n🕐 更新时间：{update_time.strftime('%Y-%m-%d %H:%M')}")
    print(f"📍 当前温度：{current_temp}")
    print(f"🌡️  今日天气：{today_weather}")

    # ✅ 美化天气实况显示
    print(f"📝 天气实况：")
    info_dict = parse_weather_info(today_info)
    if info_dict:
        for key, value in info_dict.items():
            print(f"   • {key}: {value}")
    else:
        print(f"   {today_info}")

    print(f"💨 今日风力：{today_wind}")

    print("\n" + "-" * 60)
    print("📋 生活指数")
    print("-" * 60)

    # 解析生活指数
    if life_index and "感冒指数" in life_index:
        for line in life_index.split("\n"):
            if line.strip():
                print(f"   {line}")

    print("\n" + "-" * 60)
    print("📅 未来三天预报")
    print("-" * 60)
    print(f"   明天：{tomorrow_weather}  {tomorrow_temp}  {tomorrow_wind}")
    print(f"   后天：{day3_weather}  {day3_temp}  {day3_wind}")

    # 🆕 添加城市信息
    print("\n" + "-" * 60)
    print("🏙️  城市简介")
    print("-" * 60)
    # 自动换行，每行不超过 50 字符
    wrapped_info = textwrap.fill(city_info, width=50)
    for line in wrapped_info.split("\n"):
        print(f"   {line}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    city = "北京"
    format_weather(fetch_weather(city))
