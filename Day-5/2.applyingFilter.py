# Creating a dataframe from a dictionary
# Creating a Dataframe from a dictionary
import pandas as pd

data_dict = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 22],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data_dict)
"""
print(df)
# Selecting a single column
ages = df["Age"]
print("Ages:\n", ages)

# Selecting multiple columns
subset = df[["Name", "City"]]
print("Subset:\n", subset)

# Filtering based on a condition
adults = df[df["Age"] >= 18]
print("Adults\n", adults)

print(adults["Name"])

# Grouping the column and calculating the mean age
grouped = df.groupby("City")["Age"].mean()
print("Mean age by city:\n ", grouped)

# Sorting the dataframe by age in descending order
sorted_df = df.sort_values(by="Age", ascending="False")
print("Sorted Dataframe:\n", sorted_df)
"""

"""
# Adding a new column
df["Gender"] = ["Female", "Male", "Male"]
print("Data frame with gender:\n", df)

# Removing a column
df.drop(columns="Gender", inplace=True)
print("After removing the data frame:\n", df)
"""

# Applying a custom function to age column


def classify_age(age):
    if age < 25:
        return "Young"
    elif 25 <= age < 40:
        return "Adult"
    else:
        return "Senior"


df["Age Category"] = df["Age"].apply(classify_age)
print("data frame with age category:\n", df)

