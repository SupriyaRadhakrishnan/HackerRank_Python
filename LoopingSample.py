total = 0
TAX = 1.08
productCount = 0
moreProducts = True
while moreProducts is True:
  productCount = productCount + 1
  productCost = input("Enter Product Cost: ")
  productCost = float(productCost)
  total = total + (productCost*TAX)
  anotherProduct = input("Do You have more Products ? (yes/no): ")
  if anotherProduct != "yes":
      moreProducts = False
print("Total No of Items : " , productCount)
print(total)