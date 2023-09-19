import pandas as pd

# Read a CSV file into a data frame
data = pd.read_csv("C:/Users/VMUser/Documents/data.csv")

# Display the first few rows of the dataframe
# print(data.head())

# Creating a Dataframe from a dictionary
data_dict = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 22]
}

df = pd.DataFrame(data_dict)
# print(df)

# Selecting a single column
ages = df["Age"]
# print("\n", ages)

# Selecting multiple columns
subset = df[["Name", "Age"]]
print(subset)
