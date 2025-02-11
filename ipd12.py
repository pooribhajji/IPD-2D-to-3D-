# Fill missing values with "unknown"
df.fillna("unknown", inplace=True)

# Convert all text to lowercase
df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

# Save the cleaned DataFrame to a new XML or JSON file as needed
df.to_csv("cleaned_metadata.csv", index=False)  # Optional: to CSV if needed
print("Data cleaned!")


## DATA CLEANING ###

