name = "John"
age = 44
weight = 81.955437
sentence = "Hello {1}.You are {0} years Old"
print(sentence.format(age,name))

sentence = "Hello {1}.You are {0} years Old and you weigh {2:0.2f}" #rounding off the float value
print(sentence.format(age,name,weight))