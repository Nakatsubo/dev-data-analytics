import pandas as pd

# データを読み込む
uriage_data = pd.read_csv("uriage.csv")
uriage_data.head()
# print(uriage_data.head())

kokyaku_data = pd.read_excel("kokyaku_daicho.xlsx")
kokyaku_data.head()
# print(kokyaku_data.head())