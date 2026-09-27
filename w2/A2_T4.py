print("Program starting.")
print("Estimate how many minutes you spent on programming...")
print()

a1_t1 = int(input("A1_T1: "))
a1_t2 = int(input("A1_T2: "))
a1_t3 = int(input("A1_T3: "))
a1_t4 = int(input("A1_T4: "))
a1_t5 = int(input("A1_T5: "))
a1_t6 = int(input("A1_T6: "))
a1_t7 = int(input("A1_T7: "))

total = a1_t1 + a1_t2 + a1_t3 + a1_t4 + a1_t5 + a1_t6 + a1_t7
average = total / 7
rounded_average = int(round(average, 0))

print()
print(f"In total you spent {total} minutes on programming.")
print(f"Average per task was {average:.2f} min and same rounded to the nearest integer {rounded_average} min.")
print()
print("Program ending.")