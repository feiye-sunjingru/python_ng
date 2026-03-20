# 下载视频示例
from pathlib import Path

import requests


def download_video(filename, url):
    res = requests.get(
        url=url,
        headers={
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/\
                537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        },
    )
    # wb 模式写入二进制数据
    with Path(f"tmp_output/{filename}.mp4").open(mode="wb") as f:
        f.write(res.content)


if __name__ == "__main__":
    with Path("tmp_input/urls.txt").open("r", encoding="utf8") as f:
        print("正在下载视频...")
        for line in f:
            o = line.strip().split(", ")
            print(o)
            download_video(*o)
            download_video(*o)
            download_video(*o)
