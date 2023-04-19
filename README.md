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

