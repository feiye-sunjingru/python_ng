import hashlib
from pathlib import Path

import pandas as pd


def count_char(string, char):
    """计算一个字符在字符串中出现的次数"""
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count


def len_greater_than_5(strings):
    """返回一个列表，包含所有长度大于5的字符串"""
    result = []
    for s in strings:
        if len(s) > 5:
            result.append(s)
    return result


def values_greater_than_10(numbers):
    """返回一个列表，包含所有大于10的数字"""
    result = []
    for num in numbers:
        if num > 10:
            result.append(num)
    return result


def get_max_value(numbers):
    """返回一个列表中的最大值"""
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


def write_student_info(name, gender, age, education):
    """将学生信息写入文件"""
    with Path("tmp_output/student_info.txt").open(mode="a", encoding="utf-8") as f:
        f.write("*".join([name, gender, str(age), education]) + "\n")
        f.write(f"姓名: {name}, 性别: {gender}, 年龄: {age}, 学历: {education}\n")


def select_content_by_keyword(filename, keyword):
    """读文件，根据关键词选择内容"""
    result = []
    file_path = Path(filename)
    if not file_path.exists(file_path):
        return result

    with file_path.open(encoding="utf-8") as f:
        for line in f:
            if keyword in line:
                result.append(line.strip())
    return result


def change_string(string):
    """实现敏感词替换"""
    data_list = ["苍老师", "东京热", "无码", "有码"]
    result = string
    for word in data_list:
        result = result.replace(word, "***")
    return result


def get_user_info_from_xlsx(filename, sheet_name="Sheet1"):
    """从xlsx文件中获取用户信息"""
    df = pd.read_excel(filename, sheet_name=sheet_name)

    # 转换为字典列表（每行是一个用户）
    user_list = df.to_dict(orient="records")

    dict = {}
    for user in user_list:
        dict[user["用户名"]] = user["密码"]

    return dict


def encrypt(origin):
    """md5加密"""
    origin_bytes = origin.encode("utf-8")
    # MD5 对象已经计算了 origin_bytes 的哈希
    md5_obj = hashlib.md5(origin_bytes)
    # 又追加了一次 origin_bytes，相当于加密了两遍相同的数据
    # md5_obj.update(origin_bytes)
    return md5_obj.hexdigest()


def check_user(username, password, user_dict):
    """检查用户是否正确"""
    if username in user_dict:
        if encrypt(password) == user_dict[username]:
            print("登录成功")
        else:
            print("密码错误，请重新输入")
    else:
        print("用户名不存在，请重新输入")


if __name__ == "__main__":
    print(count_char("xxxxaacscf", "a"))
    print(len_greater_than_5(["hello", "world", "python", "programming"]))
    print(values_greater_than_10([5, 15, 25, 35]))
    print(get_max_value([5, 15, 25, 35]))
    write_student_info(name="张三", gender="男", age=18, education="本科")
    print(select_content_by_keyword("tmp_output/student_info.txt", "张三"))
    print(change_string("苍老师是东京热的无码女优"))

    # print(encrypt("admin"))
    # print(encrypt("123123"))
    # print(encrypt("123456"))
    user_dict = get_user_info_from_xlsx("tmp_input/users.xlsx", "s1")
    print(user_dict)

    print("请输入用户名：")
    username = input()
    print("请输入密码：")
    password = input()
    check_user(username, password, user_dict)
    check_user(username, password, user_dict)
    check_user(username, password, user_dict)
