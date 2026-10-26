import pandas as pd

index = pd.MultiIndex.from_tuples(
    [("Engineering", "CSE"), ("Engineering", "ECE"),
     ("Science", "Physics"), ("Science", "Chemistry")],
    names=["Department", "Branch"]
)
data = pd.DataFrame({"2025": [85, 78, 92, 88], "2026": [90, 82, 95, 91]}, index=index)

print("Original Data:")
print(data)
unstacked = data.unstack()
print("\nAfter unstack():")
print(unstacked)
print("\nAfter stack():")
print(unstacked.stack())
