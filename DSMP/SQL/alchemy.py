import pandas as pd
from sqlalchemy import create_engine

# 1. Connection settings
USER = "root"
PASSWORD = "1234!" # Updated to match your reset password
HOST = "127.0.0.1"      
PORT = "3306"                 
DATABASE = "olympics"

# 2. Build connection string
connection_string = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

try:
    # 3. Create the SQLAlchemy Engine
    engine = create_engine(connection_string)
    print("Engine created successfully!")

    # 4. Load your CSV data
    df = pd.read_csv(r"C:\Users\rahul_tvnnpln\Downloads\athlete_event.csv")
    print(f"Loaded CSV successfully! Found {len(df)} rows.")

    # 5. Upload data to MySQL
    print("Uploading data to MySQL")
    df.to_sql(name="athlete_event", con=engine, if_exists="append", index=False)
    print("Data uploaded successfully to MySQL Workbench!")

except Exception as e:
    print(f"An error occurred: {e}")