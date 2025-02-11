# Ensure numeric conversion for coordinate columns
df['x0'] = pd.to_numeric(df['x0'])
df['x1'] = pd.to_numeric(df['x1'])
df['y0'] = pd.to_numeric(df['y0'])
df['y1'] = pd.to_numeric(df['y1'])

# Compute width and height based on coordinate differences
df['width'] = abs(df['x1'] - df['x0'])
df['height'] = abs(df['y1'] - df['y0'])

# Compute the area as a product of width and height
df['area'] = df['width'] * df['height']

print(df[['label', 'width', 'height', 'area']].head())


## COMPUTE WIDTH AND HEIGHT AND AREA BASED ON NUMERIC DIFFERENCES ###