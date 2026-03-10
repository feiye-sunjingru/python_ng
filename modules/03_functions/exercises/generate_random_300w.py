import random


def func():
    data_list = []
    for i in range(30000000):
        val = random.randint(1000, 9999)
        data_list.append(val)

    # 再使用时，去 data_list 中获取即可。
    return data_list


def gen_random_num(max_count):
    counter = 0
    while counter < max_count:
        yield random.randint(1000, 9999)
        counter += 1


data_list = gen_random_num(3000000)
# 再使用时，去 data_list 中获取即可。
