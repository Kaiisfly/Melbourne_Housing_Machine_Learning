import pandas as pd

# Save File path
datapath = "melb_data.csv"
# Read Data
data = pd.read_csv(datapath)

# Show summary of data
data.describe()


