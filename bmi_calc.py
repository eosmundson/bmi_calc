#!/usr/bin/python3

def main():
    weight = float(input("Enter your weight(lbs): "))
    height = float(input("Enter your height(inches): "))
    age = int(input("What's your age?: "))
    sex = ask_gender()
    
    bmi = float(calc_bmi(weight, height))
    print(f"\nYour BMI is {bmi:.1f}")
    
    bfp = calc_body_fat(age, bmi, sex)
    print(f"\nYour body fat percentage is {bfp:.1f}%")
    
    
def calc_bmi(weight, height):
    return 703 * (weight / (height ** 2))
    
    
def calc_body_fat(age, bmi, sex):
    if sex == "M":
        bfp = float((1.20 * bmi) + float((0.23 * age)) - 16.2)
        return bfp
    if sex == "F":
        bfp = float((1.20 * bmi) + float((0.23 * age)) - 5.4)
        return bfp
    
    
def ask_gender():
    sex = ""
    while sex != "M" or sex != "F":
        sex = input("What's your gender (M or F)?: ")
        if sex == "M" or sex == "F":
            return sex
        else:
            continue
    
    
if __name__ == "__main__":
    main()