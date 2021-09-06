#to open the json doc
import json

fd = open("/content/Srinu.json",'r')
r = fd.read()
fd.close()

Srinu = json.loads(r)

#to get new prod_id,name,pr,qn
prod_id = str(input("Enter product id:"))
name = str(input("Enter name:"))
pr = int(input("Enter price:"))
qn = int(input("Enter quantity:"))

manu[prod_id] = {'name': name, 'pr': pr, 'qn': qn}

js = json.dumps(manu)

fd = open("/content/manu.json",'w')
fd.write(js)
fd.close()

#to open the updated doc
import json

fd = open("/content/Srinu.json",'r')
r = fd.read()
fd.close()

Srinu = json.loads(r)

#to get prod_id and quantity from to do buy
d_prod  = str(input("Enter the product_Id: "))
d_quant = int(input("Enter the quantity: "))
if Srinu[d_prod]['qn']<=0:
  print("product is not available in store")
elif d_quant>Srinu[d_prod]['qn']:
  print("That much quantity is not available")
else:
  print("Product: ", Srinu[d_prod]['name'])
  print("Price: ", Srinu[d_prod]['pr'])
  print("Billing Amount: ", Srinu[d_prod]['pr'] * d_quant)
  Srinu[d_prod]['qn'] = Srinu[d_prod]['qn'] - d_quant

#to update the file as per sales
import json

fd = open("/content/Srinu.json",'r')
r = fd.read()
fd.close()

Srinu = json.loads(r)

#to print the reciept
reciept={'prod' : d_prod, 'qn' : d_quant, 'amount': Srinu[d_prod]['pr'] * d_quant}