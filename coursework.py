# Restaurant Menu Ordering System Coursework

# A restaurant has asked you to build a program that allows customers to order food from a menu. 
# The menu contains the following items:

menu = {
    "burger": 5.99,
    "pizza": 8.99,
    "fries": 2.99,
    "drink": 1.99
}

# You will need to implement the following functions:

# Function 1 - getTotalPrice
# This function takes a list of items and returns the total price of those items.
# The list contains strings of the items the customer wants to order.

def getTotalPrice(order: list) -> int:
    # TODO
    pass

# Function 2 - getOrderString
# This function takes a list of items and returns a string of the order.
# The list contains strings of the items the customer wants to order.

def getOrderString(order: list) -> str:
    # TODO
    pass

# Function 3 - checkDiscount
# This function takes a list of items and returns True if the order is eligible for a discount.
# The discount applies if the order contains at least 3 items and at least one of them is a burger.

def checkDiscount(order: list) -> bool:
    # TODO
    pass

# Function 4 - getDiscountPrice
# This function takes a list of items and returns the total price with the discount applied.
# The discount applies if the order contains at least 3 items and at least one of them is a burger.
# The discount is 10% off the total price.

def getDiscountPrice(order: list) -> int:
    # TODO
    pass

# Function 5 - getOrderSummary
# This function takes a list of items and returns a string with the order summary.
# The string should include the total price of the order, any discount applied, and the final price paid.

def getOrderSummary(order: list) -> str:
    # TODO
    pass