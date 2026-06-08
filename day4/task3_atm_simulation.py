balance=5000

print("welcome to python bank ATM")
print("1.check balance")
print("2.withdraw amount")

choice =int(input("enter choice(1-2):"))
if choice==1:
      print(f"your balance:{balance}")

elif choice==2:
      withdraw_amount=float(input("enter amount to withdraw:"))
      if withdraw_amount<=balance:
              balance=balance-withdraw_amount  
              print("transaction successful")
              print(f"remaining balance:{int(balance)}")
      else:
            print("insufficent balance")
else:
      print("invalid choice")

