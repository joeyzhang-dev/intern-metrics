import pandas as pd
import re

# INPUT FILE 
FILENAME = "internships.csv" 
df = pd.read_csv(FILENAME) # Loading CSV
df['Role'] = df['Role'].astype(str).str.lower()

# Regex filter roles
role_keywords = r"swe|software engineer|software engineering|full[- ]?stack|front[- ]?end|back[- ]?end|web developer|software developer| react"
df['Match'] = df['Role'].str.contains(role_keywords, regex=True)

# Parsing posted date
df['Date Posted'] = pd.to_datetime(df['Date Posted'], errors='coerce')
df['Month'] = df['Date Posted'].dt.to_period('M')

# Validating Matching roles
filtered_df = df[df['Match'] == True]

# Match Monthly Counter
monthly_counts = filtered_df.groupby('Month').size().reset_index(name='Count')

# Otput
print("SWE-related internships per month:\n")
print(monthly_counts)

# Optional: Save results to CSV
monthly_counts.to_csv("monthly_swe_counts.csv", index=False)