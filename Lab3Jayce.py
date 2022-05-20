# Sample Run:

# Welcome to Jayce's Plant Store
# Buy 3 or more items to receive a 5% discount.
# Spend $50.00 or more and get 1 free plant.
# Price per plant is $5.00


# Enter quantity: 2

# You did not qualify for a discount.
# Shipping $ 5.00
# You owe $ 5.90

# Thank you for shopping!
# --------------------------------------------------

# Delcare Constant price_per_plant = 5.00
price_per_plant = 5.00


# Module main()

#     Declare Integer quantity
#     Declare Real unit_price
#     Declare Real total_price
#     Declare Real discount
#     Declare Integer free_plant

#     Call welcome_message()

#     Set item_name = get_item_name()
#     Set quantity = get_quantity()
#     Set unit_price = get_unit_price()

#     Set discount = get_discount(quanity, unit_price)
#     Set total_price = quanity * unit_price - discount

#     Set total_plants = get_quantity + free_plant

#     Call print_totals(discount, total_plants, total_price)

# End Module
def main():
    quantity = 0
    unit_price = 0.00
    total_price = 0.0
    discount = 0.0
    unit_total = 0
    free_plant = 0
    welcome_message()
    quantity = get_quantity()
    unit_price = get_unit_price()
    discount = get_discount(quantity, unit_price)
    total_price = quantity * unit_price - discount()
    get_unit_total = (quantity + get_free_plants)
    get_free_plants = (get_free(quantity, total_price)
    print_totals = (get_quantity, get_discount, unit_total, total_price)


# Function Void welcome_message()
# Welcome to Jayce's Plant Store
# Buy 3 or more items to receive a 5% discount.
# Spend $50.00 or more and get 1 free plant.
# Price per plant is $5.00
# End Function
def welcome_message():
    print("\nWelcome to Jayce's Plant Store!")
    print("\nIf you buy 3 or more plants you receive a 10% discount.")
    print("\nIf you spend more than 50.00 you get 1 free plant!")
    print("\n(Price per plant is $5.00.)")


# Function Integer get_quantity()
#     Delcare Integer qty
#     Display "Enter quantity: "
#     Input qty
#     Return qty
# End Function
def get_quantity():
    quantity = (int(input("Enter quantity: ")))
    return quantity


# Function Real get_unit_price()
#     Delcare Real price
#     Display "Enter unit price $ "
#     Input price
#     Return price
# End Function
void def get_unit_price():
    price = 5.00
    return price


# Function Real get_discount(quantity, unit_price)
#     If quantity >= 3 Then
#         Return quantity * price * .10
#     Else
#         Return 0
# End Function
def get_discount(quantity, price):
    if quantity >= 3:
        return quantity * price * .05
    else:
        return 0

def free_plants(total_price):
    if total_price >= 50:
        return 0
    else:
        return free_plants(total_price)

# Function Real total_plants(free_plants, quantity)
#     If total_price >= 50 Then
#         Return 0
#     Else
#         Return SHIPPING
# End Function
def unit_total(get_quantity, total_price):
    if total_price >= 50:
        return + 1
    else:
        return unit_total(get_quantity, total_price)


# Function Void print_totals(discount, shipping, total_price)
#     If discount > 0 Then
#         Display "You qualify for a discount of $ ", discount
#     Else
#         Display "You do not qualify for a discount"

#     Display "Shipping $ ", shipping
#     Diplsay "Please pay $ ", total_price + shipping

#     Display "Thank you for shopping!"

# End Function
def print_totals(discount, total_plants, total_price):
    if discount > 0:
        print("\nYou qualify for a discount of $ ", format(discount, ".2f"))
    else:
        print("\nYou do not qualify for a discount.")

    print("\nYour total # of plants is ", format(total_plants, ".2f"))
    print("\nYou owe $ ", format(total_price + ".2f"))



main()