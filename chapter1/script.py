import pandas as pd

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

# データを行方向に結合する(concat/ユニオン)
transaction = pd.concat([transaction_1, transaction_2], ignore_index=True)
# print(len(transaction_1))
# print(len(transaction_2))
# print(len(transaction))

transaction_detail = pd.concat([transaction_detail_1, transaction_detail_2], ignore_index=True)
# print(len(transaction_detail))

# データを結合する(join/ジョイン)
join_data = pd.merge(transaction_detail, transaction[["transaction_id", "payment_date"]], on="transaction_id", how="left")
join_data.head()
print(join_data.head())