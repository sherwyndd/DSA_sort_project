# Sorting Algorithm Performance Comparison

Dự án này thực hiện so sánh hiệu năng thực tế của các thuật toán sắp xếp phổ biến (Quicksort, Mergesort, Heapsort) và so sánh với thư viện tối ưu hóa `numpy.sort`.

## 📌 Tính năng
- Cài đặt các thuật toán sắp xếp cơ bản bằng Python.
- Script đo thời gian thực thi chính xác cho từng bộ dữ liệu.
- Dựng biểu đồ trực quan từ file csv (Seaborn/Matplotlib).

## 📊 Kết quả thực nghiệm (ms)
Dưới đây là bảng tóm tắt thời gian chạy trung bình trên 10 bộ dữ liệu:

| Thuật toán | Thời gian TB (ms) |
| :--- | :---: |
| **Quicksort** | 740 |
| **Mergesort** | 2983 |
| **Heapsort** | 1538 |
| **Numpy Sort** | 38 |

## 📁 Cấu trúc dữ liệu đầu vào
Vì các file dữ liệu thử nghiệm (`test_1.txt` đến `test_10.txt`) có dung lượng lớn nên không được upload trực tiếp lên repository này. 

**Để chạy thử nghiệm, vui lòng sử dụng script sinh dữ liệu:**
1. Chạy file `gen_test.py` để tạo các file test mẫu.
2. Script sẽ tự động sinh ra các dãy số thực ngẫu nhiên với kích thước n cố định là 1e6 và giá trị trong khoảng [-1e9, 1e9].
