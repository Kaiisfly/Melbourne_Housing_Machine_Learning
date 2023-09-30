import pandas as pd

# Save File path
datapath = "C:/Users/kanse/PycharmProjects/Melbourne_Housing_Machine_Learning/melb_data.csv"
# Read Data
data = pd.read_csv(datapath)

# Show summary of data
data.describe()



