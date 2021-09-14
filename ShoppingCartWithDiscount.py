productCost = input("Enter Price of the product : ")  #All inputs via console is String
productCost = int(productCost)
TAX = 1.08
shippingPrice = 5
loyalityPoints = 0

#Shipping price

if(productCost > 500):
    discount = productCost * (5/100)
    taxedPrice = (productCost-discount) *TAX
    finalPrice = taxedPrice
    loyalityPoints = 100
    print("The Final Price is : ", finalPrice)
    print("Total Loyality Points : " ,loyalityPoints)

else:
    finalPrice = productCost * TAX +shippingPrice
    print(finalPrice)