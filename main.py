#Additional rolls (guaranteed)
#Loot Morekakera.png Kakera (~20%)
#Loot Rtcd.png Better $rt cooldown (up to a 5 hour cooldown instead of 20) (~0.3%)
#Loot Disablemore.png Better disablelist capacity (~7.5%)
#Loot Addroll.png More (permanent) rolls (~0.1%)
#Loot Wlslot.png More wishlist slots (~0.45%)
#Loot Wishprotect.png Wishprotect levels (~14%)
#Loot Mudapin.png Mudapins (~10%)
import random


print("MADE BY MUSH POGGERS XQCL\n")
qualityinput=int(input("Please select a quality level from 1-100\n"))
quantityinput=int(input("Please select a quantity level from 1-100\n"))
tryinput=int(input("Please enter how many tries you'd like. \n"))
q1=float(qualityinput)/100.00
quality=1.00+q1
quantity=float(quantityinput)

additionalrollscount=0
additionalrollschance=5000.00

kakerarewardcount=0
kakerarewardchance=1000.00

betterrtcooldowncount=0
betterrtcooldownchance=15.00

disablespotscount=0
disablespotschance=375.00

addrollscount=0
addrollschance=5.00

wishlistspotcount=0
wishlistspotchance=22.50

wishprotectcount=0
wishprotectchance=700.00

pincount=0
pinchance=500.00

hundredcounter=0
while(hundredcounter<tryinput):
  num1 = float(random.randint(1, 10000))
  qual=quality*num1

  
  
  if(num1<=additionalrollschance+10000):
    additionalrollscount+=1
    num2=random.randint(1,100)
    if(num2 <= quantity):
      additionalrollscount+=1
  num1 = float(random.randint(1, 10000))
      
  if(num1<=kakerarewardchance*quality):
    kakerarewardcount+=1
    num2=random.randint(1,100)
    if(num2 <= quantity):
      kakerarewardcount+=1
  num1 = float(random.randint(1, 10000))
      
  if(num1<=betterrtcooldownchance*quality):
    betterrtcooldowncount+=1
    num2=random.randint(1,100)
    if(num2 <= quantity):
      betterrtcooldowncount+=1
  num1 = float(random.randint(1, 10000))
      
  if(num1<=disablespotschance*quality):
    disablespotscount+=1
    num2=random.randint(1,100)
    if(num2 <= quantity):
      disablespotscount+=1
  num1 = float(random.randint(1, 10000))
      
  if(num1<=addrollschance*quality):
    addrollscount+=1
    num2=random.randint(1,100)
    if(num2 <= quantity):
      addrollscount+=1
  num1 = float(random.randint(1, 10000))
      
  if(num1<=wishlistspotchance*quality):
    wishlistspotcount+=1
    num2=random.randint(1,100)
    if(num2 <= quantity):
      wishlistspotcount+=1
  num1 = float(random.randint(1, 10000))
      
  if(num1<=wishprotectchance*quality):
    wishprotectcount+=1
    num2=random.randint(1,100)
    if(num2 <= quantity):
      wishprotectcount+=1
  num1 = float(random.randint(1, 10000))
      
  if(num1<=pinchance*quality):
    pincount+=1
    num2=random.randint(1,100)
    if(num2 <= quantity):
      pincount+=1
  hundredcounter+=1


print(f"This is the result of {tryinput} tries with these quantity and quality settings\n")
print(f"Additional rolls: {additionalrollscount}\n")
print(f"Kakera reward: {kakerarewardcount}\n")
print(f"Better $rt cooldown: {betterrtcooldowncount}\n")
print(f"Disable spots: {disablespotscount}\n")
print(f"Added Perma rolls: {addrollscount}\n")
print(f"Added wishlist spots: {wishlistspotcount}\n")
print(f"Wish protect upgrade count: {wishprotectcount}\n")
print(f"Pin count: {pincount}\n")

  
  
  
