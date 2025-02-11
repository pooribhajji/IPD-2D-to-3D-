import xml.etree.ElementTree as ET
import pandas as pd

# Parse the XML file
tree = ET.parse("D:\Backup\ipd\d1.xml")
root = tree.getroot()

# Extract data into a list of dictionaries
data = []
for blueprint in root.findall("blueprint"):
    blueprint_id = blueprint.get("id")
    for room in blueprint.findall("room"):
        room_type = room.get("type")
        width = room.find("width").text
        height = room.find("height").text
        floor = room.find("floor").text
        data.append({
            "blueprint_id": blueprint_id,
            "room_type": room_type,
            "width_ft": width,
            "height_ft": height,
            "floor": floor
        })

# Convert list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# Display first 5 rows
print("Data extracted from XML:")
print(df.head())

