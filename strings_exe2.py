string1 = "good"
string2 = "morning"
help = string1[0]
s1 = string1.replace(string1[0], string2[0])
s2 = string2.replace(string2[0], help)
new_string = s1 + " " + s2
print(new_string)