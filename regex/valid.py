import re

email=input("provide email: ").strip()

# # test
# if "@" in email and "." in email:
#     print("valid")
# else:
#     print("Invalid")

# # using more specific rules
# username,domain=email.split("@")

# if (username) and ("." in domain):
#     print("Valid")
# else: print("Invalid")



# re(regEx) library
# search function
# re.search(pattern,string,flags=0)
# +:-with repetition from 1 or more
# .:- any character
# \:- escape
# ^:- start of the string
# &:- end of the string
# []:- set of characters that are valid
# [^]:- set of characters that are not valid
# [a-zA-Z0-9]:- all these elements will be included
# [all the elements in this bracket will be valid]
# \w:- alphanumeric \w=[a-zA-Z0-9_]
pattern=r"^\w+@\w+\..+$"
if re.search(pattern,email):
    print("Valid")
else:
    print("Invalid")

