# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# size = size.upper()
# add_pepperoni = add_pepperoni.upper()
# extra_cheese = extra_cheese.upper()
bill = 0

if size == "S" or size == "s":
	bill += 15
	print(f"Current bill: ${bill}")
elif size == "M" or size == "m":
	bill += 20
	print(f"Current bill: ${bill}")
elif size == "L" or size == "l":
	bill += 25
	print(f"Current bill: ${bill}")

if add_pepperoni == "Y" or add_pepperoni == "y":
	if size == "S" or size == "s":
		bill += 2
	else:
		bill += 3

if extra_cheese == "Y" or extra_cheese == "y":
	bill += 1

print(f"Your final bill is: ${bill}")