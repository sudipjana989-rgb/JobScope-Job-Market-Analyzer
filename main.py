import pandas as pd

# Load the dataset

df = pd.read_csv("job_data.csv")

print("=" * 40)
print("       JOB MARKET ANALYZER")
print("=" * 40)

# 1. Total job listings

print("\n1. TOTAL JOBS")
print("Total listings:", len(df))

# 2. Jobs by title

print("\n2. JOBS BY TITLE")
print(df["Job_Title"].value_counts())

# 3. Jobs by location

print("\n3. JOBS BY LOCATION")
print(df["Location"].value_counts())

# 4. Most demanded skills

skills = ["Python", "SQL", "Excel", "Machine_Learning"]

print("\n4. SKILL DEMAND")
skill_demand = df[skills].sum().sort_values(ascending=False)
print(skill_demand)

# 5. Average salary by job title

print("\n5. AVERAGE SALARY BY JOB TITLE")
average_salary = df.groupby("Job_Title")["Salary"].mean()
print(average_salary.round(2))

# 6. Find the highest-paying job listing

print("\n6. HIGHEST-PAYING JOB LISTING")
highest_job = df.loc[df["Salary"].idxmax()]

print("Job:", highest_job["Job_Title"])
print("Company:", highest_job["Company"])
print("Location:", highest_job["Location"])
print("Annual salary: Rs.", highest_job["Salary"])

# 7. Find jobs requiring Python

print("\n7. JOBS REQUIRING PYTHON")

python_jobs = df[df["Python"] == 1]

print(python_jobs[["Job_Title", "Company", "Location", "Salary"]])

print("\nAnalysis completed successfully!")
import matplotlib.pyplot as plt

# Chart 1: Skill Demand
skills = ["Python", "SQL", "Excel", "Machine_Learning"]

skill_demand = df[skills].sum().sort_values(ascending=False)

skill_demand.plot(kind="bar")

plt.title("Demand for Different Skills")
plt.xlabel("Skills")
plt.ylabel("Number of Job Listings")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("skill_demand.png")
plt.show()


# Chart 2: Average Salary
average_salary = df.groupby("Job_Title")["Salary"].mean()

average_salary.sort_values().plot(kind="bar")
plt.title("Average Salary by Job Title")
plt.xlabel("Job Title")
plt.ylabel("Average Annual Salary (INR)")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("average_salary.png")
plt.show()

print("Both charts created successfully!")