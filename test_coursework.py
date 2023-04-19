from coursework import *

# Unit Test 1: getTotalPrice
# Test that getTotalPrice returns the correct price for a list of items
def test_getTotalPrice():
    assert getTotalPrice(["burger", "fries"]) == 8.98
    assert getTotalPrice(["pizza", "drink"]) == 10.98
    assert getTotalPrice(["burger", "pizza", "fries", "drink"]) == 19.96

# Unit Test 2: getOrderString
# Test that getOrderString returns the correct string for a list of items
def test_getOrderString():
    assert getOrderString(["burger", "fries"]) == "burger, fries"
    assert getOrderString(["pizza", "drink"]) == "pizza, drink"
    assert getOrderString(["burger", "pizza", "fries", "drink"]) == "burger, pizza, fries, drink"


# Unit Test 3: checkDiscount
# Test that checkDiscount returns the correct boolean for a list of items
def test_checkDiscount():
    assert checkDiscount(["burger", "drink"]) == False
    assert checkDiscount(["burger", "fries", "drink"]) == True
    assert checkDiscount(["burger", "burger", "fries", "drink"]) == True
    assert checkDiscount(["burger", "pizza", "fries", "drink"]) == True
    assert checkDiscount(["pizza", "pizza", "fries", "drink"]) == False

# Unit Test 4: getDiscountPrice
# Test that getDiscountPrice returns the correct price for a list of items with discount applied
def test_getDiscountPrice():
    assert getDiscountPrice(["burger", "fries", "drink"]) == 9.87
    assert getDiscountPrice(["burger", "burger", "fries", "drink"]) == 15.26
    assert getDiscountPrice(["burger", "pizza", "fries", "drink"]) == 17.96
    

# Unit Test 5: getOrderSummar
# Test that getOrderSummar returns the correct order summary
def test_getOrderSummary():
    assert getOrderSummary(["burger", "fries"]) == "Total price: $8.98\nFinal price: $8.98"
    assert getOrderSummary(["pizza", "drink"]) == "Total price: $10.98\nFinal price: $10.98"
    assert getOrderSummary(["burger", "pizza", "fries", "drink"]) == "Total price: $19.96\nDiscount applied: $2.00\nFinal price: $17.96"
    assert getOrderSummary(["burger", "burger", "burger"]) == "Total price: $17.97\nDiscount applied: $1.80\nFinal price: $16.17"