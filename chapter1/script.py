import pandas as pd
import matplotlib.pyplot as plt

# データを読み込む
customer_master = pd.read_csv('customer_master.csv')
customer_master.head()
# 先頭5行を出力
# print(customer_master.head())

item_master = pd.read_csv('item_master.csv')
item_master.head()
# 先頭5行を出力
# print(item_master.head())

transaction_1 = pd.read_csv('transaction_1.csv')
transaction_1.head()
# 先頭5行を出力
# print(transaction_1.head())

transaction_detail_1 = pd.read_csv('transaction_detail_1.csv')
transaction_detail_1.head()
# 先頭5行を出力
# print(transaction_detail_1.head())

transaction_2 = pd.read_csv('transaction_2.csv')
transaction_2.head()
# 先頭5行を出力
# print(transaction_2.head())

transaction_detail_2 = pd.read_csv('transaction_detail_2.csv')
transaction_detail_2.head()
# 先頭5行を出力
# print(transaction_detail_2.head())

########################################

# データを行方向に結合する(concat/ユニオン)
transaction = pd.concat([transaction_1, transaction_2], ignore_index=True)
# print(len(transaction_1))
# print(len(transaction_2))
# print(len(transaction))

transaction_detail = pd.concat([transaction_detail_1, transaction_detail_2], ignore_index=True)
# print(len(transaction_detail))

# データを結合する(join/ジョイン)
join_data = pd.merge(transaction_detail, transaction[["transaction_id", "payment_date", "customer_id"]], on="transaction_id", how="left")
join_data.head()
# print(join_data.head())

# マスターデータを結合する
join_data = pd.merge(join_data, customer_master, on="customer_id", how="left")
join_data = pd.merge(join_data, item_master, on="item_id", how="left")
join_data.head()
# print(join_data.head())

########################################

# データ列を作成する
join_data["price"] = join_data["quantity"] * join_data["item_price"]
join_data[["quantity", "item_price", "price"]].head()
# print(join_data[["quantity", "item_price", "price"]].head())

# データを検算する
# print(join_data["price"].sum())
# print(transaction["price"].sum())

# print(join_data["price"].sum() == transaction["price"].sum())

########################################

# 各種統計量を把握する
# 欠損値の数を出力する
# print(join_data.isnull().sum()) # -> Trueの数をカウントする
# データ件数(count)、平均値(mean)、標準偏差(std)、最小値(min)、四分位数(25%, 75%)、中央値(50%)、最大値(max)
# print(join_data.describe())

# データの範囲を出力する
# print(join_data["payment_date"].min())
# print(join_data["payment_date"].max())

# データ型を確認する -> dtypes
# print(join_data.dtypes)

# データ型を変換する
join_data["payment_date"] = pd.to_datetime(join_data["payment_date"])
join_data["payment_month"] = join_data["payment_date"].dt.strftime("%Y%m")
join_data[["payment_date","payment_month"]].head()
# print(join_data[["payment_date","payment_month"]].head())

# データをソートする -> groupby
join_data.groupby("payment_month").sum()["price"]
# print(join_data.groupby("payment_month").sum()["price"])

join_data.groupby(["payment_month","item_name"]).sum()[["price","quantity"]]
# print(join_data.groupby(["payment_month","item_name"]).sum()[["price","quantity"]])

########################################
# データを可視化する

# ピポッドテーブルを作成する
# values -> 集計したい数値, aggfunc -> 集計方法
pd.pivot_table(join_data, index='item_name', columns='payment_month', values=['price','quantity'], aggfunc='sum')
# print(pd.pivot_table(join_data, index='item_name', columns='payment_month', values=['price','quantity'], aggfunc='sum'))

graph_data = pd.pivot_table(join_data, index='payment_month', columns='item_name', values='price', aggfunc='sum')
# print(graph_data.head())

# %matplotlib inline
plt.plot(list(graph_data.index), graph_data["PC-A"], label='PC-A')
plt.plot(list(graph_data.index), graph_data["PC-B"], label='PC-B')
plt.plot(list(graph_data.index), graph_data["PC-C"], label='PC-C')
plt.plot(list(graph_data.index), graph_data["PC-D"], label='PC-D')
plt.plot(list(graph_data.index), graph_data["PC-E"], label='PC-E')
plt.legend()