COUNTRY = "中国"
CITY_LIST = ["北京", "上海", "深圳"]


def download():
    url = "http://www.xxx.com"
    # CITY_LIST = ["河北", "河南", "山西"]
    CITY_LIST.append("广州")
    print(url)
    print(COUNTRY)
    print(CITY_LIST)


def upload():
    file_name = "rose.zip"
    print(COUNTRY)
    print(CITY_LIST)


print(COUNTRY)
download()
print(CITY_LIST)
