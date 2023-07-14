import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('HAM10000_metadata.csv')

# Define the range of image IDs you're interested in
start_id = 24306
end_id = 25305

# Extract the numerical ID from the image_id column
df['id'] = df['image_id'].apply(lambda x: int(x.split('_')[1]))

# Select the rows where the id column is within the range
subset_df = df[(df['id'] >= start_id) & (df['id'] <= end_id)]

# Remove the id column
subset_df = subset_df.drop('id', axis=1)

# Print the subset DataFrame
subset_df.to_csv('subset_metadata.csv', index=False)