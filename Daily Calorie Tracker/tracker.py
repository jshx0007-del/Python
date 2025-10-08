# Project: Daily Calorie Tracker
# Name: Janvi Sehrawat
# Date: 05-10-2025
# Description: This is a mini project to track daily calories intake by the user. 

print("Welcome to the Daily Calorie Tracker!🎉")
print("\nThis tool helps you log your meals, calculate total calories and\n average calories per meal, compare them to your daily limit.")

# Task 2: Input & Data Collection

meal = [] #This is to store meal names
calories = [] #This is to store calorie amounts


num_meals = int(input("How many meals you want to register today? "))

for i in range(num_meals):
    meal_name = input(f"\nEnter the name of your meal {i+1}: ")
    calorie_amount = float(input(f"\nEnter the number of calories in {meal_name}: "))
    meal.append(meal_name)
    calories.append(calorie_amount)

# Task 3: Calorie Calculations

total_calories = sum(calories)
average_calories = total_calories / len(calories)
daily_limit = float(input("\n Enter your daily calories limit: "))

# Task 4: Exceed Limit Warning if limit is exceeded

if total_calories>daily_limit:
    status = "⚠️ You have exceeded your daily calorie limit!!"
else:
    status = "✅ You are within your daily calories limit. Great Job!!"

# Task 5: Output

print("\n ----- Daily Calorie Summary -----")
print("\n Meal Name\tCalories")
print("----------------------------------")
for meal, cal in zip(meal, calories):
    print(f"{meal}\t\t{cal}")
print("------------------------------------")
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{average_calories: }")
print(status)
