# 1.  Create two dictionaries, Jane and John, to store contact information for Jane and John, respectively.
# 2.  Each contact dictionary contains keys for 'name,' 'phone,' and 'email' with corresponding values.
# 3.  Create a contacts dictionary and use the names 'Jane' and 'John' as keys, associating them with their respective contact dictionaries.
# 4.  Print Jane's contact information.
# 5.  Update Jane's phone number.
# 6.  Print Jane's updated contact information.



# Krijo dictionaries
jane = {
    "name": "Jane",
    "phone": "555-1234",
    "email": "jane@example.com",
    "birthday": "01/03/2006"
}

john = {
    "name": "John",
    "phone": "555-5678",
    "email": "john@example.com",
    "birthday": "03/01/2007"
}

# Krijo contacts dictionary
contacts = {
    "Jane": jane,
    "John": john
}

# Printo Jane's contact information
print("Here is Jane updated phone number")
print(contacts["Jane"])
print(contacts["John"])

# Update Jane's phone number
contacts["Jane"]["phone"] = "555-9999"

# Step 6: Print Jane's updated contact information
print("Here is Jane updated phone number")
print(contacts["Jane"])
