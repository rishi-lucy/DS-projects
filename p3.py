import pandas as pd

df1 = pd.DataFrame(
    {"Name": ["Ravi", "Sita", "Arun"], "Marks": [85, None, 78], "Grade": ["A", "B", None]},
    index=[101, 102, 103]
)
df2 = pd.DataFrame(
    {"Name": ["Ravi", "Sita", "Kiran"], "Marks": [90, 88, 82], "Grade": [None, "A", "B"]},
    index=[101, 102, 104]
)

print("First DataFrame:")
print(df1)
print("\nSecond DataFrame:")
print(df2)
print("\nMerged by index:")
print(pd.merge(df1, df2, left_index=True, right_index=True, how="outer", suffixes=("_DF1", "_DF2")))
print("\nCombined with combine_first():")
print(df1.combine_first(df2))
