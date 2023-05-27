square_meters = float(input("Enter square meters: "))
number_of_boxes = int(input("Enter the number of cans of paint: "))
square_meters_per_box = 7

total_paint = number_of_boxes * square_meters_per_box
diff = abs(square_meters - total_paint)

if total_paint >= square_meters:
    print(f"Martin will have {diff:.3f} extra liters of paint.")
else:
    print(f"Martin will need {diff:.3f} more liters of paint.")


