"""
登奇电机选型计算功能模块
"""

def create_dengqi_motor_calculator(notebook, root, create_section_title, grid_params, entry_style, button_style, hint_style, validate_positive_float, save_history, ToolTip, tk, ttk, messagebox, style):
    """创建登奇电机选型计算功能界面"""
    # 创建标签页
    tab_dengqi = ttk.Frame(notebook, padding=10)
    notebook.add(tab_dengqi, text="登奇电机选型")
    
    # 添加标题
    title_frame = create_section_title(tab_dengqi, "登奇电机选型计算")
    title_frame.grid(row=0, column=0, columnspan=2, pady=15, sticky='ew')
    
    # 创建输入框和标签
    # 轴名称
    tk.Label(tab_dengqi, text="轴名称:", font=('微软雅黑', 11)).grid(row=1, column=0, **grid_params)
    axis_name_entry = tk.Entry(tab_dengqi, **entry_style, takefocus=False)
    axis_name_entry.grid(row=1, column=1, **grid_params)
    
    # 电机型号
    tk.Label(tab_dengqi, text="电机型号:", font=('微软雅黑', 11)).grid(row=2, column=0, **grid_params)
    motor_model_entry = tk.Entry(tab_dengqi, **entry_style, takefocus=False)
    motor_model_entry.grid(row=2, column=1, **grid_params)
    
    # 额定转速选择
    tk.Label(tab_dengqi, text="额定转速 (rpm):", font=('微软雅黑', 11)).grid(row=3, column=0, **grid_params)
    rated_speed_var = tk.StringVar(value="3000")
    rated_speed_combo = ttk.Combobox(tab_dengqi, textvariable=rated_speed_var, 
                                    values=["3000", "2000", "1500"], 
                                    width=13, 
                                    state="readonly")
    rated_speed_combo.grid(row=3, column=1, **grid_params)
    
    # 显示对应的额定扭矩电流系数
    tk.Label(tab_dengqi, text="额定扭矩电流系数:", font=('微软雅黑', 11)).grid(row=4, column=0, **grid_params)
    torque_current_coef_var = tk.StringVar(value="0.7")
    torque_current_coef_entry = tk.Entry(tab_dengqi, textvariable=torque_current_coef_var, 
                                        **entry_style, takefocus=False, state="readonly")
    torque_current_coef_entry.grid(row=4, column=1, **grid_params)
    
    # 静扭矩
    tk.Label(tab_dengqi, text="静扭矩 (Nm):", font=('微软雅黑', 11)).grid(row=5, column=0, **grid_params)
    static_torque_entry = tk.Entry(tab_dengqi, **entry_style, takefocus=False,
                                 validate='key',
                                 validatecommand=(root.register(validate_positive_float), '%P', '%d'))
    static_torque_entry.grid(row=5, column=1, **grid_params)
    
    # 线电流
    tk.Label(tab_dengqi, text="线电流 (A):", font=('微软雅黑', 11)).grid(row=6, column=0, **grid_params)
    line_current_entry = tk.Entry(tab_dengqi, **entry_style, takefocus=False,
                                validate='key',
                                validatecommand=(root.register(validate_positive_float), '%P', '%d'))
    line_current_entry.grid(row=6, column=1, **grid_params)
    
    # 功率系数（固定值）
    tk.Label(tab_dengqi, text="功率系数:", font=('微软雅黑', 11)).grid(row=7, column=0, **grid_params)
    power_coef_var = tk.StringVar(value="9550")
    power_coef_entry = tk.Entry(tab_dengqi, textvariable=power_coef_var, 
                              **entry_style, takefocus=False, state="readonly")
    power_coef_entry.grid(row=7, column=1, **grid_params)
    
    # 计算结果显示区域
    result_frame = ttk.LabelFrame(tab_dengqi, text="计算结果", padding=(10, 5))
    result_frame.grid(row=8, column=0, columnspan=2, pady=15, sticky='ew')
    
    # 设置结果框架的样式
    style.configure('ResultFrame.TLabelframe', background='#F4F3F9')
    style.configure('ResultFrame.TLabelframe.Label', background='#F4F3F9')
    result_frame.configure(style='ResultFrame.TLabelframe')
    
    # 额定扭矩
    tk.Label(result_frame, text="额定扭矩 (Nm):", font=('微软雅黑', 11)).grid(row=0, column=0, **grid_params)
    rated_torque_var = tk.StringVar()
    rated_torque_entry = tk.Entry(result_frame, textvariable=rated_torque_var, 
                                **entry_style, takefocus=False, state="readonly")
    rated_torque_entry.grid(row=0, column=1, **grid_params)
    
    # 额定电流
    tk.Label(result_frame, text="额定电流 (A):", font=('微软雅黑', 11)).grid(row=1, column=0, **grid_params)
    rated_current_var = tk.StringVar()
    rated_current_entry = tk.Entry(result_frame, textvariable=rated_current_var, 
                                 **entry_style, takefocus=False, state="readonly")
    rated_current_entry.grid(row=1, column=1, **grid_params)
    
    # 额定功率
    tk.Label(result_frame, text="额定功率 (kW):", font=('微软雅黑', 11)).grid(row=2, column=0, **grid_params)
    rated_power_var = tk.StringVar()
    rated_power_entry = tk.Entry(result_frame, textvariable=rated_power_var, 
                               **entry_style, takefocus=False, state="readonly")
    rated_power_entry.grid(row=2, column=1, **grid_params)
    
    # 更新额定扭矩电流系数的函数
    def update_torque_current_coefficient(*args):
        speed = rated_speed_var.get()
        if speed == "3000":
            torque_current_coef_var.set("0.7")
        elif speed == "2000":
            torque_current_coef_var.set("0.8")
        elif speed == "1500":
            torque_current_coef_var.set("0.85")
    
    # 绑定下拉框选择事件
    rated_speed_var.trace_add("write", update_torque_current_coefficient)
    
    # 清空输入和结果的函数
    def clear_dengqi_fields():
        axis_name_entry.delete(0, tk.END)
        motor_model_entry.delete(0, tk.END)
        rated_speed_var.set("3000")
        static_torque_entry.delete(0, tk.END)
        line_current_entry.delete(0, tk.END)
        rated_torque_var.set("")
        rated_current_var.set("")
        rated_power_var.set("")
    
    # 计算函数
    def calculate_dengqi_motor():
        try:
            # 获取输入值
            static_torque_str = static_torque_entry.get().strip()
            line_current_str = line_current_entry.get().strip()
            
            # 验证输入
            if not static_torque_str or not line_current_str:
                messagebox.showwarning("输入错误", "请输入静扭矩和线电流值")
                return
            
            # 转换为浮点数
            static_torque = float(static_torque_str)
            line_current = float(line_current_str)
            rated_speed = float(rated_speed_var.get())
            torque_current_coef = float(torque_current_coef_var.get())
            power_coef = float(power_coef_var.get())
            
            # 计算结果
            # 额定扭矩 = 静扭矩 * 额定扭矩电流系数
            rated_torque = static_torque * torque_current_coef
            
            # 额定电流 = 线电流 * 额定扭矩电流系数
            rated_current = line_current * torque_current_coef
            
            # 额定功率 = 额定转速 * 额定扭矩 / 9550
            rated_power = rated_speed * rated_torque / power_coef
            
            # 显示结果，保留3位小数
            rated_torque_var.set(f"{rated_torque:.3f}")
            rated_current_var.set(f"{rated_current:.3f}")
            rated_power_var.set(f"{rated_power:.3f}")
            
            # 保存到历史记录
            params = {
                "轴名称": axis_name_entry.get(),
                "电机型号": motor_model_entry.get(),
                "额定转速": rated_speed_var.get(),
                "额定扭矩电流系数": torque_current_coef_var.get(),
                "静扭矩": static_torque_str,
                "线电流": line_current_str
            }
            save_history("登奇电机选型计算", params, rated_power)
            
        except ValueError as e:
            messagebox.showerror("计算错误", f"计算过程中出现错误: {str(e)}")
    
    # 按钮框架
    button_frame = tk.Frame(tab_dengqi)
    button_frame.grid(row=9, column=0, columnspan=2, pady=15)
    
    # 计算按钮
    calc_button = tk.Button(button_frame, text="计算", command=calculate_dengqi_motor, **button_style)
    calc_button.pack(side=tk.LEFT, padx=10)
    
    # 清除按钮
    clear_button = tk.Button(button_frame, text="清除", command=clear_dengqi_fields, **button_style)
    clear_button.pack(side=tk.LEFT, padx=10)
    
    # 提示标签
    hint_label = tk.Label(tab_dengqi, text="提示：请输入静扭矩和线电流，选择额定转速后计算", **hint_style)
    hint_label.grid(row=10, column=0, columnspan=2, pady=10)
    
    # 添加工具提示
    ToolTip(static_torque_entry, "输入电机静扭矩，单位为牛米(Nm)")
    ToolTip(line_current_entry, "输入电机线电流，单位为安培(A)")
    ToolTip(rated_speed_combo, "选择电机额定转速，单位为转/分钟(rpm)")
    ToolTip(torque_current_coef_entry, "根据额定转速自动匹配的额定扭矩电流系数")
    ToolTip(power_coef_entry, "固定的功率系数：9550")
