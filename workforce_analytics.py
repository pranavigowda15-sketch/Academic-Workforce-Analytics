import pandas as pd

# Load faculty data
df = pd.read_csv("faculty_data.csv")

# Basic analysis
print("Total Faculty:", len(df))
print("\nDepartment-wise Faculty Count:")
print(df['department'].value_counts())

# Average workload by department
avg_workload = df.groupby('department')['workload_hours'].mean()
print("\nAverage Workload by Department:")
print(avg_workload)

# Skill distribution
skills = df['primary_skill'].value_counts()
print("\nSkill Distribution:")
print(skills)
