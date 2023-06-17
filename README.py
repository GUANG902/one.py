import time

def focus_timer(duration):
    print("专注时钟开始！")
    time.sleep(duration * 60)
    print("专注时钟结束！")

if __name__ == "__main__":
    duration = int(input("请输入专注时长（分钟）："))
    focus_timer(duration)
