
import pandas as pd

data = [
    {
        "name": "John",
        "age": 30,
        "city": "New York"
    },
    {
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
    },
    {
        "name": "Bob",
        "age": 35,
        "city": "Seattle"
    },
     {
        "name": "Lulu",
        "age": 55,
        "city": "Tokyo"
    }
]

df = pd.DataFrame(data)

print(df)

##new df from data where age is greater than 31
df2 = df[df["age"] > 31]
print(df2)