# Python Coursework 1

## Task

A restaurant has requested a program that will allow customers
to order food from their menu. The menu has four items: burger, 
pizza, fries, and drink, each with their respective prices. 
The program needs to implement five functions to provide different 
functionalities, such as calculating the total price of the order, 
checking for a discount, and generating a summary of the order 
with the final price paid.

This coursework is broken up into 5 functions. You may notice 
none of them are complete. It is your job to get the Restaurant 
Menu Ordering System up and running, by writing each of these 5 
functions. Don't stress we'll take them one at a time.

(OK stress a little no one can order their food at the moment!)

### Function 1 - `getTotalPrice`
This function takes a list of items and returns the total price of those items.
The list contains strings of the items the customer wants to order.

### Function 2 - `getOrderString`
This function takes a list of items and returns a string of the order.
The list contains strings of the items the customer wants to order.

### Function 3 - `checkDiscount`
This function takes a list of items and returns True if the order is 
eligible for a discount. The discount applies if the order contains 
at least 3 items and at least one of them is a burger.

### Function 4 - `getDiscountPrice`
This function takes a list of items and returns the total price with the discount applied. The discount applies if the order contains at least 3 items and at least one of them is a burger. The discount is 10% off the total price

### Function 5 - `getOrderSummary`
This function takes a list of items and returns a string with the order summary. The string should include the total price of the order, any discount applied, and the final price paid.

## Testing

Once you have written your solutions test them using `pytest`

To start all the tests should fail, and you should see the following:

```
$ pytest

==================== short test summary info ====================
FAILED test_coursework.py::test_getTotalPrice - AssertionError: assert None == 8.98
FAILED test_coursework.py::test_getOrderString - AssertionError: assert None == 'burger, fries'
FAILED test_coursework.py::test_checkDiscount - AssertionError: assert None == False
FAILED test_coursework.py::test_getDiscountPrice - AssertionError: assert None == 9.87
FAILED test_coursework.py::test_getOrderSummary - AssertionError: assert None == 'Total price: $8.98\nFinal price: $8.98'
======================= 5 failed in 0.04s =======================
```

