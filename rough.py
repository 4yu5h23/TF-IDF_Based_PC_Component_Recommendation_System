text="\nAsus TUF GAMING OC GeForce RTX 4070 Ti 12 GB\n$819.00\n"
    
    
def removeprice(text):    
    text=text.replace("\n","").replace("$"," ")
    text=text.split(" ")
    text.pop(-1)
    text = " ".join(text)
    print(text)

removeprice(text)

def removeunwanted(text):















    