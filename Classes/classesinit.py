import emoji

class nft:
    def __init__(self,name,price,bc):
        self.name=name
        self.price=price
        self.blockchain=bc
        x=5
    def greetMe(self):
        print('Hello Ape, Vitalik wants to be your friend ' + emoji.emojize(':red_heart:'))

nft1=nft('BAYC','100 ETH','Eth Mainnet')

print(nft1.price)
nft1.greetMe()
nft1.blockchain='Polygon'
print(nft1.blockchain)

        