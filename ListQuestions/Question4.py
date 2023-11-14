# Find sum of Number in Python List
print("____ Question No 3 ________")
print("------ Sum of Number in list ---------")
print("Start entering the list Press 000 if List is Created ")
print("---------------------------------------")

new_List = []
while True:
    input_Values = int(input("Enter the Number in list and Press 000 for Exit:  "))

    if input_Values == 000:
        break
        print("List is Created")

    new_List.append(input_Values)

print(new_List)


def sumList():
    sumValues = 0
    for number in new_List:
        sumValues += number
    print("Sum of Values are:", sumValues)    

sumList()
