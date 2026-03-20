# 生成图片验证码的示例代码
# 需要提前安装 pillow 模块：pip3 install pillow

import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def create_image_code(
    img_file_path, text=None, size=(120, 30), mode="RGB", bg_color=(255, 255, 255)
):
    """
    生成一个图片验证码
    :param img_file_path: 输出图片路径
    :param text: 自定义验证码文本（可选）
    :param size: 图片尺寸 (宽, 高)
    :param mode: 图片模式（默认 RGB）
    :param bg_color: 背景颜色（默认白色）
    :return: 验证码字符串
    """
    # 字符集：小写字母（去掉 i, l, o, z）、大写字母、数字
    _letter_cases = "abcdefghjkmnpqrstuvwxxy"  # 去除可能干扰的 i, l, o, z
    _upper_cases = _letter_cases.upper()
    _numbers = "".join(map(str, range(3, 10)))  # 数字 3-9（避免 0 和 1）
    chars = "".join([_letter_cases, _upper_cases, _numbers])

    width, height = size  # 宽高

    # 创建图像
    img = Image.new(mode, size, bg_color)
    draw = ImageDraw.Draw(img)  # 创建画笔

    def get_chars():
        """生成给定长度的字符列表"""
        return random.sample(chars, 4)

    def create_lines():
        """绘制干扰线"""
        line_num = random.randint(1, 2)  # 干扰线条数
        for _ in range(line_num):
            begin = (random.randint(0, size[0]), random.randint(0, size[1]))
            end = (random.randint(0, size[0]), random.randint(0, size[1]))
            draw.line([begin, end], fill=(0, 0, 0))  # 黑色线条

    def create_points():
        """绘制干扰点"""
        chance = min(100, max(0, 2))  # 干扰点出现概率控制在 [0, 100]
        for w in range(width):
            for h in range(height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    draw.point((w, h), fill=(0, 0, 0))

    def create_code():
        """绘制验证码字符"""
        if text:
            code_string = text
        else:
            char_list = get_chars()
            code_string = "".join(
                char_list
            )  # 每个字符前后以空格隔开（实际不加空格更常见）

        # 设置字体（根据系统选择）
        # Windows 系统字体
        # font = ImageFont.truetype(r"C:\Windows\Fonts\SEGOEPR.TTF", size=24)
        # Mac 系统字体
        # font = ImageFont.truetype("/System/Library/Fonts/SFNSRounded.ttf", size=24)
        # 项目字体文件（推荐）
        font = ImageFont.truetype("tmp_input/msyh.ttc", size=15)  # 微软雅黑

        draw.text((0, 0), code_string, "red", font=font)
        return code_string

    # 执行绘制
    create_lines()
    create_points()
    code = create_code()

    # 将图片写入文件
    with Path(img_file_path).open(mode="wb") as img_object:
        img.save(img_object)

    return code


# 使用示例
if __name__ == "__main__":
    code = create_image_code("tmp_output/图片验证码.png")
    print(f"生成的验证码为: {code}")
