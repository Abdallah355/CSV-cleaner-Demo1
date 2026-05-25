import pandas as pd

df = pd.read_csv("Contacts.csv") #read contacts csv

df.columns = df.columns.str.strip() #remove extra spaces in columns

df["Name"] = df["Name"].str.strip().str.title() #remove extra spaces and capitalize properly

df["Email Valid"] = df["Email"].apply(lambda x: "Yes" if "@" in str(x) else "No") #flag the emails with no @ symbol

df["Phone"] = df["Phone"].str.replace(r"\D", "", regex= True)

df.to_csv("Contacts_Cleaned.csv", index = False)

print("Done! Check Contacts_Cleaned.csv")
