import math

print("Trigonometric calculator ")
user_angle = float(input("Please Enter the degrees of the angle: "))
rad = math.radians(user_angle)

print(f"sin({user_angle}) = {round(math.sin(rad), 4)}")
print(f"cos({user_angle}) = {round(math.cos(rad), 4)}")
print(f"tan({user_angle}) = {round(math.tan(rad), 4)}")