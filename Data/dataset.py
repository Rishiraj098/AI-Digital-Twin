import pandas as pd
import numpy as np

np.random.seed(42)

rows = 50000

marketing = np.random.randint(5000, 100000, rows)
employees = np.random.randint(5, 100, rows)
time = np.random.randint(1, 365, rows)

sales = (
    5000
    + marketing * 0.75
    + employees * 1200
    + time * 40
    + np.random.normal(0, 10000, rows)
)

df = pd.DataFrame({
    "Marketing_Spend": marketing,
    "Employees": employees,
    "Time": time,
    "Sales": sales
})

df.to_csv("sales_data.csv", index=False)

print("✅ Dataset Created Successfully")