# Making a Pandas Data Frame from a Dictionary 
import pandas as pd #importing pandas library
import requests as rq
import emoji 
#making 3 lists for our small database(DataFrame)
Names=['John', 'Taylor', 'Emily','Jimmy']
Age=[18,22,26,30]
gender=['M','F','F','M']
#Making Dictionary and Giving the List as the "Value" in Key Value pairs
My_dictionary={'identifier' : Names,
'age_group': Age,
'sex':gender
}
print(My_dictionary) 
df=pd.DataFrame(My_dictionary) #making DataFrame from My_dictionary
df.index=['J','T','E','J'] 
print(df)
print(type(df))
r=rq.get('https://www.google.com/')
print(r.status_code)
print(df['age_group'])
print(ord('A')) 
print("\U0001f600")
print(emoji.emojize(':red_heart:'))

"""import pandas as pd
# Fix import by including index_col
cars = pd.read_csv('cars.csv',index_col=0)
# Print out cars
print(cars)"""