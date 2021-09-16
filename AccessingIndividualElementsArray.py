names = ["Jane","Bob","Tom"]
for name in names:
    if name == "Bob":
       print(name)

if names.__contains__("Bob"):
    print("Yes")
if "Tom" in name:
    print("Tom is Found")

if "Peter" in name:
    print("Found")
else:
    print("Peter is not Found")
counter = 0
names.extend(["Sylvia","Joan"])
for name in names:
       counter = counter + 1
       print(str(counter) , name)