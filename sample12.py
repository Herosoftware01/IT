import pandas as pd


data = {
    'Department': ['Sales', 'Sales', 'HR', 'HR', 'IT', 'IT'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Salary': [50000, 60000, 45000, 47000, 70000, 72000]
}

df = pd.DataFrame(data)

pivot_df = pd.pivot_table(df, values='Salary', index='Department', aggfunc='mean')

print(pivot_df)