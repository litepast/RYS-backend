import pandas as pd

data = {'Sport': ['soccer', 'soccer', 'basketball', 'basketball'],
        'Action': ['goal', 'ball', '3-pointer', 'net']}

df = pd.DataFrame(data)
data_dict = df.groupby('Sport')['Action'].apply(list).to_dict()

print(data_dict)