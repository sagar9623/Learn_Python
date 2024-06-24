# Dictionaries
# Add "Karan" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.

phonebook = {
    "Sagar" : 9856578955,
    "Kaustubh" : 8956894578,
    "Karan" : 7894561237
}

phonebook["Shivam"] =  8547856921 
del phonebook["Karan"]

if "Shivam" in phonebook:
    print("Shivam is listed in the phonebook.")
if "Karan" not in phonebook:
    print("Karan is not listed in the phonebook.")

print(phonebook)