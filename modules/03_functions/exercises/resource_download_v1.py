import os

import requests

# 全局变量：记录已下载的资源（按类型区分）
downloaded_images = set()
downloaded_videos = set()
downloaded_nba = set()


# ==================== 1. 图片下载专区 ====================
def download_image():
    """下载花瓣网图片专区"""
    image_dict = {
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
    }

    while True:
        print("\n--- 图片下载专区 ---")
        for key, (name, url) in image_dict.items():
            if key not in downloaded_images:
                print(f"  {key}. {name}")

        choice = input("\n请输入要下载的编号（输入 Q/q 退出）: ").strip()
        if choice.upper() == "Q":
            break

        if choice not in image_dict:
            print("❌ 无效选项，请重新输入。")
            continue

        name, url = image_dict[choice]
        if choice in downloaded_images:
            print("✅ 已下载过，跳过。")
            continue

        # 下载图片
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        try:
            res = requests.get(url, headers=headers)
            if res.status_code == 200:
                filename = f"{name}.jpg"
                with open(filename, "wb") as f:
                    f.write(res.content)
                downloaded_images.add(choice)
                print(f"✅ 成功下载: {filename}")
            else:
                print(f"❌ 下载失败: {url}")
        except Exception as e:
            print(f"❌ 下载出错: {e}")


# ==================== 2. 抖音短视频下载专区 ====================
def download_douyin():
    """下载抖音短视频专区"""
    video_dict = {
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
    }

    while True:
        print("\n--- 抖音短视频下载专区 ---")
        for key, (name, url) in video_dict.items():
            if key not in downloaded_videos:
                print(f"  {key}. {name}")

        choice = input("\n请输入要下载的编号（输入 Q/q 退出）: ").strip()
        if choice.upper() == "Q":
            break

        if choice not in video_dict:
            print("❌ 无效选项，请重新输入。")
            continue

        name, url = video_dict[choice]
        if choice in downloaded_videos:
            print("✅ 已下载过，跳过。")
            continue

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        try:
            res = requests.get(url, headers=headers)
            if res.status_code == 200:
                filename = f"{name}.mp4"
                with open(filename, "wb") as f:
                    f.write(res.content)
                downloaded_videos.add(choice)
                print(f"✅ 成功下载: {filename}")
            else:
                print(f"❌ 下载失败: {url}")
        except Exception as e:
            print(f"❌ 下载出错: {e}")


# ==================== 3. NBA锦集下载专区 ====================
def download_nba():
    """下载NBA锦集专区"""
    nba_dict = {
        "1": ("詹姆斯扣篮", "https://example.com/nba/james.d.mp4"),  # 示例URL
        "2": ("库里三分", "https://example.com/nba/curry.d.mp4"),
        "3": ("杜兰特得分", "https://example.com/nba/durant.d.mp4"),
    }

    while True:
        print("\n--- NBA锦集下载专区 ---")
        for key, (name, url) in nba_dict.items():
            if key not in downloaded_nba:
                print(f"  {key}. {name}")

        choice = input("\n请输入要下载的编号（输入 Q/q 退出）: ").strip()
        if choice.upper() == "Q":
            break

        if choice not in nba_dict:
            print("❌ 无效选项，请重新输入。")
            continue

        name, url = nba_dict[choice]
        if choice in downloaded_nba:
            print("✅ 已下载过，跳过。")
            continue

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        try:
            res = requests.get(url, headers=headers)
            if res.status_code == 200:
                filename = f"{name}.mp4"
                with open(filename, "wb") as f:
                    f.write(res.content)
                downloaded_nba.add(choice)
                print(f"✅ 成功下载: {filename}")
            else:
                print(f"❌ 下载失败: {url}")
        except Exception as e:
            print(f"❌ 下载出错: {e}")


# ==================== 主程序 ====================
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

        if choice == "1":
            download_image()
        elif choice == "2":
            download_douyin()
        elif choice == "3":
            download_nba()
        else:
            print("❌ 无效选项，请重新输入。")


if __name__ == "__main__":
    main()
