from concurrent.futures.thread import ThreadPoolExecutor
from pathlib import Path

import requests

"""
基于多线程去下载视频
"""


def download_video(url):
    """下载视频内容"""
    res = requests.get(
        url=url,
        headers={
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/\
                537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        },
    )
    return res.content


def outer(file_name):
    """返回一个写入文件的回调函数"""

    def write_file(response):
        content = response.result()  # 获取实际响应内容
        with Path(file_name).open(mode="wb") as file_object:
            file_object.write(content)
        print(f"✅ 已保存: {file_name}")

    return write_file


# 视频列表：(文件名, 下载链接)
video_dict = [
    (
        "tmp_output/东北F4模仿秀.mp4",
        "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvmace0gvch7lo53oog&ratio=720p&line=0",
    ),
    (
        "tmp_output/卡特扣篮.mp4",
        "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f3e0000bv52fpn5t6p007e34qlg&ratio=720p&line=0",
    ),
    (
        "tmp_output/罗斯mvp.mp4",
        "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buer5aa4tij4gv6ajgg&ratio=720p&line=0",
    ),
]

# 创建线程池（最大 10 个线程）
POOL = ThreadPoolExecutor(10)

# 提交任务并添加回调
for item in video_dict:
    future = POOL.submit(download_video, url=item[1])
    # 下载完成后执行回调函数，保存文件：注意这里加的是函数
    future.add_done_callback(outer(item[0]))

# 关闭线程池
POOL.shutdown()  # 关闭线程池
print("✅ 已全部完成")
