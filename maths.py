import math

# Input angle in degrees
angle_degrees = float(input("Enter an angle in degrees: "))

# Convert degrees to radians
angle_radians = math.radians(angle_degrees)

# Calculate and print sin, cos, and tan
print(f"sin({angle_degrees}°) = {math.sin(angle_radians)}")
print(f"cos({angle_degrees}°) = {math.cos(angle_radians)}")
print(f"tan({angle_degrees}°) = {math.tan(angle_radians)}")
