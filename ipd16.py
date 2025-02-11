import matplotlib.pyplot as plt

# Group by the symbol 'label' and compute the average area
avg_area = df.groupby("label")["area"].mean().reset_index()

# Create a bar chart
plt.bar(avg_area["label"], avg_area["area"], color='skyblue')
plt.xlabel("Symbol Label")
plt.ylabel("Average Area")
plt.title("Average Area of Symbols by Label")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

## PLOTS BAR GRAPH BASED ON  AVERAGE AREA OF SYMBOL ###



#PHASE 1 COMPLETED!!!!
#Parsed XML data into a DataFrame
#Cleaned and standardized the data
#Converted the data into JSON (or CSV) format
#Visualized key aspects of your data