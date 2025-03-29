#Dictionary()
#we have key:value in dictionary
#Ordered collection of key value pairs
#we can convert this to another language because it has some standard format


stud={}
print(type(stud))  #output <class 'dict'>

student={"firstname":"sachin",
         "last_name":"Tendulkar",
         "age":40,
         "city":"Mumbai",
         "Skills":['Batting','Bowling','Fielding']
         }
print(student)

EC2={"pem_key":"name.pem",
         "type":"T2micro",
         "AMI":40,
         "Volume":"30GB",
         }
print(EC2["type"])  #Display the value of the key
print(EC2["pem_key"])

# print(EC2["security_groups"])  #Displays error since there is no such key so use .get method instead

print(EC2.get("pem_key"))
print(EC2.get("type","Not allocated any value")) #when value is there it prints if not it shows next default value
print(EC2.get("security_groups","Not allocated any value"))

print(EC2.keys)
print(EC2.values)
#print(list(EC2.keys))

out=EC2.items() #list of tuples means gives both key,value
print(out)


#duplicates key example

EC23={"pem_key":"name.pem",
         "type":"T2micro",
         "AMI":40,
         "Volume":"30GB",
         "pem_key":"pem.pem"
         }

print(EC23)


#adding one dictoinary into another dictionary use Update()

other_details={"user":"itd"}

print(EC23)
EC23["Something"]=100
print(EC23)

print(EC23.pop("pem_key"))

print(EC23.popitem())
