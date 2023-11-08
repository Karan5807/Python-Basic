# write a Python program to swap first and last element of the list.

# Create a List of Numbers
new_list = []
print("---- Question No 1 -----")
print("Start creating list Press 000 if List is created")
print("----------------------------")
while True:
    number_values = int(input("Enter the Number in list:   "))
    if number_values == 000:
        print("List is Created")
        break

    new_list.append(number_values)
print(new_list)


def change():
    temp = new_list[0]
    new_list[0] = new_list[-1]
    new_list[-1] = temp
    print(new_list)


change()
