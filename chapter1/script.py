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
print(join_data["price"].sum())
print(transaction["price"].sum())

print(join_data["price"].sum() == transaction["price"].sum())

########################################
