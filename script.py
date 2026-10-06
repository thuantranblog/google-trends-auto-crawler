import os
import pandas as pd
from datetime import datetime
from pytrends.request import TrendReq

def get_trends():
    try:
        # Khởi tạo pytrends với ngôn ngữ/múi giờ VN
        pytrends = TrendReq(hl='vi-VN', tz=420)
        
        # Lấy xu hướng hàng ngày tại Việt Nam
        df = pytrends.trending_searches(pn='vietnam')
        df.columns = ['Từ khóa thịnh hành']
        
        # Thêm thời gian cập nhật (múi giờ GMT+7)
        df['Thời gian cập nhật'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Tên file lưu theo tháng để tránh file quá nặng (Ví dụ: trends_2026_10.csv)
        file_name = f"trends_{datetime.now().strftime('%Y_%m')}.csv"
        
        # Ghi đè hoặc thêm tiếp vào file cũ
        if os.path.exists(file_name):
            df.to_csv(file_name, mode='a', header=False, index=False, encoding='utf-8-sig')
        else:
            df.to_csv(file_name, index=False, encoding='utf-8-sig')
            
        print(f"Thành công! Dữ liệu đã được ghi vào file {file_name}")
    except Exception as e:
        print(f"Lỗi khi lấy dữ liệu: {e}")

if __name__ == "__main__":
    get_trends()
