# Find Maximum and Minimum of two numbers in Python

print("____ Question No 3 ________")
print("------ Sum of Number in list ---------")
print("Start entering the list Press 000 if List is Created ")
print("---------------------------------------")

new_List = []
while True:
    input_values = int(input("Enter the Number in List and Press 000 for Exit:  "))

    if input_values == 000:
        break
    print("List is Created")

    new_List.append(input_values)

print(new_List)


def maxNum():
    maxnumber = 0
