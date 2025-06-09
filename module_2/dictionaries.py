contact_info = {
    "Alice": "5555-1234",
    "Bob": "1234-444"
}

print(contact_info)

alice_phone = contact_info["Alice"]
print(alice_phone)

#update Alice's phone number
contact_info["Alice"] = "123456"
print(contact_info)

#add a new contact
contact_info["Eve"] = "555-6969"
print(contact_info)

#delete a contact
del contact_info["Bob"]
print(contact_info)

#Get the key
keys = contact_info.keys()
print(keys)

#get the values
values = contact_info.values()
print(values)

#get the items
items = contact_info.items()
print(items)