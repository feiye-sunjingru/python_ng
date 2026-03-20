from pathlib import Path
from typing import Any

import requests

# 常量配置
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ..."}

OUTPUT_DIR = "tmp_output"

DB: dict[str, dict[str, Any]] = {
    "1": {
        "area": "下载花瓣网图片专区",
        "resources": {
            "1": (
                "吉他男神",
                "https://hbimg.huabanimg.com/51d46dc32abe7ac7f83b94c67bb8cacc46869954f478-aP4Q3V",
            ),
            "2": (
                "漫画美女",
                "https://hbimg.huabanimg.com/703fdb063bdc37b11033ef794f9b3a7adfa01fd21a6d1-wTFbnO",
            ),
            "3": (
                "游戏地图",
                "https://hbimg.huabanimg.com/b438d8c61ed2abf50ca94e00f257ca7a223e3b64b471-xrzoQd",
            ),
            "4": (
                "alex媳妇",
                "https://hbimg.huabanimg.com/4edba1ed6a71797f52355aa1de5af961b85bf824cb71-px1nZz",
            ),
        },
        "ext": "png",
        "selected": set(),
    },
    "2": {
        "area": "抖音短视频下载专区",
        "resources": {
            "1": (
                "模仿",
                "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvmace0gvch7lo53oog&ratio=720p&line=0",
            ),
            "2": (
                "卡特",
                "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f3e0000bv52fpn5t6p007e34qlg&ratio=720p&line=0",
            ),
            "3": (
                "罗斯",
                "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buer5aa4tij4gv6ajgg&ratio=720p&line=0",
            ),
        },
        "ext": "mp4",
        "selected": set(),
    },
    "3": {
        "area": "NBA锦集下载专区",
        "resources": {
            "1": ("詹姆斯扣篮", "https://example.com/nba/james.d.mp4"),  # 示例URL
            "2": ("库里三分", "https://example.com/nba/curry.d.mp4"),
            "3": ("杜兰特得分", "https://example.com/nba/durant.d.mp4"),
        },
        "ext": "mp4",
        "selected": set(),
    },
}


def download(area: str) -> None:
    """下载指定专区的资源"""
    Path.mkdir(Path(OUTPUT_DIR), exist_ok=True)
    content_dict = DB[area]["resources"]
    ext = DB[area]["ext"]
    selected = DB[area]["selected"]

    while True:
        print(f"\n--- {DB[area]['area']} ---")
        for key, (name, _) in content_dict.items():
            if key not in selected:
                print(f"  {key}. {name}")

        choice = input("\n请输入要下载的编号（输入 Q/q 退出）: ").strip()
        if choice.upper() == "Q":
            break

        if choice not in content_dict:
            print("❌ 无效选项，请重新输入。")
            continue

        name, url = content_dict[choice]
        if choice in selected:
            print("✅ 已下载过，跳过。")
            continue

        try:
            res = requests.get(url, headers=HEADERS)
            if res.status_code == 200:
                filename = f"{name}.{ext}"
                with Path(f"{OUTPUT_DIR}/{filename}").open("wb") as f:
                    f.write(res.content)
                selected.add(choice)
                print(f"✅ 成功下载: {filename}")
            else:
                print(f"❌ 下载失败: {url}")
        except Exception as e:
            print(f"❌ 下载出错: {e}")


def main():
    """主菜单"""
    print("🎯 欢迎使用资源下载器！")
    while True:
        print("\n请选择下载专区：")
        print("  1. 下载花瓣网图片专区")
        print("  2. 下载抖音短视频专区")
        print("  3. 下载NBA锦集专区")
        print("  Q/q: 退出程序")

        choice = input("\n请输入选择（1-3 或 Q/q）: ").strip()
        if choice.upper() == "Q":
            print("👋 再见！")
            break

        if choice in DB:
            download(choice)
        else:
            print("❌ 无效选项，请重新输入。")


if __name__ == "__main__":
    main()
