import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Đọc file Excel 
# Do file có 2 dòng tiêu đề (Dòng 1: Thời gian thực hiện, Dòng 2: Tên thuật toán)
# Chúng ta sẽ đọc từ dòng thứ 2 (header=[0, 1]) để lấy cả 2 tầng tiêu đề
df = pd.read_excel('dulieu.xlsx', header=[0, 1])

# 2. Xử lý dữ liệu
# Loại bỏ dòng 'Trung bình' để biểu đồ không bị lệch tỉ lệ
df_plot = df[df.iloc[:, 0] != 'Trung bình'].copy()

# Chuyển đổi dữ liệu từ dạng rộng (Wide) sang dạng dài (Long) để Seaborn dễ vẽ
# Chúng ta sẽ giữ cột 'Dữ liệu' và gom các cột thuật toán lại
df_melted = df_plot.melt(id_vars=df.columns[0], 
                         value_vars=df.columns[1:], 
                         var_name=['Header', 'Thuật toán'], 
                         value_name='Thời gian (ms)')

# 3. Vẽ biểu đồ với Seaborn
plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")

# Vẽ biểu đồ cột nhóm (Grouped Bar Chart)
ax = sns.barplot(data=df_melted, 
                 x=df.columns[0], 
                 y='Thời gian (ms)', 
                 hue='Thuật toán', 
                 palette="muted")

# 4. Tùy chỉnh hiển thị
plt.title("So sánh thời gian thực hiện các thuật toán sắp xếp", fontsize=15, fontweight='bold')
plt.xlabel("Bộ dữ liệu (Test Case)", fontsize=12)
plt.ylabel("Thời gian (ms)", fontsize=12)

# Sử dụng thang đo Log nếu bạn muốn nhìn rõ cột 'sort (numpy)' 
# ax.set_yscale("log") 

# Thêm giá trị lên đầu mỗi cột (tùy chọn)
for container in ax.containers:
    ax.bar_label(container, padding=3, fontsize=8)

plt.tight_layout()
plt.show()