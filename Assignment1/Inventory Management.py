from itertools import product
print("Enter your Product Items and their Price, when done enter 'exit' ")
shop={ 
}

product_list=[]
price_list=[]
for i in range(20):

    product=input('Enter Product Name')
    if product=='exit'.lower:
        break
    product_list.append(product)
    price=input('Enter Price in usd')
    price_list.append(price)
    shop[product_list[i]]=price_list[i]

print(shop)


    


