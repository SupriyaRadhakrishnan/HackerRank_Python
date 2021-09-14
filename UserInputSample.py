productCost = input("Enter Price of the product : ")  #All inputs via console is String
productCost = int(productCost)
TAX = 1.08
shippingPrice = 5

#Shipping price

if(productCost > 100):
    finalPrice = productCost * TAX + shippingPrice
else:
    finalPrice = productCost * TAX
    print(finalPrice)