# Check if element exists in list in Python

new_list = []
print("------Question 2---------")
print("Start entering the list Press 000 if List is Created ")
print("----------------------")

while True:
    input_value = input("Enter the element in List:  ")
    if input_value == "000":
        print("List is Created")
        break
    new_list.append(input_value)
print(new_list)


def check():
    check_value = input("Enter the Value to be Checked:   ")
    if check_value in new_list:
        index = new_list.index(check_value)
        print(f"{check_value} is present in {new_list}")
        print(f"The index of {check_value} is {index}")
    else:
        print(f"{check_value} is present in {new_list}")


check()
