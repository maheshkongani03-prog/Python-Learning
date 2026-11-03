weight = int(input("what is the weight:"))
height = int(input("What is the height:"))

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi<18.5:
    print("underweight")
elif 18.5<=bmi<25:
    print("normal weight")
else:
    print("over weight")
 

        