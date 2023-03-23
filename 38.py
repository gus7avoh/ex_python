
p= ['milk','eggs','carrot','cheese'] 

v =float(input ('what are the value? '))

print("""
metod to pay 
[1] card/ticket
[2] debt
[3] 2x on card
[4] 3x or more times on the card 
""")

m=input('tipy the metod: ')


if m ==('1'):
    print ('the price of the your buys will be {:.2f} dollars'.format((v*0.1)-v))

if m ==('2'):
    print ('the price of the your buys will be {:.2f} dollars'.format((v*0.05)-v))

if m ==('3'):
    print ('the price of the your buys will be {:.2f} dollars'.format(v))

if m ==('4'):
    print ('the price of the your buys will be {:.2f} dollars'.format((v*0.2)+v))



