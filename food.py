import pandas as pd
from sqlalchemy import create_engine


# Load cleaned data
df = pd.read_csv("data/processed/cleaned_food_delivery.csv")

# Convert date & time
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Order_Time'] = pd.to_datetime(df['Order_Time']).dt.time

# MySQL connection
engine = create_engine(
    "mysql+pymysql://root:password@localhost:3306/food_delivery_db"
)

# Insert data
df.to_sql(
    name='food_orders',
    con=engine,
    if_exists='append',
    index=False,
    chunksize=5000
)

print("✅ Data successfully loaded into MySQL")
