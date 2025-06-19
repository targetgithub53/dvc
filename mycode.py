import os
import pandas as pd

# 1. Create a simple DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'marks': [85, 90, 95]
    
}
df = pd.DataFrame(data)
df_new_row={'name':'ram','marks':98}
df.loc[len(df.index)]=df_new_row

# 2. Create a folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

# 3. Save DataFrame as CSV
output_path = "data/processed/students.csv"
df.to_csv(output_path, index=False)

print(f"Data saved to {output_path}")
