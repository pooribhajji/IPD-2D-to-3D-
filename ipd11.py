
### PHASE 1 STARTS ####


# Processing an XML File Using Python
import xml.etree.ElementTree as ET
import pandas as pd

# Parse the XML file
tree = ET.parse('D:\Backup\ipd\d1.xml')
root = tree.getroot()

data = []

# The XML structure is:
# <gom.OHL>
#   <ov size="29">
#     <o id="0">
#       <gom.std.OSymbol label="door1" x0="1280.910406" y0="493.44241" ... />
#     </o>
#     ...
#   </ov>
#   <av size="0">...</av>
# </gom.OHL>

# Locate the <ov> element
ov_element = root.find('ov')
if ov_element is None:
    print("No 'ov' element found in the XML.")
else:
    # Iterate over each <o> element within <ov>
    for o in ov_element.findall('o'):
        # Each <o> element should have a child element that is the symbol
        # Since the tag name includes a dot, we use a loop to check each child
        for child in o:
            # Check if the child tag contains 'OSymbol' (to avoid namespace issues)
            if 'OSymbol' in child.tag:
                # Extract all desired attributes
                row = {
                    'label': child.get('label'),
                    'x0': child.get('x0'),
                    'y0': child.get('y0'),
                    'x1': child.get('x1'),
                    'y1': child.get('y1'),
                    'resize': child.get('resize'),
                    'morph': child.get('morph'),
                    'direction': child.get('direction')
                }
                data.append(row)

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

if df.empty:
    print("The DataFrame is empty. Check if the XML file structure matches the expected format.")
else:
    print("Extracted DataFrame:")
    print(df.head())

# Optionally, save the DataFrame to a CSV or JSON file
df.to_csv("extracted_blueprint_metadata.csv", index=False)
print("Data saved to extracted_blueprint_metadata.csv")



###GIVES EXTRACTED DATA FRAME and STORES IT IN CSV FILES. #####