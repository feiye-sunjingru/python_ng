import requests


def write_file(*args, **kwargs):
    """
    将天气信息拼接起来，并写入到文件
    格式要求：
    1. 每个城市的天气占一行
    2. 每行的格式为: city-北京,cityid-101010100,temp-18...
    """
    with open("tmp_output/weather_info.txt", "w", encoding="utf-8") as f:
        for weather_info in args:
            city = weather_info["weatherinfo"]["city"]
            cityid = weather_info["weatherinfo"]["cityid"]
            temp = weather_info["weatherinfo"]["temp"]
            wind = weather_info["weatherinfo"]["WD"] + weather_info["weatherinfo"]["WS"]
            line = f"city-{city},cityid-{cityid},temp-{temp},wind-{wind}\n"
            f.write(line)


def get_weather(code):
    """获取天气信息"""
    url = "http://www.weather.com.cn/data/ks/{}.html".format(code)
    res = requests.get(url=url)
    res.encoding = "utf-8"
    weather_dict = res.json()
    return weather_dict


city_list = [{"code": "101020100", "title": "上海"}, {"code": "101010100", "title": "北京"}]

if __name__ == "__main__":
    weather_info_list = []
    for city in city_list:
        weather_info = get_weather(city["code"])
        weather_info_list.append(weather_info)

    # print(weather_info_list)
    write_file(*weather_info_list)
