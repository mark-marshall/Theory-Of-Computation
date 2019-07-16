import re # module for processing regular expressions https://docs.python.org/3/library/re.html

# Initial prompt to user
line = input("Enter a phone number to validate or 'exit' when done. ")

# Define your regex
phone_re = r"[-(\s]?([0-9]{3})[-)\s]?[-)\s]?([0-9]{3})[-\s(]?[-)\s]?([0-9]{4})"

while line != "exit":
    # Find matches 
    match = re.findall(phone_re, line)
    
    # If no match found, print that no number was found
    if not match:
        print("Invalid number")
    
    
    # Else, break number up into area code, prefix, and suffix
    phone = match[0]
    phone_constituents = re.sub(r"[\s(')]", '', str(phone))
    ans = re.split(',', phone_constituents)
    # Print the formated number output
    print(f"Area Code: {ans[0]}\nPrefix: {ans[1]}\nSuffix: {ans[2]}")
    
    # Done validating, read in a new line
    line = input("Enter a phone number to validate or 'exit' when done. ")