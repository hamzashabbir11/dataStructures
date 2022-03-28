print("Enter your Product Items and their Price, when done enter 'exit' ")
shop={ 
}
product_list=[]
price_list=[]
for i in range(20):

    product=input('Enter Product Name')
    if product=='exit':
        break
    product_list.append(product)
    price=int(input('Enter Price in usd'))
    price_list.append(price)
    shop[product_list[i]]=price_list[i]
print(shop)
price_usd=input("Enter dollar amount")
#print(*shop) # prints all the keys 
'''product_list=['a','b','c']
price_list=[1,2,3]'''
for i in range(len(product_list)):
    if price_list[i]<price_usd:
        print(product_list[i])
        


   


    


