import pandas as pd

# Load raw data
companies = pd.read_csv("data/raw/raw_companies.csv")
people = pd.read_csv("data/raw/raw_people.csv")

# Clean companies
companies["Company_Name"] = companies["Company_Name"].str.strip()
companies["Website"] = companies["Website"].str.strip()
companies["Industry"] = companies["Industry"].str.strip()

companies["Revenue_in_Millions"] = pd.to_numeric(
    companies["Revenue_in_Millions"], errors="coerce"
)
companies = companies[companies["Revenue_in_Millions"] >= 0]
companies = companies.drop_duplicates(subset=["Company_Name"])

# Clean people
people["Name"] = people["Name"].str.strip()
people["Email"] = people["Email"].str.lower().str.strip()
people["Company"] = people["Company"].str.strip()

people = people[people["Email"].notna()]
people = people.drop_duplicates(subset=["Email"])

# Save cleaned data
companies.to_csv("data/curated/clean_companies.csv", index=False)
people.to_csv("data/curated/clean_people.csv", index=False)

print("Data cleaned and saved!")