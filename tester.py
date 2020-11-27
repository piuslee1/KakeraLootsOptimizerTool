#Additional rolls (guaranteed)
#Loot Morekakera.png Kakera (~20%)
#Loot Rtcd.png Better $rt cooldown (up to a 5 hour cooldown instead of 20) (~0.3%)
#Loot Disablemore.png Better disablelist capacity (~7.5%)
#Loot Addroll.png More (permanent) rolls (~0.1%)
#Loot Wlslot.png More wishlist slots (~0.45%)
#Loot Wishprotect.png Wishprotect levels (~14%)
#Loot Mudapin.png Mudapins (~10%)
from random import random
from random import seed

print("MADE BY MUSH POGGERS XQCL\n")
qualityinput=int(input("Please select a quality level from 1-100\n"))
quantityinput=int(input("Please select a quantity level from 1-100\n"))

quality=float(1+float(qualityinput)/100)
quantity=int(quantityinput)

additionalrollscount=0
additionalrollschance=10000

kakerarewardcount=0
kakerarewardchance=2000

betterrtcooldowncount=0
betterrtcooldownchance=30

disablespotscount=0
disablespotschance=750

addrollscount=0
addrollschance=10

wishlistspotcount=0
wishlistspotchance=45

wishprotectcount=0
wishprotectchance=1400

pincount=0
pintchance=1000

hundredcounter=0
while(hundredcounter<100):
  num1 = random.randint(1, 10000)
  qual=quality*num1
  
  if(qual<=additionalrollschance):
    additionalrollscount+=1
    num2=random.randint(1,100)
    if(num2 <= quantity):
      additionalrollscount+=1
      
  if(qual<=kakerarewardchance):
    kakerarewardcount+=1
    num2=random.randint(1,100)
    if(num2 <= quantity):
      kakerarewardcount+=1
      
  if(qual<=betterrtcooldownchance):
    betterrtcooldowncount+=1
    num2=random.randint(1,100)
    if(num2 <= quantity):
      betterrtcooldowncount+=1
      
  if(qual<=disablespotschance):
    disablespotscount+=1
    num2=random.randint(1,100)
    if(num2 <= quantity):
      disablespotscount+=1
      
  if(qual<=addrollschance):
    addrollscount+=1
    num2=random.randint(1,100)
    if(num2 <= quantity):
      addrollscount+=1
      
  if(qual<=wishlistspotchance):
    wishlistspotcount+=1
    num2=random.randint(1,100)
    if(num2 <= quantity):
      wishlistspotcount+=1
      
  if(qual<=wishprotectchance):
    wishprotectcount+=1
    num2=random.randint(1,100)
    if(num2 <= quantity):
      wishprotectcount+=1
      
  if(qual<=pinchance):
    pincount+=1
    num2=random.randint(1,100)
    if(num2 <= quantity):
      pincount+=1
print("This is the result of 100 tries with these quantity and quality settings\n")
print(f"Additional rolls: {additionalrollscount}\n")
print(f"Kakera reward: {kakerarewardcount}\n")
print(f"Better $rt cooldown: {betterrtcooldowncount}\n")
print(f"Disable spots: {disablespotscount}\n")
print(f"Added Perma rolls: {addrollscount}\n")
print(f"Added wishlist spots: {wishlistspotcount}\n")
print(f"Wish protect upgrade count: {wishprotectcount}\n")
print(f"Pin count: {pincount}\n")

    
  
  
  
  
  
