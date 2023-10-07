# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 23:17:23 2023

@author: wytheY
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def two_decimal(x, pos):
    return '{:.2f}'.format(x)

formatter = FuncFormatter(two_decimal)

# 设置matplotlib的字体参数
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

file_path = r'C:\\Users\\wytheY\\Desktop\\华证指数笔试题\\9988.HK-财务摘要(单季).csv'
df = pd.read_csv(file_path, encoding='gbk')

# 提取需要的数据
dates = df.columns[2:]

# 移除逗号并转换为数字
revenue = pd.to_numeric(df.iloc[4, 2:].str.replace(',', ''), errors='coerce')
net_profit = pd.to_numeric(df.iloc[8, 2:].str.replace(',', ''), errors='coerce')
roe = pd.to_numeric(df.iloc[21, 2:].str.replace(',', ''), errors='coerce')
roa = pd.to_numeric(df.iloc[22, 2:].str.replace(',', ''), errors='coerce')

revenue_growth = pd.to_numeric(df.iloc[10, 2:].str.replace('%', ''), errors='coerce')
net_profit_growth = pd.to_numeric(df.iloc[18, 2:].str.replace('%', ''), errors='coerce')
operating_profit = pd.to_numeric(df.iloc[13, 2:].str.replace(',', ''), errors='coerce')


# 设置全局字体大小
plt.rcParams.update({'font.size': 10})

# 绘制营业总收入和净利润同比增长率的折线图（成长性分析）
plt.figure(figsize=(12, 7))
plt.plot(dates, revenue_growth, label='营业总收入同比增长率', color='blue', linestyle='-', marker='o')
plt.plot(dates, net_profit_growth, label='净利润同比增长率', color='green', linestyle='--', marker='x')
plt.xlabel('日期')
plt.ylabel('增长率 (%)')
plt.title('营业总收入和净利润同比增长率(成长性分析)')

plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 绘制营业总收入和净利润的折线图
plt.figure(figsize=(12, 7))
plt.plot(dates, revenue, label='营业总收入', color='blue', linestyle='-', marker='o')
plt.plot(dates, net_profit, label='净利润', color='green', linestyle='--', marker='x')
plt.xlabel('日期')
plt.ylabel('金额 (万元)')
plt.title('营业总收入和净利润变化趋势(盈利能力分析)')

plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 绘制ROE和ROA的折线图
plt.figure(figsize=(12, 7))
plt.plot(dates, roe, label='ROE', color='red', linestyle='-', marker='o')
plt.plot(dates, roa, label='ROA', color='purple', linestyle='--', marker='x')
plt.xlabel('日期')
plt.ylabel('百分比 (%)')
plt.title('ROE和ROA变化趋势(盈利能力分析)')

plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 绘制P/E和P/B的折线图
pe = pd.to_numeric(df.iloc[29, 2:].str.replace(',', ''), errors='coerce')
pb = pd.to_numeric(df.iloc[30, 2:].str.replace(',', ''), errors='coerce')

plt.figure(figsize=(12, 7))
plt.plot(dates, pe, label='P/E', color='orange', linestyle='-', marker='o')
plt.plot(dates, pb, label='P/B', color='brown', linestyle='--', marker='x')
plt.xlabel('日期')
plt.ylabel('比率')
plt.title('P/E和P/B变化趋势(估值分析)')

ax = plt.gca()
ax.yaxis.set_major_formatter(formatter)

plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
