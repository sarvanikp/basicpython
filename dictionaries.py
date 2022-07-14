


handbags = {"color": "pink", "brand": "Tory burch", "price_in_$": "300", "type": "tote"}
#print(handbags["brand"])

#print(handbags["material"]) #fetching a key which does not exist
#get method for dict: 
#print(handbags.get("type"))
#print(handbags.get("material", "leather")) #default is leather for material key

handbags["material"] = "leather" #add extra keys as needed

#print(handbags)

v = handbags["color"]
#print(v)

#print("hello the colour of the bag is "  + handbags["color"])
#print("hello the colour of bag is " + handbags.get("color"))


#update color#add attribute # update cost
handbags.update({"color": "blue", "price_in_$":"250", "size": "small"})
#print(handbags)

#print keys, items, values, len
#print(len(handbags))
#print(handbags.keys())
#print(handbags.values())
print(handbags.items())

#for a in handbags.keys(): #handbag.keys() returns list of strings and "a" is a variable which represents each item in the list of handbags.keys()
    #print(a)

for b in handbags.items():
    print(b)

for k,v in handbags.items(): #handbags.items() returns a list with each item in the form of ("key","value") so we use 2 variables in the for loop to represent key and value in each item
    print(v)
    print(k)
    




