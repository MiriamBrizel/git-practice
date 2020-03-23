password = 123
confirm_password = 124
if password == confirm_password:
    is_correct = True
else:
    is_correct = False
string = "The password is correct: "
if is_correct:
    string += "True"
else:
    string += "false"    
print(string)