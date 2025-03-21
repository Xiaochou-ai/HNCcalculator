import os
import shutil
from datetime import datetime
import tkinter as tk

# 清理旧文件
if os.path.exists('build'):
    shutil.rmtree('build')
if os.path.exists('dist'):
    shutil.rmtree('dist')
for file in os.listdir('.'):
    if file.endswith('.spec'):
        os.remove(file)

# 获取当前时间并格式化
now = datetime.now()
exe_name = f"HuaZhong_Calculator_{now.strftime('%Y年%m月%d日_%H时%M分')}"

# 构建 PyInstaller 命令
cmd = f'pyinstaller -F --noconsole --add-data "hnc-logo.png;." --name "{exe_name}" acceleration_calculator.py'

# 执行打包命令
print(f"将生成: {exe_name}.exe")
os.system(cmd)
print(f"生成完成: {exe_name}.exe")
input("按任意键退出...")

# 5. 更友好的错误提示
def show_error(title, message):
    error_window = tk.Toplevel()
    error_window.title(title)
    error_window.geometry("300x150")
    
    tk.Label(error_window, text=message, wraplength=250).pack(pady=20)
    tk.Button(error_window, text="确定", command=error_window.destroy).pack() 