from datetime import datetime
DISCOUNT_RATE=.1
TAX_RATE=.06
today=datetime.now()
dow=today.weekday()
subtotal=float(input("enter the subtotal:"))
print(f"Total order {subtotal}")
discount=0
if dow==2 or dow==3 or dow==4:
  if subtotal > 50:
   discount=subtotal * DISCOUNT_RATE
  print(f"Discount {discount}") 
else:
  short=50-subtotal
  print(f"you can get a discount by ordering {short} more.")
subtotal -=discount
tax=subtotal * TAX_RATE
total=subtotal + tax

print(f"Subtotal {subtotal}")
print(f"Tax {tax}")
print(f"Total Due {total}")