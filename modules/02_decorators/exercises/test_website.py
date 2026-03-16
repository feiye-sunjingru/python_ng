"""
快速创建一个网站
"""

from flask import Flask


def auth(func):
    def wrapper(*args, **kwargs):
        print("正在验证用户身份...")
        # 这里可以添加实际的认证逻辑，例如检查用户是否登录
        # 登录了则获取func的返回值，否则返回一个错误提示
        print("用户身份验证成功！")
        res = func(*args, **kwargs)
        return res

    return wrapper


# 创建 Flask 应用实例
app = Flask(__name__)
# 配置：忽略尾随斜杠（可选）
app.url_map.strict_slashes = False


# 定义视图函数（处理请求的函数）:当用户访问某个 URL 时，返回对应的响应内容
# 访问 http://127.0.0.1:5000/index/ → 显示 “首页”
@auth
@app.route("/index")
def index():
    return "首页"


# 将 URL 路径与视图函数关联起来
# 相当于app.add_url_rule("/login/", view_func=login)
@app.route("/login")
def login():
    return "登录页面"


@auth
@app.route("/info")
def info():
    return "用户中心"


@auth
@app.route("/order")
def order():
    return "订单中心"


# 启动 Flask 内置的开发服务器
if __name__ == "__main__":
    app.run(debug=True)  # 添加 debug=True 便于调试
