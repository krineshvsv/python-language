'''
    strip():
        -> "strip()" function removes extra spaces and characters from the beginning and
            end of a string.
'''
# Email slicer with python.
email=input("Enter Your Email:").strip()

'''
    username=email[:email.index("@")]
        ->this part uses slicing to extract the substring from the beginning of the email
            ("email[:") up to ,but not including , the "@" symbol
            ("email.index("@")").
    
    domain_name=email[email.index("@")+1:]
        ->This part uses slicing to extract the substring starting from one character
            after the '@' symbol('email.index(@")+1') until the end of the email9(':').
'''
username=email[:email.index("@")]
domain_name=email[email.index("@")+1:]
format_=(f"Your user name is '{username}' and your domain is '{domain_name}'")
print(format_)