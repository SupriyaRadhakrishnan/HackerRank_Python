itemsCost = [50,20,30,40,70]
total = 0
for cost in itemsCost:
    total = total + cost

print("Total Bill is  : " , str(total))
print("Average amount spent: ",str(total/3))



#Collections helps to process large ampunt of data of same type.
#Array Facts : Name,Type of data,Insert/Delete based on the position
#Insert using append
#Delete using pop
#Error will occur if we try to delete an element that is not present

#print(itemsCost[5])  Error : IndexError: list index out of range
