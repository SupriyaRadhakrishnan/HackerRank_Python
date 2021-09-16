colors = ["Blue","Green","Red","Orange","Yellow"]

colorsCount = len(colors)
print("Total No Of colors : " , str(colorsCount))
for x in range(colorsCount):
    print(colors[x])

colors.append("Violet")
for each in colors:
    print(each)
print("Total No Of colors after append : " , str(len(colors)))

colors.pop(2)
for each in colors:
    print(each)
print("Total No Of colors after append : " , str(len(colors)))


