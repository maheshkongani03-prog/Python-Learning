print("Welcome to the tip Calculator:")
Total_bill=float(input("What was the Total Bill:"))
tip=float(input("Hou much tip would you like to give?"))
total_people=float(input("How many people to split the bill:"))
pay_amnt=float((Total_bill+tip)/total_people)
print(f"Each Person should pay:{pay_amnt}")


