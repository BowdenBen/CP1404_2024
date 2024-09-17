"""
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount
 is displayed on the screen.
"""

"""
Get number of items
    check number is greater than 0
    display number of items
    ask for price of each items
        if items total more than $100 apply 10% discount
    display total
"""

number_of_items = int(input("Enter the number of items: "))
while number_of_items > 0:
    for i in range(1, number_of_items + 1):
        price = float(input("Price of item: $"))
        total_price =+ price
        if total_price >= 100:
            new_total_price = total_price * 0.9
        else:
            new_total_price = total_price
        print(f"Total price for {number_of_items} items is ${new_total_price:.2f}")
print("Thankyou and please come again")

