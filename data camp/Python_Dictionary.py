from turtle import clear
clear
# Dictionary in Python 
# Data is stored in a class dictionary in the form of a Key Value Pair 
data={
"Hamza": 'Single',
"Huzaifa" :3.25,
"Maba" : 3.8,
"Asad" :3.5,
"Asad" :4,
"Asad" :5 #5 wale value uthai ga wo 
}
print(data["Hamza"])
print(data["Maba"])
print(type(data))
print(data)
# keys in a dict must have immutable objects i.e. they cannot be chnaged 
# list however can be changed 
data['Neha']=3.13
print(data["Neha"])
print('Hamza' in data)
print('Haroon ' in data)
#updating a value in dict 
data["Hamza"]=2.99
del data["Neha"]
print(data.items)











