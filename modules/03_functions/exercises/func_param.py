def send_message(content):
    """发送消息函数，recipient默认为'World'"""
    return f"Hello, You have a message: {content}"


def send_image(image_url, content):
    """发送图片函数，recipient默认为'World'"""
    return f"Hello, {content}! You have a new image: {image_url}"


def send_emoji(emoji):
    """发送表情函数，recipient默认为'World'"""
    return f"Hello, You have a new emoji: {emoji}"


def send_file(file_path):
    """发送文件函数，recipient默认为'World'"""
    return f"Hello,You have a new file: {file_path}"


function_dict: dict[str, list] = {
    "1": [send_message, ["这是一个测试消息"]],
    "2": [send_image, ["xxx.png", "这是一个测试图片"]],
    "3": [send_emoji, ["这是一个测试表情"]],
    "4": [send_file, ["这是一个测试文件"]],
}

print("欢迎使用消息发送系统！")
print("请选择要发送的消息类型：1. 消息 2. 图片 3. 表情 4. 文件")
choice = input("请输入选择（1-4）：")
if choice in function_dict:
    func, args = function_dict[choice]
    print(func(*args))
else:
    print("无效的选择，请输入1-4之间的数字。")
