import tkinter as tk
from tkinter import ttk, messagebox
import os
import sys
from functools import lru_cache
from typing import Tuple, Dict
import csv
from datetime import datetime
import re

# 添加输入验证函数
def validate_float(value, action):
    """验证输入是否为有效的浮点数"""
    # 删除操作总是允许
    if action == '0':  # 删除操作
        return True
    
    # 空字符串是允许的
    if value == "":
        return True
    
    # 允许输入小数点和负号
    if value in ['.', '-', '-.']:
        return True
    
    # 验证是否为有效的浮点数
    try:
        float(value)
        return True
    except ValueError:
        return False

def validate_positive_float(value, action):
    """验证输入是否为有效的正浮点数"""
    # 删除操作总是允许
    if action == '0':  # 删除操作
        return True
    
    # 空字符串是允许的
    if value == "":
        return True
    
    # 允许输入小数点
    if value == '.':
        return True
    
    # 验证是否为有效的正浮点数
    try:
        num = float(value)
        # 允许输入，但不验证是否为正数，让计算函数处理错误
        return True
    except ValueError:
        return False

def validate_integer(value, action):
    """验证输入是否为有效的整数"""
    # 删除操作总是允许
    if action == '0':  # 删除操作
        return True
    
    # 空字符串是允许的
    if value == "":
        return True
    
    # 允许输入负号
    if value == '-':
        return True
    
    # 验证是否为有效的整数
    if re.match(r'^-?\d+$', value):
        return True
    else:
        return False

def validate_positive_integer(value, action):
    """验证输入是否为有效的正整数"""
    # 删除操作总是允许
    if action == '0':  # 删除操作
        return True
    
    # 空字符串是允许的
    if value == "":
        return True
    
    # 验证是否为有效的正整数
    if re.match(r'^\d+$', value):
        return True
    else:
        return False

# 在文件顶部添加常量定义
class Constants:
    PRIMARY_COLOR = '#6B5B95'
    LIGHT_COLOR = '#F4F3F9'
    TEXT_COLOR = '#2F184B'
    ENTRY_WIDTH = 15  # 增加输入框宽度
    FONT_NORMAL = ('微软雅黑', 11)  # 增加基础字体大小
    FONT_TITLE = ('微软雅黑', 14, 'bold')  # 增加标题字体大小

# 定义按钮样式
button_style = {
    'font': Constants.FONT_NORMAL,
    'bg': Constants.PRIMARY_COLOR,
    'fg': 'white',
    'padx': 20,
    'pady': 5,
    'relief': 'raised',
    'cursor': 'hand2'
}

def resource_path(relative_path):
    """ 获取资源的绝对路径 """
    try:
        # PyInstaller创建临时文件夹，将路径存储在_MEIPASS中
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# 添加输入验证函数
def validate_float(value, action, widget=None):
    """验证输入是否为有效的浮点数"""
    # 删除操作总是允许
    if action == '0':  # 删除操作
        return True
    
    # 空字符串是允许的
    if value == "":
        if widget:
            widget.config(background="white")
        return True
    
    # 允许输入小数点和负号
    if value in ['.', '-', '-.']:
        if widget:
            widget.config(background="#FFFFCC")  # 淡黄色表示输入未完成
        return True
    
    # 验证是否为有效的浮点数
    try:
        float(value)
        if widget:
            widget.config(background="#E6FFE6")  # 淡绿色表示有效输入
        return True
    except ValueError:
        if widget:
            widget.config(background="#FFE6E6")  # 淡红色表示无效输入
        return False

def validate_positive_float(value, action, widget=None):
    """验证输入是否为有效的正浮点数"""
    # 删除操作总是允许
    if action == '0':  # 删除操作
        return True
    
    # 空字符串是允许的
    if value == "":
        if widget:
            widget.config(background="white")
        return True
    
    # 允许输入小数点
    if value == '.':
        if widget:
            widget.config(background="#FFFFCC")  # 淡黄色表示输入未完成
        return True
    
    # 验证是否为有效的正浮点数
    try:
        num = float(value)
        if num <= 0:
            if widget:
                widget.config(background="#FFE6E6")  # 淡红色表示无效输入
            return True  # 仍然允许输入，但标记为错误
        else:
            if widget:
                widget.config(background="#E6FFE6")  # 淡绿色表示有效输入
            return True
    except ValueError:
        if widget:
            widget.config(background="#FFE6E6")  # 淡红色表示无效输入
        return False

def validate_integer(value, action, widget=None):
    """验证输入是否为有效的整数"""
    # 删除操作总是允许
    if action == '0':  # 删除操作
        return True
    
    # 空字符串是允许的
    if value == "":
        if widget:
            widget.config(background="white")
        return True
    
    # 允许输入负号
    if value == '-':
        if widget:
            widget.config(background="#FFFFCC")  # 淡黄色表示输入未完成
        return True
    
    # 验证是否为有效的整数
    if re.match(r'^-?\d+$', value):
        if widget:
            widget.config(background="#E6FFE6")  # 淡绿色表示有效输入
        return True
    else:
        if widget:
            widget.config(background="#FFE6E6")  # 淡红色表示无效输入
        return False

def validate_positive_integer(value, action, widget=None):
    """验证输入是否为有效的正整数"""
    # 删除操作总是允许
    if action == '0':  # 删除操作
        return True
    
    # 空字符串是允许的
    if value == "":
        if widget:
            widget.config(background="white")
        return True
    
    # 验证是否为有效的正整数
    if re.match(r'^\d+$', value):
        num = int(value)
        if num <= 0:
            if widget:
                widget.config(background="#FFE6E6")  # 淡红色表示无效输入
            return True  # 仍然允许输入，但标记为错误
        else:
            if widget:
                widget.config(background="#E6FFE6")  # 淡绿色表示有效输入
            return True
    else:
        if widget:
            widget.config(background="#FFE6E6")  # 淡红色表示无效输入
        return False

def create_validation_command(root, validation_func, widget=None):
    """创建验证命令"""
    return (root.register(lambda val, action: validation_func(val, action, widget)), '%P', '%d')

# 添加输入验证装饰器
def validate_input(func):
    def wrapper():
        try:
            status_bar.config(text="计算中...")
            func()
            status_bar.config(text="计算完成")
        except ValueError as e:
            messagebox.showerror("输入错误", str(e))
            status_bar.config(text=f"错误: {str(e)}")
        except Exception as e:
            messagebox.showerror("系统错误", f"发生意外错误: {str(e)}")
            status_bar.config(text="发生系统错误")
    return wrapper

# 修改计算函数
@validate_input
def calculate_acceleration():
    # 获取输入值
    acc_time_str = acc_entry.get()
    acc_g_str = acc_g_result_entry.get()
    
    # 检查哪个值被输入了
    if acc_time_str and not acc_g_str:  # 如果输入了时间常数
        acceleration_time = float(acc_time_str)
        if acceleration_time <= 0:
            raise ValueError("时间常数必须大于0")
        # 计算加速度
        acceleration = (1000 * 1000) / (60 * acceleration_time * 9.8 * 1000)
        # 显示结果
        acc_g_result_entry.delete(0, tk.END)
        acc_g_result_entry.insert(0, f"{acceleration:.5f}")
    elif acc_g_str and not acc_time_str:  # 如果输入了加速度
        acceleration = float(acc_g_str)
        if acceleration <= 0:
            raise ValueError("加速度必须大于0")
        # 计算时间常数
        acceleration_time = (1000 * 1000) / (60 * acceleration * 9.8 * 1000)
        # 显示结果
        acc_entry.delete(0, tk.END)
        acc_entry.insert(0, f"{acceleration_time:.2f}")
    elif acc_time_str and acc_g_str:
        raise ValueError("请只填写一个参数")
    else:
        raise ValueError("请填写一个参数")

    # 在计算结果后添加保存历史记录
    result_value = acceleration if acc_time_str else acceleration_time
    save_history("常规计算", {
        "时间常数(ms)": acc_time_str,
        "加速度(g)": acc_g_str
    }, result_value)

def clear_acc_fields():
    """清空加速度计算相关的输入框"""
    acc_entry.delete(0, tk.END)
    acc_g_result_entry.delete(0, tk.END)
    jerk_entry.delete(0, tk.END)

def calculate_g00():
    try:
        # 获取快移速度（必填）
        speed = float(speed_entry.get())
        if speed <= 0:
            raise ValueError("快移速度必须大于0")
            
        # 获取加速度和参数值
        acc_g_str = acc_g_entry.get()
        param216_str = param216_entry.get()
        
        # 检查加速度和参数值的填写情况
        if acc_g_str and not param216_str:  # 如果填写了加速度
            acceleration_g = float(acc_g_str)
            if acceleration_g <= 0:
                raise ValueError("加速度必须大于0")
            # 计算216号参数
            param216 = (speed * 1000 / 60) / (acceleration_g * 9.8 * 1000) * 1000
            # 显示结果
            param216_entry.delete(0, tk.END)
            param216_entry.insert(0, f"{param216:.2f}")
        elif param216_str and not acc_g_str:  # 如果填写了参数值
            param216 = float(param216_str)
            if param216 <= 0:
                raise ValueError("参数值必须大于0")
            # 计算加速度
            acceleration_g = (speed * 1000 / 60) / (param216 * 9.8)
            # 显示结果
            acc_g_entry.delete(0, tk.END)
            acc_g_entry.insert(0, f"{acceleration_g:.5f}")
        elif acc_g_str and param216_str:
            raise ValueError("理论加速度和216号参数只需填写一个")
        else:
            raise ValueError("请填写理论加速度或216号参数其中一个")
            
    except ValueError as e:
        messagebox.showerror("输入错误", str(e))

    # 在计算结果后添加保存历史记录
    result_value = param216 if acc_g_str else acceleration_g
    save_history("G00计算", {
        "快移速度(m/min)": speed,
        "加速度(g)": acc_g_str,
        "216号参数(ms)": param216_str
    }, result_value)

def clear_g00_fields():
    """清空G00计算相关的输入框"""
    speed_entry.delete(0, tk.END)
    acc_g_entry.delete(0, tk.END)
    param216_entry.delete(0, tk.END)

def show_about():
    about_window = tk.Toplevel()
    about_window.title("关于")
    about_window.geometry("400x350")  # 增加关于窗口尺寸
    about_window.configure(bg=Constants.LIGHT_COLOR)
    about_window.resizable(False, False)
    
    try:
        logo = tk.PhotoImage(file=resource_path('hnc-logo.png'))
        logo_label = tk.Label(about_window, image=logo, bg=Constants.LIGHT_COLOR)
        logo_label.image = logo
        logo_label.pack(pady=20)  # 增加上下边距
    except Exception as e:
        print(f"无法加载图标: {e}")
    
    info_text = "深圳华中数控\n作者：黄灿峰\n版本：V6.0\n电话：18675540326"
    tk.Label(about_window, text=info_text, 
            justify=tk.CENTER,
            font=('微软雅黑', 12),  # 增加字体大小
            fg=Constants.TEXT_COLOR,
            bg=Constants.LIGHT_COLOR).pack(pady=20)  # 增加上下边距
    
    tk.Button(about_window, text="确定", 
             command=about_window.destroy,
             **button_style).pack(pady=15)  # 增加上下边距
    
    about_window.transient(root)
    about_window.grab_set()
    about_window.focus_set()

# 创建主窗口
root = tk.Tk()
root.title("华中计算器")
root.geometry("800x700")  # 增加窗口尺寸
root.minsize(800, 700)  # 设置最小窗口尺寸

# 配置全局颜色和样式
root.configure(bg=Constants.LIGHT_COLOR)
style = ttk.Style()
style.theme_use('clam')  # 使用clam主题
style.theme_use('clam')
style.configure('TFrame', background=Constants.LIGHT_COLOR)
style.configure('TLabel', background=Constants.LIGHT_COLOR, font=('微软雅黑', 11))
style.configure('TButton', font=('微软雅黑', 11), relief='flat', focuscolor=Constants.PRIMARY_COLOR, focustyle='')

# 设置窗口图标
try:
    icon_path = resource_path('hnc-logo.png')
    if os.path.exists(icon_path):
        icon = tk.PhotoImage(file=icon_path)
        root.iconphoto(True, icon)
except tk.TclError:
    pass  # 忽略图标加载错误
except Exception as e:
    pass  # 忽略其他错误

# 配置全局颜色
root.configure(bg=Constants.LIGHT_COLOR)
style.configure('TFrame', background=Constants.LIGHT_COLOR)
style.configure('TLabel', background=Constants.LIGHT_COLOR, font=('微软雅黑', 11))  # 增加标签字体大小
style.configure('TButton', 
                font=('微软雅黑', 11),  # 增加按钮字体大小
                relief='flat',
                focuscolor=Constants.PRIMARY_COLOR,
                focustyle='')

# 配置输入框样式
entry_style = {
    'font': ('Consolas', 12),  # 增加输入框字体大小
    'bd': 1, 
    'relief':'solid', 
    'width': 15,  # 增加输入框宽度
    'bg': 'white',
    'fg': Constants.TEXT_COLOR
}

# 配置提示标签样式
hint_style = {
    'font': ('微软雅黑', 11),  # 增加提示标签字体大小
    'fg': Constants.TEXT_COLOR,
    'bg': Constants.LIGHT_COLOR
}

# 配置网格布局参数
grid_params = {'padx': 12, 'pady': 10, 'sticky': 'ew'}  # 增加网格间距

# 修改状态栏样式
style.configure('Status.TLabel', 
                background='#E8E8E8',
                foreground=Constants.TEXT_COLOR,
                font=('微软雅黑', 10))  # 增加状态栏字体大小

# 添加菜单栏
menu_bar = tk.Menu(root)
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="计算公式", command=lambda: show_formulas())
help_menu.add_command(label="关于", command=show_about)
menu_bar.add_cascade(label="帮助", menu=help_menu)

# 添加历史记录查看功能
def show_history():
    history_window = tk.Toplevel()
    history_window.title("计算历史记录")
    history_window.geometry("1000x500")  # 增加历史记录窗口尺寸
    history_window.configure(bg=Constants.LIGHT_COLOR)
    
    # 创建树状表格
    columns = ("时间", "操作类型", "参数", "结果")
    tree = ttk.Treeview(history_window, columns=columns, show="headings")
    
    # 设置列宽
    tree.column("时间", width=150)
    tree.column("操作类型", width=100)
    tree.column("参数", width=400)
    tree.column("结果", width=100)
    
    # 设置表头
    for col in columns:
        tree.heading(col, text=col)
    
    # 添加滚动条
    scrollbar = ttk.Scrollbar(history_window, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    
    # 布局
    tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # 读取历史记录
    try:
        with open('history.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                tree.insert("", "end", values=row)
    except FileNotFoundError:
        tree.insert("", "end", values=["暂无历史记录", "", "", ""])

# 在菜单栏添加历史记录查看
history_menu = tk.Menu(menu_bar, tearoff=0)
history_menu.add_command(label="查看历史", command=show_history)
menu_bar.add_cascade(label="历史", menu=history_menu)

# 将菜单栏设置为窗口的菜单栏
root.config(menu=menu_bar)

# 在样式配置部分添加以下内容
style.configure('TNotebook', tabmargins=0)
style.configure('TNotebook.Tab', 
                focuscolor=Constants.PRIMARY_COLOR,  # 设置焦点颜色与背景一致
                focuswidth=0)  # 移除焦点边框宽度

style.configure('child.TNotebook', tabmargins=0)
style.configure('child.TNotebook.Tab', 
                focuscolor=Constants.PRIMARY_COLOR,
                focuswidth=0)

# 修改创建标签页的代码
notebook = ttk.Notebook(root, style='TNotebook')
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)  # 轴快移速度计算标签页
tab4 = ttk.Frame(notebook)  # 添加角度转换标签页
tab5 = ttk.Frame(notebook)  # 添加分数简化标签页
tab6 = ttk.Frame(notebook)  # 添加正余弦偏移计算标签页
notebook.add(tab1, text="常规计算")
notebook.add(tab2, text="G00为2计算")
notebook.add(tab3, text="轴快移速度计算")
notebook.add(tab4, text="角度转换")
notebook.add(tab5, text="分数简化")  # 添加新标签页
notebook.add(tab6, text="正余弦偏移")  # 添加正余弦偏移计算标签页
notebook.pack(expand=True, fill="both", padx=15, pady=15)  # 增加标签页内边距

# 在每个标签页顶部添加标题
def create_section_title(parent: ttk.Frame, text: str) -> ttk.Frame:
    title_frame = ttk.Frame(parent)
    ttk.Label(title_frame, text=text, font=('微软雅黑', 14, 'bold'),  # 增加标题字体大小
             foreground=Constants.PRIMARY_COLOR).pack(side=tk.LEFT)
    ttk.Separator(title_frame, orient=tk.HORIZONTAL).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)  # 增加分隔符内边距
    return title_frame

# 轴快移速度计算界面 (tab3)
# 添加ToolTip类
class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)
    
    def show_tooltip(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        
        # 创建一个顶级窗口
        self.tooltip = tk.Toplevel()
        self.tooltip.wm_overrideredirect(True)  # 移除窗口边框
        self.tooltip.wm_geometry(f"+{x}+{y}")
        
        # 创建带有内边距的标签
        label = tk.Label(self.tooltip, text=self.text, 
                         background="#FFFFDD", foreground="#333333",
                         relief="solid", borderwidth=1,
                         font=("微软雅黑", 11),  # 增加提示文本字体大小
                         padx=10, pady=5)  # 增加提示文本内边距
        label.pack()
    
    def hide_tooltip(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

# 在创建子标签页时添加事件绑定
def remove_focus(event):
    event.widget.master.focus_set()

# 完整的轴速度计算器函数
def create_axis_speed_calculator():
    # 移除虚线框，添加以下样式配置
    style.configure('child.TNotebook.Tab', borderwidth=0)
    style.configure('child.TFrame', borderwidth=0, relief='flat')
    
    # 创建子标签页
    axis_notebook = ttk.Notebook(tab3, style='child.TNotebook')
    linear_tab = ttk.Frame(axis_notebook, style='child.TFrame')
    rotate_tab = ttk.Frame(axis_notebook, style='child.TFrame')  # 修复样式问题
    axis_notebook.bind('<<NotebookTabChanged>>', remove_focus)
    axis_notebook.add(linear_tab, text="直线轴")
    axis_notebook.add(rotate_tab, text="旋转轴")
    axis_notebook.pack(expand=True, fill="both", padx=10, pady=10)  # 增加内边距
    
    # 直线轴页面添加标题
    title_frame_linear = create_section_title(linear_tab, "直线轴快移速度计算")
    title_frame_linear.grid(row=0, column=0, columnspan=2, pady=15, sticky='ew')  # 增加上下边距

    # 直线轴界面
    tk.Label(linear_tab, text="丝杠螺距 (mm):", font=('微软雅黑', 11)).grid(row=1, column=0, **grid_params)
    screw_pitch_entry = tk.Entry(linear_tab, **entry_style, takefocus=False, 
                                validate='key', 
                                validatecommand=(root.register(validate_positive_float), '%P', '%d'))
    screw_pitch_entry.grid(row=1, column=1, **grid_params)

    tk.Label(linear_tab, text="PA17轴最大转速 (转/分):", font=('微软雅黑', 11)).grid(row=2, column=0, **grid_params)
    linear_max_speed_entry = tk.Entry(linear_tab, **entry_style, takefocus=False, 
                                     validate='key', 
                                     validatecommand=(root.register(validate_positive_float), '%P', '%d'))
    linear_max_speed_entry.grid(row=2, column=1, **grid_params)

    tk.Label(linear_tab, text="直线轴快移速度 (mm/min):", font=('微软雅黑', 11)).grid(row=3, column=0, **grid_params)
    linear_result_entry = tk.Entry(linear_tab, **entry_style, takefocus=False)
    linear_result_entry.grid(row=3, column=1, **grid_params)

    # 按钮框架
    linear_button_frame = tk.Frame(linear_tab)
    linear_button_frame.grid(row=4, column=0, columnspan=2, pady=15)  # 增加上下边距

    # 计算直线轴速度的函数
    def calculate_linear_speed():
        try:
            # 获取输入值
            screw_pitch = float(screw_pitch_entry.get())
            max_speed = float(linear_max_speed_entry.get())
            
            if screw_pitch <= 0 or max_speed <= 0:
                raise ValueError("参数必须大于0")
                
            # 计算直线轴快移速度
            linear_speed = screw_pitch * max_speed
            
            # 显示结果
            linear_result_entry.delete(0, tk.END)
            linear_result_entry.insert(0, f"{linear_speed:.2f}")
    
            # 添加计算历史记录
            save_history("直线轴计算", {
                "screw_pitch": screw_pitch,
                "max_speed": max_speed
            }, linear_speed)
        except ValueError as e:
            messagebox.showerror("输入错误", str(e))
    
    # 清空直线轴计算相关的输入框
    def clear_linear_fields():
        screw_pitch_entry.delete(0, tk.END)
        linear_max_speed_entry.delete(0, tk.END)
        linear_result_entry.delete(0, tk.END)

    # 计算按钮
    linear_calc_btn = tk.Button(linear_button_frame, text="计算", command=calculate_linear_speed, **button_style)
    linear_calc_btn.pack(side=tk.LEFT, padx=10)  # 增加左右边距

    # 清除按钮
    linear_clear_btn = tk.Button(linear_button_frame, text="清除", command=clear_linear_fields, **button_style)
    linear_clear_btn.pack(side=tk.LEFT, padx=10)  # 增加左右边距

    # 提示标签
    linear_hint_label = tk.Label(linear_tab, text="提示：填写丝杠螺距和最大转速计算快移速度", **hint_style)
    linear_hint_label.grid(row=5, column=0, columnspan=2, pady=10)  # 增加上下边距

    # 旋转轴页面添加标题
    title_frame_rotate = create_section_title(rotate_tab, "旋转轴快移速度计算")
    title_frame_rotate.grid(row=0, column=0, columnspan=2, pady=15, sticky='ew')  # 增加上下边距

    # 旋转轴界面
    tk.Label(rotate_tab, text="PA17轴最大转速 (转/分):", font=('微软雅黑', 11)).grid(row=1, column=0, **grid_params)
    rotate_max_speed_entry = tk.Entry(rotate_tab, **entry_style, takefocus=False, 
                                     validate='key', 
                                     validatecommand=(root.register(validate_positive_float), '%P', '%d'))
    rotate_max_speed_entry.grid(row=1, column=1, **grid_params)

    # 修改减速比输入部分为横向布局
    ratio_frame = tk.Frame(rotate_tab)
    ratio_frame.grid(row=2, column=0, columnspan=2, pady=10)

    # 为减速比输入框创建特殊的样式（复制entry_style但修改width）
    ratio_entry_style = entry_style.copy()
    ratio_entry_style['width'] = 8

    tk.Label(ratio_frame, text="减速比 = 电机端").pack(side=tk.LEFT, padx=2)
    motor_ratio_entry = tk.Entry(ratio_frame, **ratio_entry_style, takefocus=False, 
                                validate='key', 
                                validatecommand=(root.register(validate_positive_integer), '%P', '%d'))
    motor_ratio_entry.pack(side=tk.LEFT, padx=2)
    tk.Label(ratio_frame, text=":").pack(side=tk.LEFT, padx=2)
    mech_ratio_entry = tk.Entry(ratio_frame, **ratio_entry_style, takefocus=False, 
                               validate='key', 
                               validatecommand=(root.register(validate_positive_integer), '%P', '%d'))
    mech_ratio_entry.pack(side=tk.LEFT, padx=2)
    tk.Label(ratio_frame, text="机械端").pack(side=tk.LEFT, padx=2)

    tk.Label(rotate_tab, text="旋转轴快移速度 (度/分):", font=('微软雅黑', 11)).grid(row=3, column=0, **grid_params)
    rotate_result_entry = tk.Entry(rotate_tab, **entry_style, takefocus=False)
    rotate_result_entry.grid(row=3, column=1, **grid_params)

    # 按钮框架
    rotate_button_frame = tk.Frame(rotate_tab)
    rotate_button_frame.grid(row=4, column=0, columnspan=2, pady=15)  # 增加上下边距
    
    # 计算旋转轴速度的函数
    @lru_cache(maxsize=32)
    def calculate_rotate_speed_core(max_speed, motor_ratio, mech_ratio):
        ratio = motor_ratio / mech_ratio
        return max_speed * 2 * 3.14 * 57.3 / ratio
    
    def calculate_rotate_speed():
        try:
            # 获取输入值
            max_speed = float(rotate_max_speed_entry.get())
            motor_ratio = float(motor_ratio_entry.get())    # 电机端
            mech_ratio = float(mech_ratio_entry.get())      # 机械端
            
            if max_speed <= 0 or motor_ratio <= 0 or mech_ratio <= 0:
                raise ValueError("参数必须大于0")
                
            # 计算旋转轴快移速度：最大速度*2*π*57.3/(电机端/机械端)
            rotate_speed = calculate_rotate_speed_core(max_speed, motor_ratio, mech_ratio)
            
            # 显示结果
            rotate_result_entry.delete(0, tk.END)
            rotate_result_entry.insert(0, f"{rotate_speed:.2f}")
    
            # 在计算结果后添加保存历史记录
            save_history("旋转轴计算", {
                "最大转速(rpm)": max_speed,
                "电机端减速比": motor_ratio,
                "机械端减速比": mech_ratio
            }, rotate_speed)
        except ValueError as e:
            messagebox.showerror("输入错误", str(e))
    
    # 清空旋转轴相关输入框的函数
    def clear_rotate_fields():
        rotate_max_speed_entry.delete(0, tk.END)
        motor_ratio_entry.delete(0, tk.END)
        mech_ratio_entry.delete(0, tk.END)
        rotate_result_entry.delete(0, tk.END)

    # 计算按钮
    rotate_calc_btn = tk.Button(rotate_button_frame, text="计算", command=calculate_rotate_speed, **button_style)
    rotate_calc_btn.pack(side=tk.LEFT, padx=10)  # 增加左右边距

    # 清除按钮
    rotate_clear_btn = tk.Button(rotate_button_frame, text="清除", command=clear_rotate_fields, **button_style)
    rotate_clear_btn.pack(side=tk.LEFT, padx=10)  # 增加左右边距

    # 提示标签
    rotate_hint_label = tk.Label(rotate_tab, text="提示：填写最大转速和减速比计算快移速度", **hint_style)
    rotate_hint_label.grid(row=5, column=0, columnspan=2, pady=10)  # 增加上下边距
    
    # 添加工具提示
    ToolTip(screw_pitch_entry, "丝杠螺距，单位：mm")
    ToolTip(motor_ratio_entry, "减速比电机端数值")
    ToolTip(mech_ratio_entry, "减速比机械端数值")

# 确保在合适的位置调用创建轴速度计算器的函数
create_axis_speed_calculator()

# 在主窗口底部添加状态栏
status_bar = ttk.Label(root, text="就绪", relief=tk.SUNKEN, anchor=tk.W, style='Status.TLabel')
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# 在创建主窗口后添加样式配置之前，添加工具提示类
# 在创建完输入框后添加工具提示
def create_tooltips():
    ToolTip(acc_entry, "输入范围: 0.1-1000ms")
    ToolTip(acc_g_result_entry, "加速度值，单位：g")
    ToolTip(jerk_entry, "捷度时间常数，单位：ms")
    ToolTip(speed_entry, "理论快移速度，单位：m/min")
    ToolTip(param216_entry, "216号参数值，单位：ms")

# 添加模块文档字符串
"""
华中数控加速度计算器
版本：6.0
功能：
1. 常规加速度计算
2. G00参数计算
3. 轴快移速度计算
作者：黄灿峰
联系方式：18675540326
"""

# 添加计算历史记录
def save_history(operation: str, params: dict, result: float):
    with open('history.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            operation,
            str(params),
            result
        ])

# 在创建主窗口后添加
root.option_add('*focusHighlight', False)
root.option_add('*focusColor', Constants.LIGHT_COLOR)

# 创建一个不可见的控件并设置焦点
invisible_label = tk.Label(root, text="", height=0, width=0)
invisible_label.pack()
invisible_label.focus_set()

# 显示计算公式的函数
def show_formulas():
    formula_window = tk.Toplevel()
    formula_window.title("计算公式")
    formula_window.geometry("600x500")
    formula_window.configure(bg=Constants.LIGHT_COLOR)
    
    # 创建一个带滚动条的文本框
    frame = tk.Frame(formula_window, bg=Constants.LIGHT_COLOR)
    frame.pack(fill="both", expand=True, padx=10, pady=10)
    
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")
    
    text = tk.Text(frame, wrap="word", bg=Constants.LIGHT_COLOR, fg=Constants.TEXT_COLOR, 
                   font=('微软雅黑', 11), padx=10, pady=10,
                   yscrollcommand=scrollbar.set)
    text.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=text.yview)
    
    # 设置文本为只读模式
    text.config(state="normal")
    
    # 添加公式内容
    formula_text = """# 计算公式说明

## 1. 常规计算

### 加速度计算
加速度(g) = (1000 * 1000) / (60 * 时间常数(ms) * 9.8 * 1000)

### 时间常数计算
时间常数(ms) = (1000 * 1000) / (60 * 加速度(g) * 9.8 * 1000)

## 2. G00参数计算

### 216号参数计算
216号参数(ms) = (快移速度(m/min) * 1000 / 60) / (加速度(g) * 9.8 * 1000) * 1000

### 加速度计算
加速度(g) = (快移速度(m/min) * 1000 / 60) / (216号参数(ms) * 9.8)

## 3. 直线轴快移速度计算

直线轴快移速度(mm/min) = 丝杠螺距(mm) * 轴最大转速(转/分)

## 4. 旋转轴快移速度计算

旋转轴快移速度(度/分) = 最大转速(转/分) * 2 * π * 57.3 / (电机端减速比 / 机械端减速比)

## 5. 角度单位转换

### 度与其他单位的转换关系
- 弧度(rad) = 度(°) × (π / 180)
- 百分度(gon) = 度(°) × (10/9)
- 角分(') = 度(°) × 60
- 角秒(") = 度(°) × 3600
- 毫角秒(mas) = 度(°) × 3600000
- 微角秒(μas) = 度(°) × 3600000000

### 其他单位转换为度
- 度(°) = 弧度(rad) × (180 / π)
- 度(°) = 百分度(gon) × (9/10)
- 度(°) = 角分(') / 60
- 度(°) = 角秒(") / 3600
- 度(°) = 毫角秒(mas) / 3600000
- 度(°) = 微角秒(μas) / 3600000000

## 6. 分数简化计算

分数简化是通过计算分子和分母的最大公约数(GCD)实现的。

### 最大公约数（欧几里得算法）
GCD(a, b) = a                  如果 b = 0
GCD(a, b) = GCD(b, a mod b)    其他情况

### 分数简化
分子 ÷ 最大公约数 = 简化后的分子
分母 ÷ 最大公约数 = 简化后的分母

例如:
55/99 = (5×11)/(9×11) = 5/9

## 7. 正余弦偏移计算

### 正弦信号幅值偏移值 (PB5)
PB5 = (正弦波峰绝对值 - 正弦波谷绝对值) / (正弦波峰绝对值 + 正弦波谷绝对值) * 100

### 余弦信号幅值偏移值 (PB6)
PB6 = (余弦波峰绝对值 - 余弦波谷绝对值) / (余弦波峰绝对值 + 余弦波谷绝对值) * 100

### 正余弦信号幅值不匹配值 (PB7)
PB7 = (正弦幅值 - 余弦幅值) / ((正弦幅值 + 余弦幅值) / 2) * 100
其中:
- 正弦幅值 = (正弦波峰绝对值 + 正弦波谷绝对值) / 2
- 余弦幅值 = (余弦波峰绝对值 + 余弦波谷绝对值) / 2

## 8. 登奇电机选型计算

### 额定扭矩计算
额定扭矩(Nm) = 静态扭矩(Nm) × 额定扭矩电流系数

### 额定电流计算
额定电流(A) = 线电流(A) × 额定扭矩电流系数

### 额定功率计算
额定功率(kW) = 额定转速(rpm) × 额定扭矩(Nm) / 9550

### 额定扭矩电流系数
- 3000rpm: 0.7
- 2000rpm: 0.8
- 1500rpm: 0.85

## 9. 主轴定向脉冲计算

### 第一档主轴定向起始偏移角度PA48
PA48 = (期望定向位置 × 18) / 主轴脉冲
注意: 计算结果向下取整

### 第一档主轴定向位置PA39
PA39 = 期望定向位置 - (PA48 × (主轴脉冲 / 18))
注意: 计算结果四舍五入
"""
    
    text.insert("1.0", formula_text)
    text.config(state="disabled")  # 设置为只读模式
    
    # 添加关闭按钮
    close_button = tk.Button(formula_window, text="关闭", 
                            command=formula_window.destroy,
                            **button_style)
    close_button.pack(pady=10)
    
    # 使窗口成为模态窗口
    formula_window.transient(root)
    formula_window.grab_set()
    formula_window.focus_set()

# 角度转换功能
def create_angle_converter():
    # 添加标题
    title_frame = create_section_title(tab4, "角度单位转换")
    title_frame.grid(row=0, column=0, columnspan=2, pady=15, sticky='ew')  # 增加上下边距
    
    # 创建输入框和标签
    angle_labels = [
        "度 (°):", 
        "弧度 (rad):", 
        "百分度 (gon):", 
        "角分 ('):", 
        "角秒 (\"):", 
        "毫角秒 (mas):", 
        "微角秒 (μas):"
    ]
    
    angle_entries = []
    
    for i, label in enumerate(angle_labels):
        tk.Label(tab4, text=label, font=('微软雅黑', 11)).grid(row=i+1, column=0, **grid_params)
        entry = tk.Entry(tab4, **entry_style, takefocus=False, 
                         validate='key', 
                         validatecommand=(root.register(validate_float), '%P', '%d'))
        entry.grid(row=i+1, column=1, **grid_params)
        angle_entries.append(entry)
    
    # 从度转换到其他单位的函数
    def convert_from_degrees(degrees):
        radians = degrees * (3.14159265358979323846 / 180)
        gon = degrees * (10/9)
        minutes = degrees * 60
        seconds = minutes * 60
        mas = seconds * 1000
        muas = mas * 1000
        return radians, gon, minutes, seconds, mas, muas
    
    # 转换功能实现
    def convert_angles(event=None):
        # 确定哪个输入框有值
        for i, entry in enumerate(angle_entries):
            value = entry.get().strip()
            if value and event and event.widget != entry:
                continue
                
            if value:
                try:
                    value = float(value)
                    # 清空其他输入框
                    for j, other_entry in enumerate(angle_entries):
                        if i != j:
                            other_entry.delete(0, tk.END)
                    
                    if i == 0:  # 度
                        rad, gon, minutes, seconds, mas, muas = convert_from_degrees(value)
                        angle_entries[1].insert(0, f"{rad:.6f}")
                        angle_entries[2].insert(0, f"{gon:.6f}")
                        angle_entries[3].insert(0, f"{minutes}")
                        angle_entries[4].insert(0, f"{seconds}")
                        angle_entries[5].insert(0, f"{mas}")
                        angle_entries[6].insert(0, f"{muas}")
                    elif i == 1:  # 弧度
                        degrees = value * (180 / 3.14159265358979323846)
                        rad, gon, minutes, seconds, mas, muas = convert_from_degrees(degrees)
                        angle_entries[0].insert(0, f"{degrees:.6f}")
                        angle_entries[2].insert(0, f"{gon:.6f}")
                        angle_entries[3].insert(0, f"{minutes}")
                        angle_entries[4].insert(0, f"{seconds}")
                        angle_entries[5].insert(0, f"{mas}")
                        angle_entries[6].insert(0, f"{muas}")
                    elif i == 2:  # 百分度
                        degrees = value * (9/10)
                        rad, gon, minutes, seconds, mas, muas = convert_from_degrees(degrees)
                        angle_entries[0].insert(0, f"{degrees:.6f}")
                        angle_entries[1].insert(0, f"{rad:.6f}")
                        angle_entries[3].insert(0, f"{minutes}")
                        angle_entries[4].insert(0, f"{seconds}")
                        angle_entries[5].insert(0, f"{mas}")
                        angle_entries[6].insert(0, f"{muas}")
                    elif i == 3:  # 角分
                        degrees = value / 60
                        rad, gon, minutes, seconds, mas, muas = convert_from_degrees(degrees)
                        angle_entries[0].insert(0, f"{degrees:.6f}")
                        angle_entries[1].insert(0, f"{rad:.6f}")
                        angle_entries[2].insert(0, f"{gon:.6f}")
                        angle_entries[4].insert(0, f"{seconds}")
                        angle_entries[5].insert(0, f"{mas}")
                        angle_entries[6].insert(0, f"{muas}")
                    elif i == 4:  # 角秒
                        degrees = value / 3600
                        rad, gon, minutes, seconds, mas, muas = convert_from_degrees(degrees)
                        angle_entries[0].insert(0, f"{degrees:.6f}")
                        angle_entries[1].insert(0, f"{rad:.6f}")
                        angle_entries[2].insert(0, f"{gon:.6f}")
                        angle_entries[3].insert(0, f"{minutes:.6f}")
                        angle_entries[5].insert(0, f"{mas}")
                        angle_entries[6].insert(0, f"{muas}")
                    elif i == 5:  # 毫角秒
                        degrees = value / 3600000
                        rad, gon, minutes, seconds, mas, muas = convert_from_degrees(degrees)
                        angle_entries[0].insert(0, f"{degrees:.10f}")
                        angle_entries[1].insert(0, f"{rad:.10f}")
                        angle_entries[2].insert(0, f"{gon:.10f}")
                        angle_entries[3].insert(0, f"{minutes:.6f}")
                        angle_entries[4].insert(0, f"{seconds:.6f}")
                        angle_entries[6].insert(0, f"{muas}")
                    elif i == 6:  # 微角秒
                        degrees = value / 3600000000
                        rad, gon, minutes, seconds, mas, muas = convert_from_degrees(degrees)
                        angle_entries[0].insert(0, f"{degrees:.14f}")
                        angle_entries[1].insert(0, f"{rad:.14f}")
                        angle_entries[2].insert(0, f"{gon:.14f}")
                        angle_entries[3].insert(0, f"{minutes:.10f}")
                        angle_entries[4].insert(0, f"{seconds:.10f}")
                        angle_entries[5].insert(0, f"{mas:.6f}")
                    break
                except ValueError:
                    # 如果输入不是数字，清空所有输入框
                    for entry in angle_entries:
                        entry.delete(0, tk.END)
                    status_bar.config(text="错误：请输入有效的数字")
                    break
    
    # 绑定输入事件
    for entry in angle_entries:
        entry.bind('<KeyRelease>', convert_angles)
    
    # 添加清除按钮
    def clear_angles():
        for entry in angle_entries:
            entry.delete(0, tk.END)
        status_bar.config(text="就绪")
    
    button_frame = tk.Frame(tab4)
    button_frame.grid(row=8, column=0, columnspan=2, pady=15)  # 增加上下边距
    
    clear_angle_btn = tk.Button(button_frame, text="清除", command=clear_angles, **button_style)
    clear_angle_btn.pack(side=tk.LEFT, padx=10)  # 增加左右边距
    
    # 修改提示文本的位置，给它更多空间
    hint_text = tk.Label(tab4, text="提示：在任意字段中输入一个值以立即查看转换", **hint_style)
    hint_text.grid(row=9, column=0, columnspan=2, pady=15)  # 增加了垂直内边距

# 创建角度转换器
create_angle_converter()

# 创建正余弦偏移计算功能
def create_sine_cosine_offset_calculator():
    # 添加标题
    title_frame = create_section_title(tab6, "正余弦偏移计算")
    title_frame.grid(row=0, column=0, columnspan=2, pady=15, sticky='ew')  # 增加上下边距
    
    # 创建输入框架
    input_frame = tk.Frame(tab6, bg=Constants.LIGHT_COLOR)
    input_frame.grid(row=1, column=0, columnspan=2, pady=10)
    
    # 正弦信号输入
    sine_frame = tk.LabelFrame(input_frame, text="正弦信号", bg=Constants.LIGHT_COLOR, font=('微软雅黑', 11))
    sine_frame.grid(row=0, column=0, padx=15, pady=10, sticky='nsew')
    
    tk.Label(sine_frame, text="波峰绝对值:", bg=Constants.LIGHT_COLOR, font=('微软雅黑', 11)).grid(row=0, column=0, **grid_params)
    sine_peak_entry = tk.Entry(sine_frame, **entry_style, takefocus=False,
                             validate='key',
                             validatecommand=(root.register(validate_positive_float), '%P', '%d'))
    sine_peak_entry.grid(row=0, column=1, **grid_params)
    
    tk.Label(sine_frame, text="波谷绝对值:", bg=Constants.LIGHT_COLOR, font=('微软雅黑', 11)).grid(row=1, column=0, **grid_params)
    sine_valley_entry = tk.Entry(sine_frame, **entry_style, takefocus=False,
                               validate='key',
                               validatecommand=(root.register(validate_float), '%P', '%d'))
    sine_valley_entry.grid(row=1, column=1, **grid_params)
    
    # 余弦信号输入
    cosine_frame = tk.LabelFrame(input_frame, text="余弦信号", bg=Constants.LIGHT_COLOR, font=('微软雅黑', 11))
    cosine_frame.grid(row=0, column=1, padx=15, pady=10, sticky='nsew')
    
    tk.Label(cosine_frame, text="波峰绝对值:", bg=Constants.LIGHT_COLOR, font=('微软雅黑', 11)).grid(row=0, column=0, **grid_params)
    cosine_peak_entry = tk.Entry(cosine_frame, **entry_style, takefocus=False,
                               validate='key',
                               validatecommand=(root.register(validate_positive_float), '%P', '%d'))
    cosine_peak_entry.grid(row=0, column=1, **grid_params)
    
    tk.Label(cosine_frame, text="波谷绝对值:", bg=Constants.LIGHT_COLOR, font=('微软雅黑', 11)).grid(row=1, column=0, **grid_params)
    cosine_valley_entry = tk.Entry(cosine_frame, **entry_style, takefocus=False,
                                 validate='key',
                                 validatecommand=(root.register(validate_float), '%P', '%d'))
    cosine_valley_entry.grid(row=1, column=1, **grid_params)
    
    # 结果显示框架
    result_frame = tk.LabelFrame(tab6, text="计算结果", bg=Constants.LIGHT_COLOR, font=('微软雅黑', 11))
    result_frame.grid(row=2, column=0, columnspan=2, padx=15, pady=15, sticky='ew')
    
    # 正弦信号幅值偏移
    tk.Label(result_frame, text="正弦信号幅值偏移值 (PB5):", bg=Constants.LIGHT_COLOR, font=('微软雅黑', 11)).grid(row=0, column=0, **grid_params)
    sine_offset_result = tk.Entry(result_frame, **entry_style, takefocus=False, state='readonly')
    sine_offset_result.grid(row=0, column=1, **grid_params)
    
    # 余弦信号幅值偏移
    tk.Label(result_frame, text="余弦信号幅值偏移值 (PB6):", bg=Constants.LIGHT_COLOR, font=('微软雅黑', 11)).grid(row=1, column=0, **grid_params)
    cosine_offset_result = tk.Entry(result_frame, **entry_style, takefocus=False, state='readonly')
    cosine_offset_result.grid(row=1, column=1, **grid_params)
    
    # 正余弦信号幅值不匹配值
    tk.Label(result_frame, text="正余弦信号幅值不匹配值 (PB7):", bg=Constants.LIGHT_COLOR, font=('微软雅黑', 11)).grid(row=2, column=0, **grid_params)
    mismatch_result = tk.Entry(result_frame, **entry_style, takefocus=False, state='readonly')
    mismatch_result.grid(row=2, column=1, **grid_params)
    
    # 清除结果函数
    def clear_results():
        sine_offset_result.config(state='normal')
        sine_offset_result.delete(0, tk.END)
        sine_offset_result.config(state='readonly')
        
        cosine_offset_result.config(state='normal')
        cosine_offset_result.delete(0, tk.END)
        cosine_offset_result.config(state='readonly')
        
        mismatch_result.config(state='normal')
        mismatch_result.delete(0, tk.END)
        mismatch_result.config(state='readonly')
    
    # 添加输入变化事件绑定
    def on_input_change(event=None):
        clear_results()
    
    # 为所有输入框添加事件绑定
    sine_peak_entry.bind("<KeyRelease>", on_input_change)
    sine_valley_entry.bind("<KeyRelease>", on_input_change)
    cosine_peak_entry.bind("<KeyRelease>", on_input_change)
    cosine_valley_entry.bind("<KeyRelease>", on_input_change)
    
    # 计算函数
    @validate_input
    def calculate_sine_cosine_offset():
        # 获取输入值
        sine_peak = float(sine_peak_entry.get())
        sine_valley = float(sine_valley_entry.get())
        cosine_peak = float(cosine_peak_entry.get())
        cosine_valley = float(cosine_valley_entry.get())
        
        # 验证输入
        if sine_peak <= 0 or cosine_peak <= 0:
            raise ValueError("波峰值必须大于0")
        
        # 计算正弦信号幅值偏移值，使用波谷的绝对值
        sine_offset = (sine_peak - abs(sine_valley)) / 2
        
        # 计算余弦信号幅值偏移值，使用波谷的绝对值
        cosine_offset = (cosine_peak - abs(cosine_valley)) / 2
        
        # 计算正余弦信号幅值不匹配值，使用波谷的绝对值
        mismatch = ((sine_peak + abs(sine_valley)) * 1024) / (cosine_peak + abs(cosine_valley))
        
        # 显示结果
        sine_offset_result.config(state='normal')
        sine_offset_result.delete(0, tk.END)
        sine_offset_result.insert(0, f"{sine_offset:.6f}")
        sine_offset_result.config(state='readonly')
        
        cosine_offset_result.config(state='normal')
        cosine_offset_result.delete(0, tk.END)
        cosine_offset_result.insert(0, f"{cosine_offset:.6f}")
        cosine_offset_result.config(state='readonly')
        
        mismatch_result.config(state='normal')
        mismatch_result.delete(0, tk.END)
        mismatch_result.insert(0, f"{mismatch:.6f}")
        mismatch_result.config(state='readonly')
        
        # 保存计算历史
        save_history("正余弦偏移计算", {
            "正弦波峰绝对值": sine_peak,
            "正弦波谷绝对值": sine_valley,
            "余弦波峰绝对值": cosine_peak,
            "余弦波谷绝对值": cosine_valley
        }, f"正弦偏移:{sine_offset:.6f}, 余弦偏移:{cosine_offset:.6f}, 不匹配值:{mismatch:.6f}")
    
    # 清除函数
    def clear_sine_cosine_fields():
        sine_peak_entry.delete(0, tk.END)
        sine_valley_entry.delete(0, tk.END)
        cosine_peak_entry.delete(0, tk.END)
        cosine_valley_entry.delete(0, tk.END)
        
        sine_offset_result.config(state='normal')
        sine_offset_result.delete(0, tk.END)
        sine_offset_result.config(state='readonly')
        
        cosine_offset_result.config(state='normal')
        cosine_offset_result.delete(0, tk.END)
        cosine_offset_result.config(state='readonly')
        
        mismatch_result.config(state='normal')
        mismatch_result.delete(0, tk.END)
        mismatch_result.config(state='readonly')
        
        status_bar.config(text="就绪")
    
    # 按钮框架
    button_frame = tk.Frame(tab6, bg=Constants.LIGHT_COLOR)
    button_frame.grid(row=3, column=0, columnspan=2, pady=15)
    
    # 计算按钮
    calc_button = tk.Button(button_frame, text="计算", command=calculate_sine_cosine_offset, **button_style)
    calc_button.pack(side=tk.LEFT, padx=10)
    
    # 清除按钮
    clear_button = tk.Button(button_frame, text="清除", command=clear_sine_cosine_fields, **button_style)
    clear_button.pack(side=tk.LEFT, padx=10)
    
    # 提示标签
    hint_label = tk.Label(tab6, text="提示：输入正弦和余弦信号的波峰和波谷绝对值，点击计算按钮获取结果", **hint_style)
    hint_label.grid(row=4, column=0, columnspan=2, pady=10)

# 调用创建正余弦偏移计算器函数
create_sine_cosine_offset_calculator()

# 分数简化功能
def create_fraction_simplifier():
    # 添加标题
    title_frame = create_section_title(tab5, "分数简化")
    title_frame.grid(row=0, column=0, columnspan=2, pady=15, sticky='ew')  # 增加上下边距
    
    # 创建输入框架
    input_frame = tk.Frame(tab5, bg=Constants.LIGHT_COLOR)
    input_frame.grid(row=1, column=0, columnspan=2, pady=15)  # 增加上下边距
    
    # 为分数简化创建特殊的输入框样式
    fraction_entry_style = entry_style.copy()
    fraction_entry_style['width'] = 25
    
    # 分子输入
    numerator_label = tk.Label(input_frame, text="分子:", bg=Constants.LIGHT_COLOR, font=('微软雅黑', 11))
    numerator_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
    numerator_entry = tk.Entry(input_frame, **fraction_entry_style, takefocus=False, 
                               validate='key', 
                               validatecommand=(root.register(validate_integer), '%P', '%d'))
    numerator_entry.grid(row=0, column=1, padx=5, pady=5)
    
    # 分母输入
    denominator_label = tk.Label(input_frame, text="分母:", bg=Constants.LIGHT_COLOR, font=('微软雅黑', 11))
    denominator_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
    denominator_entry = tk.Entry(input_frame, **fraction_entry_style, takefocus=False, 
                                 validate='key', 
                                 validatecommand=(root.register(validate_positive_integer), '%P', '%d'))
    denominator_entry.grid(row=1, column=1, padx=5, pady=5)
    
    # 结果显示框
    result_frame = tk.Frame(tab5, bg=Constants.LIGHT_COLOR)
    result_frame.grid(row=2, column=0, columnspan=2, pady=15)  # 增加上下边距
    
    # 使用可调整大小的Canvas来绘制结果
    result_canvas = tk.Canvas(result_frame, width=600, height=250, bg="white", highlightthickness=1, highlightbackground="#cccccc")
    result_canvas.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    
    # 计算最大公约数的函数
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    # 显示简化过程的函数
    def show_simplification_process(num, denom):
        # 清除画布
        result_canvas.delete("all")
        
        # 计算最大公约数
        common_divisor = gcd(num, denom)
        simplified_num = num // common_divisor
        simplified_denom = denom // common_divisor
        
        # 获取数字的字符串表示
        num_str = str(num)
        denom_str = str(denom)
        simplified_num_str = str(simplified_num)
        simplified_denom_str = str(simplified_denom)
        common_divisor_str = str(common_divisor)
        
        # 计算最长的数字长度
        max_len = max(len(num_str), len(denom_str), 
                      len(simplified_num_str), len(simplified_denom_str),
                      len(common_divisor_str) + len(simplified_num_str) + 3,  # 加3是为了 "×" 和空格
                      len(common_divisor_str) + len(simplified_denom_str) + 3)
        
        # 根据数字长度动态调整画布大小和字体大小
        base_width = 600
        base_height = 250
        base_font_size = 24
        
        # 计算需要的额外宽度 - 更积极的扩展
        extra_width = max(0, (max_len - 8) * 20)  # 每个额外字符增加20像素宽度，从8个字符开始扩展
        canvas_width = base_width + extra_width
        
        # 如果数字过长，减小字体大小，但保持较大的基础大小
        font_size = min(base_font_size, max(12, int(base_font_size * (20 / max(max_len, 1)))))
        
        # 调整画布大小
        result_canvas.config(width=canvas_width, height=base_height)
        
        # 计算分数显示的位置 - 更好的间距
        spacing = canvas_width / 5  # 将画布分为5等份
        first_x = spacing  # 第一个分数的x位置
        second_x = spacing * 2.5  # 第二个分数的x位置
        third_x = spacing * 4  # 第三个分数的x位置
        
        # 垂直位置调整
        y_center = base_height / 2
        y_top = y_center - 40
        y_bottom = y_center + 40
        y_line = y_center
        
        # 计算分数线的长度（根据数字长度）
        line_length_factor = 0.85  # 线长为数字长度的倍数，增加一点
        first_line_len = max(len(num_str), len(denom_str)) * font_size * 0.6 * line_length_factor
        second_line_len = max(len(simplified_num_str) + len(common_divisor_str) + 3, 
                             len(simplified_denom_str) + len(common_divisor_str) + 3) * font_size * 0.6 * line_length_factor
        third_line_len = max(len(simplified_num_str), len(simplified_denom_str)) * font_size * 0.6 * line_length_factor
        
        # 确保线长至少有最小值
        min_line_len = font_size * 2
        first_line_len = max(first_line_len, min_line_len)
        second_line_len = max(second_line_len, min_line_len)
        third_line_len = max(third_line_len, min_line_len)
        
        # 绘制原始分数
        result_canvas.create_text(first_x, y_top, text=num_str, font=('Consolas', font_size, 'bold'))
        result_canvas.create_line(first_x - first_line_len/2, y_line, first_x + first_line_len/2, y_line, width=2)
        result_canvas.create_text(first_x, y_bottom, text=denom_str, font=('Consolas', font_size, 'bold'))
        
        # 绘制等号
        result_canvas.create_text(spacing * 1.75, y_line, text="=", font=('Consolas', font_size))
        
        # 绘制计算过程
        if common_divisor > 1:
            # 绘制带公因数的分数
            result_canvas.create_text(second_x, y_top, text=f"{simplified_num_str} × {common_divisor_str}", 
                                     font=('Consolas', max(12, font_size-4)), fill="red")
            result_canvas.create_line(second_x - second_line_len/2, y_line, second_x + second_line_len/2, y_line, width=2)
            result_canvas.create_text(second_x, y_bottom, text=f"{simplified_denom_str} × {common_divisor_str}", 
                                     font=('Consolas', max(12, font_size-4)), fill="red")
            
            # 绘制第二个等号
            result_canvas.create_text(spacing * 3.25, y_line, text="=", font=('Consolas', font_size))
            
            # 绘制最终简化结果
            result_canvas.create_text(third_x, y_top, text=simplified_num_str, font=('Consolas', font_size, 'bold'))
            result_canvas.create_line(third_x - third_line_len/2, y_line, third_x + third_line_len/2, y_line, width=2)
            result_canvas.create_text(third_x, y_bottom, text=simplified_denom_str, font=('Consolas', font_size, 'bold'))
        else:
            # 如果已经是最简形式，直接显示结果
            result_canvas.create_text(second_x, y_top, text=simplified_num_str, font=('Consolas', font_size, 'bold'))
            result_canvas.create_line(second_x - third_line_len/2, y_line, second_x + third_line_len/2, y_line, width=2)
            result_canvas.create_text(second_x, y_bottom, text=simplified_denom_str, font=('Consolas', font_size, 'bold'))
        
        # 保存计算历史
        save_history("分数简化", {
            "分子": num,
            "分母": denom
        }, f"{simplified_num}/{simplified_denom}")
    
    # 简化分数的函数
    def simplify_fraction():
        try:
            numerator = int(numerator_entry.get())
            denominator = int(denominator_entry.get())
            
            if denominator == 0:
                raise ValueError("分母不能为零")
            
            show_simplification_process(abs(numerator), abs(denominator))
            
            # 更新状态栏
            status_bar.config(text="分数简化完成")
        except ValueError as e:
            if str(e) == "分母不能为零":
                messagebox.showerror("输入错误", "分母不能为零")
            else:
                messagebox.showerror("输入错误", "请输入有效的整数")
            status_bar.config(text="错误：请检查输入")
    
    # 清除输入的函数
    def clear_fraction():
        numerator_entry.delete(0, tk.END)
        denominator_entry.delete(0, tk.END)
        result_canvas.delete("all")
        status_bar.config(text="就绪")
    
    # 添加按钮
    button_frame = tk.Frame(tab5, bg=Constants.LIGHT_COLOR)
    button_frame.grid(row=3, column=0, columnspan=2, pady=15)  # 增加上下边距
    
    simplify_button = tk.Button(button_frame, text="简化分数", command=simplify_fraction, **button_style)
    simplify_button.pack(side=tk.LEFT, padx=10)  # 增加左右边距
    
    clear_button = tk.Button(button_frame, text="清除", command=clear_fraction, **button_style)
    clear_button.pack(side=tk.LEFT, padx=10)  # 增加左右边距
    
    # 提示信息
    hint_label = tk.Label(tab5, text="提示：输入分子和分母，点击简化分数查看结果", **hint_style)
    hint_label.grid(row=4, column=0, columnspan=2, pady=15)  # 增加上下边距

# 调用创建分数简化器函数
create_fraction_simplifier()

# 添加工具提示类
class ToolTip(object):
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind('<Enter>', self.enter)
        self.widget.bind('<Leave>', self.leave)

    def enter(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        
        self.tooltip = tk.Toplevel()
        self.tooltip.wm_overrideredirect(True)  # 移除窗口边框
        self.tooltip.wm_geometry(f"+{x}+{y}")
        
        label = tk.Label(self.tooltip, text=self.text, 
                      justify=tk.LEFT,
                      background=Constants.LIGHT_COLOR,
                      foreground=Constants.TEXT_COLOR,
                      relief='solid', borderwidth=1,
                      font=("微软雅黑", 11),  # 增加工具提示字体大小
                      padx=8, pady=6)  # 增加工具提示内边距
        label.pack()
    
    def leave(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

# 修改标签页1的界面
title_frame = create_section_title(tab1, "常规参数计算")
title_frame.grid(row=0, column=0, columnspan=2, pady=15, sticky='ew')  # 增加上下边距

# 常规计算界面
tk.Label(tab1, text="加减速时间常数 (ms):", font=('微软雅黑', 11)).grid(row=1, column=0, **grid_params)
acc_entry = tk.Entry(tab1, **entry_style, takefocus=False, 
                    validate='key', 
                    validatecommand=(root.register(validate_positive_float), '%P', '%d'))
acc_entry.grid(row=1, column=1, **grid_params)

tk.Label(tab1, text="加速度 (g):", font=('微软雅黑', 11)).grid(row=2, column=0, **grid_params)
acc_g_result_entry = tk.Entry(tab1, **entry_style, takefocus=False,
                             validate='key',
                             validatecommand=(root.register(validate_positive_float), '%P', '%d'))
acc_g_result_entry.grid(row=2, column=1, **grid_params)

tk.Label(tab1, text="捷度时间常数 (ms):", font=('微软雅黑', 11)).grid(row=3, column=0, **grid_params)
jerk_entry = tk.Entry(tab1, **entry_style, takefocus=False,
                     validate='key',
                     validatecommand=(root.register(validate_positive_float), '%P', '%d'))
jerk_entry.grid(row=3, column=1, **grid_params)

# 按钮框架
button_frame = tk.Frame(tab1)
button_frame.grid(row=4, column=0, columnspan=2, pady=15)  # 增加上下边距

# 计算按钮
calc_button = tk.Button(button_frame, text="计算", command=calculate_acceleration, **button_style)
calc_button.pack(side=tk.LEFT, padx=10)  # 增加左右边距

# 清除按钮
clear_button = tk.Button(button_frame, text="清除", command=clear_acc_fields, **button_style)
clear_button.pack(side=tk.LEFT, padx=10)  # 增加左右边距

# 提示标签
hint_label = tk.Label(tab1, text="提示：时间常数和加速度填写其中一个即可互相计算", **hint_style)
hint_label.grid(row=5, column=0, columnspan=2, pady=10)  # 增加上下边距

# G00计算页面添加标题
title_frame_g00 = create_section_title(tab2, "G00参数计算")
title_frame_g00.grid(row=0, column=0, columnspan=2, pady=15, sticky='ew')  # 增加上下边距

tk.Label(tab2, text="理论快移速度 (m/min):", font=('微软雅黑', 11)).grid(row=1, column=0, **grid_params)
speed_entry = tk.Entry(tab2, **entry_style, takefocus=False,
                      validate='key',
                      validatecommand=(root.register(validate_positive_float), '%P', '%d'))
speed_entry.grid(row=1, column=1, **grid_params)

tk.Label(tab2, text="理论加速度 (g):", font=('微软雅黑', 11)).grid(row=2, column=0, **grid_params)
acc_g_entry = tk.Entry(tab2, **entry_style, takefocus=False,
                      validate='key',
                      validatecommand=(root.register(validate_positive_float), '%P', '%d'))
acc_g_entry.grid(row=2, column=1, **grid_params)

tk.Label(tab2, text="216号参数值 (ms):", font=('微软雅黑', 11)).grid(row=3, column=0, **grid_params)
param216_entry = tk.Entry(tab2, **entry_style, takefocus=False,
                         validate='key',
                         validatecommand=(root.register(validate_positive_float), '%P', '%d'))
param216_entry.grid(row=3, column=1, **grid_params)

# 按钮框架
g00_button_frame = tk.Frame(tab2)
g00_button_frame.grid(row=4, column=0, columnspan=2, pady=15)  # 增加上下边距

# 计算按钮
calc_g00_btn = tk.Button(g00_button_frame, text="计算", command=calculate_g00, **button_style)
calc_g00_btn.pack(side=tk.LEFT, padx=10)  # 增加左右边距

# 清除按钮
clear_g00_btn = tk.Button(g00_button_frame, text="清除", command=clear_g00_fields, **button_style)
clear_g00_btn.pack(side=tk.LEFT, padx=10)  # 增加左右边距

# 提示标签
g00_hint_label = tk.Label(tab2, text="提示：快移速度必填，加速度和参数值填写其中一个即可互相计算", 
                         **hint_style)  # 使用统一的提示样式
g00_hint_label.grid(row=5, column=0, columnspan=2, pady=10)  # 增加上下边距

# 导入并创建登奇电机选型计算器
from dengqi_motor_calculator import create_dengqi_motor_calculator
create_dengqi_motor_calculator(notebook, root, create_section_title, grid_params, entry_style, button_style, hint_style, validate_positive_float, save_history, ToolTip, tk, ttk, messagebox, style)

# 导入并创建主轴定向脉冲计算器
from spindle_orientation_calculator import create_spindle_orientation_calculator
create_spindle_orientation_calculator(notebook, root, create_section_title, grid_params, entry_style, button_style, hint_style, validate_positive_float, validate_float, save_history, ToolTip, tk, ttk, messagebox, style)

root.mainloop()