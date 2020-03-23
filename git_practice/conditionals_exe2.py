name = "John"

singer = "Lennon"
president = "Kennedy"
actor = "Travolta"

profession = "president"

if profession == "president":
    name += " " + president
elif profession == "singer":
    name += " " + singer
elif profession == "actor":
    name += " " + actor
print(name)