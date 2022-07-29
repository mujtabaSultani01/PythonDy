print("Hello World")

base = 14
height = 10

area = 1/2 * (base * height)

print("Rectangle area is: ", area)

num = input("Pleas! Enter a number: ")
num = int(num)

if(num%2 == 0):
    print("Your inserted number is even.")

else:
    print("Your inserted number is odd.")

indian = ["Samosa","daal","naan"]
italian = ["Pasta", "Pizza", "Pot Sticker"]
Chiness = ["egg role", "risotto", "fried rice"]

dish = input("Type your favorite dish to till you the country: ")

if dish in indian:
     print("You choosed indian dish.")
elif dish in italian:
     print("You choosed italian dish.")
elif dish in Chiness:
     print("You choosed Chiness dish.")
else:
     print("Based on little knowledge I have, I don't know which dish this is! ", dish)


