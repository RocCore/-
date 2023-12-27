import time
import tkinter as tk

def start_timer(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time_label.config(text=timer)
        time_window.update()
        time.sleep(1)
        seconds -= 1
    time_label.config(text="Time's up!")

def start_focus_timer():
    minutes = int(entry.get())
    start_timer(minutes)

# 创建窗口
time_window = tk.Tk()
time_window.title("Focus Timer")

# 添加标签和输入框
label = tk.Label(time_window, text="Enter focus time (minutes):")
label.pack(pady=10)

entry = tk.Entry(time_window)
entry.pack(pady=10)

# 添加开始按钮
start_button = tk.Button(time_window, text="Start Focus Timer", command=start_focus_timer)
start_button.pack(pady=10)

# 添加计时器标签
time_label = tk.Label(time_window, text="")
time_label.pack(pady=10)

# 运行窗口
time_window.mainloop()
