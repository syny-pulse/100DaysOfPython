principal = int(input("Enter loan amount> "))
rate = 0.05
for counter in range(10):
  amount = principal * (1 + rate) ** counter
  amount = round(amount,2)
  print(amount)
