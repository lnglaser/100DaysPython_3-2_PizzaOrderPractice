# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if size == "S" or "s":
	bill += 15
elif size == "M" or "m":
	bill += 20
elif size == "L" or "l":
	bill += 25
else:
	print("Invalid selection")

if add_pepperoni == "Y" or "y":
	if size == "S" or "s":
		bill += 2
	else:
		bill += 3

if extra_cheese == "Y" or "y":
	bill += 1

print(f"Your final bill is: ${bill}")