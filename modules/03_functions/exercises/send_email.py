import logging
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

logging.basicConfig(
    filename="logs/email_send.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)


def send_email(sender_email, sender_password, receiver_email, subject="测试邮件"):
    logging.info(f"尝试发送邮件到 {receiver_email}")

    # 创建邮件对象
    message = MIMEMultipart("alternative")
    message["Subject"] = "测试邮件"
    message["From"] = sender_email
    message["To"] = receiver_email

    # 邮件正文（纯文本和 HTML 可选）
    text = """\
    你好！
    这是一封通过 Python 发送的测试邮件。
    """
    html = """\
    <html>
    <body>
        <p>你好！<br>
        这是一封 <b>HTML</b> 格式的测试邮件。
        </p>
    </body>
    </html>
    """

    # 将文本和 HTML 添加到邮件中
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    # 连接 网易 的 SMTP 服务器并发送
    try:
        # 网易邮箱：smtp.163.com；网易企业邮：smtphz.qiye.163.com
        with smtplib.SMTP_SSL("smtp.163.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("邮件发送成功！")
        logging.info("邮件发送成功")
    except smtplib.SMTPAuthenticationError:
        print("认证失败：请检查授权码是否正确")
    except Exception as e:
        print(f"发送失败：{e}")


if __name__ == "__main__":
    load_dotenv()
    # 邮件配置
    sender_email = os.getenv("SENDER_USERNAME")
    sender_password = os.getenv("SENDER_PASSWORD")
    receiver_email = os.getenv("RECEIVER_USERNAME")

    print("=" * 50)
    print("配置检查：")
    print(f"发件人：{sender_email}")
    print(f"收件人：{receiver_email}")
    print(f"密码长度：{len(sender_password) if sender_password else 0}")
    print("=" * 50)

    # 确认后再发送
    confirm = input(f"确认发送邮件到 {receiver_email}？(y/n): ")
    if confirm.lower() == "y":
        send_email(sender_email, sender_password, receiver_email)
    else:
        print("已取消发送")
