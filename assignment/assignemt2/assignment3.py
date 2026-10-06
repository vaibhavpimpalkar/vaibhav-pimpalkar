# Convert distant given in feet and inches into meter and centimeter.

feet=int(input("Enter feet : "))
inches=int(input("Enter inches : "))

# 1feet = 0.3048 meter
# 1inch = 2.54 centimeter 

feet_meter = feet * 0.3048 
inches_meter= (inches/12)*0.3048

print(" Feet in Meter : ",feet_meter )
print("inches in meter : ",inches_meter)
print("Total meter : ",feet_meter+inches_meter)

centimeter = feet*12*2.54
inch_cent= inches*2.54
print("feet in centi : ",centimeter)
print("inch in centi : ",inch_cent)

print("Total centimeter : ",inch_cent+centimeter)
