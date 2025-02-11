# Convert the DataFrame to JSON format
json_data = df.to_json("blueprints_metadata.json", orient="records", indent=4)
print("XML data successfully converted to JSON!")

## CONVERTED THE DATA FRAME IN JSON FORMAT ###