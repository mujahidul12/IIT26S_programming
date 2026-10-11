
print("Program starting.\n")

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspection = int(input("Insert inspection point: "))

print()

valid = True

if start >= stop:
    print("Starting point value must be less than the stopping point value.")
    valid = False

if inspection < start or inspection > stop:
    print("Inspection value must be within the range of start and stop.")
    valid = False

if valid:
    print("First loop - inspection with break:")
    numbers = []
    for i in range(start, stop):
        if i == inspection:
            break
        numbers.append(str(i))
    print(" ".join(numbers))

    print("Second loop - inspection with continue:")
    numbers = []
    for i in range(start, stop):
        if i == inspection:
            continue
        numbers.append(str(i))
    print(" ".join(numbers))

print("\nProgram ending.")
