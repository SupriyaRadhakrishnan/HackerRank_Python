name = input ("Enter you name :")
experience = input ("Enter you experience :")
experience = float(experience)

if (experience > 0 and experience <= 2):
    print(name,"is a Junior")
elif (experience <= 6 and experience > 2):
    print(name,"is an intermediate")
elif experience > 6:
    print(name, "is a Senior")
else:
    print(name,"is not a programmer")