import pandas as pd

# Read the Excel file
data = pd.read_excel("employee_data.xlsx")

# Calculate 10% bonus
data["Bonus"] = data["Salary"] * 0.10

# Add Status based on Salary
data["Status"] = data["Salary"].apply(
    lambda salary: "High Salary" if salary >= 50000 else "Standard"
)

# Display updated data
print("Employee Data:\n")
print(data)

# -------- Summary Report --------
print("\n========== Employee Summary ==========")

print("Total Employees :", len(data))
print("Total Salary    :", data["Salary"].sum())
print("Average Salary  :", data["Salary"].mean())
print("Highest Salary  :", data["Salary"].max())
print("Lowest Salary   :", data["Salary"].min())
print("Total Bonus     :", data["Bonus"].sum())

print("======================================")

# Save updated data
summary = pd.DataFrame({
    "Metric": [
        "Total Employees",
        "Total Salary",
        "Average Salary",
        "Highest Salary",
        "Lowest Salary",
        "Total Bonus"
    ],
    "Value": [
        len(data),
        data["Salary"].sum(),
        data["Salary"].mean(),
        data["Salary"].max(),
        data["Salary"].min(),
        data["Bonus"].sum()
    ]
})

with pd.ExcelWriter("employee_bonus.xlsx") as writer:
    data.to_excel(writer, sheet_name="Employee Data", index=False)
    summary.to_excel(writer, sheet_name="Summary", index=False)

print("\nBonus and Status added successfully!")