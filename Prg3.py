'''num = -3
if (num < 0):
    print("Negative is 0")
elif (num > 0):
    print("Positive")
else:
    print("out of if else")'''

savingAmt = 1000
withdrawAmt = int(input("Enter the Amount to withdraw:"))
if(withdrawAmt > savingAmt):
    print("Insufficient balance")
else:
    savingAmt = savingAmt - withdrawAmt
    print("Account balance is :" +str(savingAmt))