# Making a Pandas Data Frame from a Dictionary 
import pandas as pd #importing pandas library
import requests as rq
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
print(df)
r=rq.get('https://www.google.com/')
print(r.status_code)
a=rq.post('https://www.google.com/',data='5')
print(a)
