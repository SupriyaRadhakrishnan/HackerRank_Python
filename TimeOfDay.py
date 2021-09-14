name = input("Enter you name :")
timeNow = input("Enter in Military Style :")
timeNow = int(timeNow)

if timeNow <=1200:
    print("Good Morning %s" % (name))
elif (timeNow >1200 and timeNow <= 1600):
    print("Good Afternoon %s" % (name))
elif 1600 < timeNow <= 2400:
    print("Go0d Night %s" % (name))