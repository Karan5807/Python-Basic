# Find sum and average of List in Python

print("----- Question 3 --------")
print("------ Find sum and average of List in Python -------")
print("Start entering the list Press 000 if List is Created ")
print(" ----------------------------------------- ")

new_List = []
while True:
    input_value = int(input("Enter one values in List and press Enter: "))
    if input_value == 000:
        print("List is Created")
        break
    new_List.append(input_value)
print(new_List)


def sumAverage():
    sumValue = sum(new_List)
    length = len(new_List)
    averageValue = float(sumValue / length)
    print(f"The Sum of list is {sumValue}")
    print(f"The average of list is {averageValue}")


sumAverage()
