import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel('dataset/dulieu.xlsx', header=[0, 1])
df.columns = [col[1] if col[1] != '' else col[0] for col in df.columns]
df_plot = df[df['Dữ liệu'] != 'Trung bình'].copy()
df_melted = df_plot.melt(
    id_vars='Dữ liệu',
    var_name='Thuật toán',
    value_name='Thời gian (ms)'
)
plt.figure(figsize=(18, 6))
sns.set_theme(style="whitegrid")
ax = sns.barplot(data=df_melted, x='Dữ liệu', y='Thời gian (ms)', hue='Thuật toán', width = 0.6)

plt.show()
