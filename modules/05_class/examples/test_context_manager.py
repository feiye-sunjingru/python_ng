class MyResource:
    def __enter__(self):
        print("资源已打开")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("资源已释放")


with MyResource() as res:
    pass
