height = eval(input("Enter you height (in meters):"))
weight = eval(input("Enter your weight (in kg):"))

BMI = weight/(height**2)

if BMI < 18.5:
    print("You are under weight")
elif 18.5<=BMI<=24.9:
    print("You have normal weight")
elif 25<=BMI<=29.9:
    print("You are overweight")
elif BMI>=30:
    print("You are obese")
else:
    print("Cannot be classified")
print("BMI is ",BMI)
