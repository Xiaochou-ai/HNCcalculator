"""
主轴定向脉冲计算功能模块
"""

def create_spindle_orientation_calculator(notebook, root, create_section_title, grid_params, entry_style, button_style, hint_style, validate_positive_float, validate_float, save_history, ToolTip, tk, ttk, messagebox, style):
    """创建主轴定向脉冲计算功能界面"""
    # 创建标签页
    tab_spindle = ttk.Frame(notebook, padding=10)
    notebook.add(tab_spindle, text="主轴定向脉冲")
    
    # 添加标题
    title_frame = create_section_title(tab_spindle, "主轴定向脉冲计算")
    title_frame.grid(row=0, column=0, columnspan=2, pady=15, sticky='ew')
    
    # 创建输入框和标签
    # 主轴脉冲
    tk.Label(tab_spindle, text="主轴脉冲:", font=('微软雅黑', 11)).grid(row=1, column=0, **grid_params)
    spindle_pulse_entry = tk.Entry(tab_spindle, **entry_style, takefocus=False,
                                 validate='key',
                                 validatecommand=(root.register(validate_positive_float), '%P', '%d'))
    spindle_pulse_entry.grid(row=1, column=1, **grid_params)
    
    # 期望定向位置
    tk.Label(tab_spindle, text="期望定向位置:", font=('微软雅黑', 11)).grid(row=2, column=0, **grid_params)
    desired_position_entry = tk.Entry(tab_spindle, **entry_style, takefocus=False,
                                    validate='key',
                                    validatecommand=(root.register(validate_float), '%P', '%d'))
    desired_position_entry.grid(row=2, column=1, **grid_params)
    
    # 计算结果显示区域
    result_frame = ttk.LabelFrame(tab_spindle, text="计算结果", padding=(10, 5))
    result_frame.grid(row=3, column=0, columnspan=2, pady=15, sticky='ew')
    
    # 设置结果框架的样式
    style.configure('ResultFrame.TLabelframe', background='#F4F3F9')
    style.configure('ResultFrame.TLabelframe.Label', background='#F4F3F9')
    result_frame.configure(style='ResultFrame.TLabelframe')
    
    # 第一档主轴定向起始偏移角度PA48
    tk.Label(result_frame, text="第一档主轴定向起始偏移角度PA48:", font=('微软雅黑', 11)).grid(row=0, column=0, **grid_params)
    pa48_var = tk.StringVar()
    pa48_entry = tk.Entry(result_frame, textvariable=pa48_var, 
                        **entry_style, takefocus=False, state="readonly")
    pa48_entry.grid(row=0, column=1, **grid_params)
    
    # 第一档主轴定向位置PA39
    tk.Label(result_frame, text="第一档主轴定向位置PA39:", font=('微软雅黑', 11)).grid(row=1, column=0, **grid_params)
    pa39_var = tk.StringVar()
    pa39_entry = tk.Entry(result_frame, textvariable=pa39_var, 
                        **entry_style, takefocus=False, state="readonly")
    pa39_entry.grid(row=1, column=1, **grid_params)
    
    # 清空输入和结果的函数
    def clear_spindle_fields():
        spindle_pulse_entry.delete(0, tk.END)
        desired_position_entry.delete(0, tk.END)
        pa48_var.set("")
        pa39_var.set("")
    
    # 计算函数
    def calculate_spindle_orientation():
        try:
            # 获取输入值
            spindle_pulse_str = spindle_pulse_entry.get().strip()
            desired_position_str = desired_position_entry.get().strip()
            
            # 验证输入
            if not spindle_pulse_str or not desired_position_str:
                messagebox.showwarning("输入错误", "请输入主轴脉冲和期望定向位置")
                return
            
            # 转换为浮点数
            spindle_pulse = float(spindle_pulse_str)
            desired_position = float(desired_position_str)
            
            # 验证主轴脉冲必须大于0
            if spindle_pulse <= 0:
                messagebox.showwarning("输入错误", "主轴脉冲必须大于0")
                return
            
            # 计算结果
            # 第一档主轴定向起始偏移角度PA48=(期望定向位置*18)/主轴脉冲 (向下取整)
            pa48 = int((desired_position * 18) / spindle_pulse)  # 使用int()向下取整
            
            # 第一档主轴定向位置PA39=期望定向位置-(第一档主轴定向起始偏移角度PA48*(主轴脉冲/18)) (四舍五入)
            pa39 = round(desired_position - (pa48 * (spindle_pulse / 18)))
            
            # 显示结果
            pa48_var.set(str(pa48))
            pa39_var.set(str(pa39))
            
            # 保存到历史记录
            params = {
                "主轴脉冲": spindle_pulse_str,
                "期望定向位置": desired_position_str
            }
            save_history("主轴定向脉冲计算", params, pa39)
            
        except ValueError as e:
            messagebox.showerror("计算错误", f"计算过程中出现错误: {str(e)}")
    
    # 按钮框架
    button_frame = tk.Frame(tab_spindle)
    button_frame.grid(row=4, column=0, columnspan=2, pady=15)
    
    # 计算按钮
    calc_button = tk.Button(button_frame, text="计算", command=calculate_spindle_orientation, **button_style)
    calc_button.pack(side=tk.LEFT, padx=10)
    
    # 清除按钮
    clear_button = tk.Button(button_frame, text="清除", command=clear_spindle_fields, **button_style)
    clear_button.pack(side=tk.LEFT, padx=10)
    
    # 提示标签
    hint_label = tk.Label(tab_spindle, text="提示：PA48计算结果向下取整，PA39计算结果四舍五入", **hint_style)
    hint_label.grid(row=5, column=0, columnspan=2, pady=10)
    
    # 添加工具提示
    ToolTip(spindle_pulse_entry, "输入主轴脉冲数值，必须大于0")
    ToolTip(desired_position_entry, "输入期望的定向位置")
    ToolTip(pa48_entry, "第一档主轴定向起始偏移角度PA48=(期望定向位置*18)/主轴脉冲，结果向下取整")
    ToolTip(pa39_entry, "第一档主轴定向位置PA39=期望定向位置-(PA48*(主轴脉冲/18))，结果四舍五入")
