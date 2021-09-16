def calculateTax(productPrice):
    TAX = 1.08
    afterTax = productPrice * TAX
    return afterTax

def calculateShipping(productPrice):
    if productPrice < 100:
        return (productPrice + 10)
    else:
        return productPrice

#main program
productCost = input("Enter the Price :")
productCost = int(productCost)
finalPrice = calculateTax(calculateShipping(productCost))
print("Final Price is : " , str(finalPrice))