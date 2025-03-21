"""
将图像转换为ICO图标文件
"""
import os
import sys
from PIL import Image

def convert_image_to_ico(image_path, ico_path):
    try:
        # 检查文件是否存在
        if not os.path.exists(image_path):
            print(f"错误: 找不到文件 {image_path}")
            return False
            
        # 打开图像
        img = Image.open(image_path)
        
        # 定义图标尺寸
        icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        
        # 保存为ICO
        img.save(ico_path, format='ICO', sizes=icon_sizes)
        
        print(f"成功: 已将 {image_path} 转换为图标 {ico_path}")
        return True
    except Exception as e:
        print(f"错误: {str(e)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 2:
        image_path = sys.argv[1]
        ico_path = sys.argv[2]
    else:
        image_path = "xiaoai.jpg"
        ico_path = "logo.ico"
    
    success = convert_image_to_ico(image_path, ico_path)
    if not success:
        sys.exit(1)
