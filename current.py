units = int(input("Enter units consumed: "))
rate = 5
bill = units * rate

print("Units Consumed:", units)
print("Total Bill: ₹", bill)

nits = int(input("Enter units consumed: "))
rate = 5
bill = units * rate

if bill > 1000:
    discount = bill * 0.10
else:
    discount = 0

final_bill = bill - discount

print("Units Consumed:", units)
print("Total Bill: ₹", bill)
print("Discount Applied: ₹", discount)
print("Final Bill: ₹", final_bill)

