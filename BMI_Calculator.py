# BMI USING METRIC UNITS

import math

print("\tWelcome to my BMI Calculator")
print("-"*50)

menu = """
Select a number option.\n
[1]: convert weight to kg
[2]: convert height to cm
[3]: calculate bmi
[4]: exit\n
"""

weight_menu = """
Unit converting from:
[1]: stone
[2]: pounds\n
"""

height_menu = """
Unit converting from:
[1]: feet
[2]: metres
[3]: inches\n
"""

while True:
    try:
        user = int(input(menu))    
        if user == 1:
            print("\nOption one chosen\nconvert weight to KG")
            weight = int(input(weight_menu))
            if weight == 1:
                stone = float(input("\nWeight in stone: "))
                new_weight = stone*6.35
                print(f"You are {round(new_weight,0)}kg.")

            elif weight == 2:
                    pounds = float(input("\nWeight in pounds: "))
                    new_weight = pounds*2.205
                    print(f"You are {round(new_weight,0)}kg.")

            elif weight > 2:
                    print("\nNumber out of range. return to main menu and try again.")
    
            elif user == 2:
                print("\nOption 2 chosen\nconvert height to CM")
                height = int(input(height_menu))
            if height == 1:
                    inches = float(input("\nHeight in inches: "))
                    new_height = inches*2.54
                    print(f"You are {round(new_height,0)}cm.")

            elif height == 2:
                    metres = int(input("\nHeight in metres: "))
                    new_height = metres*100
                    print(f"You are {new_height}cm")

            elif height == 3:
                    feet = float(input("\nHeight in feet: "))
                    new_height = feet*30.48
                    print(f"You are {round(new_height,0)}cm")

            elif height > 3:
                    print("\nNumber out of range. return to main menu and try again.")

        elif user == 3:
            print("\nOption 3 chosen\nCalculate BMI.\n")
            weight = float(input("Weight in kg: "))
            height = float(input("Height in cm: "))
            bmi = (weight/(math.pow(height,2)))*10000
            print(f"\nYour BMI is {round(bmi,1)}.")

            if bmi >= 30:
                    print("Classed as Obese")

            elif bmi >= 25 and bmi <= 30:
                    print("Classed as Overweight")

            elif bmi >= 18.5 and bmi <= 25:
                    print("Classed as Normal")

            elif bmi == 0 and bmi <= 18.5:
                    print("Classed as underweight")

        elif user == 4:
            print("\nThank you for using my service.\nGoodbye.")
            break

    except ValueError:
        print("Invalid input. Try Again.")   
