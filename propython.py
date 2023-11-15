from prettytable import PrettyTable

# Create a table object
table = PrettyTable()

# Define the columns
table.field_names = ["Name", "Age", "City", "Occupation"]

# Add data to the table
table.add_row(["John", 30, "New York", "Engineer"])
table.add_row(["Alice", 25, "San Francisco", "Designer"])
table.add_row(["Bob", 35, "Los Angeles", "Developer"])

# Print the table
print(table)
