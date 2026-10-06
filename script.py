import os
import pandas as pd
from datetime import datetime
from pytrends.request import TrendReq

# =================================================================
# 1. NHẬP CHỦ ĐỀ VÀ TỪ KHÓA BẠN CẦN THEO DÕI TẠI ĐÂY
# Bạn có thể nhập tối đa 5 từ khóa, cách nhau bằng dấu phẩy
# Ví dụ: KEYWORDS = ['iphone', 'samsung', 'xiaomi']
# =================================================================
KEYWORDS = ['bitcoin', 'crypto', 'ethereum'] 

# 2. CẤU HÌNH PHẠM VI DỮ LIỆU
GEO = 'VN'          # 'VN' là Việt Nam (để trống '' nếu muốn lấy toàn cầu)
TIMEFRAME = 'now 7-d' # 'now 7-d' là lấy dữ liệu 7 ngày qua (hoặc 'today 3m', 'today 12m')

def get_topic_trends():
    try:
        # Khởi tạo pytrends
        pytrends = TrendReq(hl='vi-VN', tz=420)
        
        # Gửi yêu cầu lấy dữ liệu theo từ khóa
        pytrends.build_payload(KEYWORDS, cat=0, timeframe=TIMEFRAME, geo=GEO, gprop='')
        
        # Lấy dữ liệu mức độ quan tâm theo thời gian (thang điểm 0 - 100)
        df = pytrends.interest_over_time()
        
        if df.empty:
            print("Không tìm thấy dữ liệu cho các từ khóa này.")
            return
            
        # Xóa cột 'isPartial' không cần thiết của Google Trends
        if 'isPartial' in df.columns:
            df = df.drop(columns=['isPartial'])
            
        # Chuyển cột index (Thời gian) thành một cột dữ liệu bình thường
        df = df.reset_index()
        
        # Đổi tên file lưu theo tháng để quản lý (Ví dụ: keyword_trends_2026_10.csv)
        file_name = f"keyword_trends_{datetime.now().strftime('%Y_%m')}.csv"
        
        # Ghi file mới hoặc đè lên file cũ nếu cùng tháng
        df.to_csv(file_name, index=False, encoding='utf-8-sig')
        print(f"Thành công! Dữ liệu từ khóa đã được lưu vào file {file_name}")
        
    except Exception as e:
        print(f"Lỗi khi lấy dữ liệu: {e}")

if __name__ == "__main__":
    get_topic_trends()
