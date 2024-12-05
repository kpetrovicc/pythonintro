# Using dictionaries in Python - allows us to store information in key-value pairs
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
# All keys have to be uniuqe, and they are case sensitive

month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(month_conversions["Nov"]) # Output: November takes key in [] and returns value for that key
print(month_conversions.get("Luv", "Not a valid key")) # Output: December takes key in get() and returns value for that key