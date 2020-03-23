string = "tomato"

if len(string) < 4:
    sub_string = ""
else:
    sub_string = string[0] + string[1] + string[-2] + string[-1]
print(sub_string)