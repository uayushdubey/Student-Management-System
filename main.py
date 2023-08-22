# Student Management System
studentdata_1 = []  # for list
studentdata_2 = []  # for tuple
studentdata_3 = []  # for dictionary

# global variables
dictionary = {}


# Function to add data
def add(name, branch, grade):
    # Each Variable assigned over here are of local scope
    list = [name, branch, grade]
    studentdata_1.append(list)
    tuple = (name, branch, grade)
    studentdata_2.append(tuple)
    dictionary = {'name': name, 'branch': branch, 'grade': grade}
    studentdata_3.append(dictionary)
    return True


# Function to remove
# Type of Function Fruitful
def remove(roll):
    # Each Variable assigned over here are of local scope
    index = roll - 1
    k = studentdata_1.pop(index)
    studentdata_2.pop(index)
    studentdata_3.pop(index)
    return k


# Function to display
def display():
    # Each Variable assigned over here are of local scope
    print("Each Student variable has same data element or key:value pair")
    for i in studentdata_1:
        print(i)

    return 1


# Function to Update
# Type of function is non-fruitful
def change(roll):
    # Each Variable assigned over here are of local scope
    index = roll - 1
    print("What you want to change?\n1.Name\n2.Branch\n3.Grade")
    choice = int(input("Enter: "))
    if (choice == 1):
        list = studentdata_1[index]
        list[0] = input("Enter New name: ")
        a = list[0]
        studentdata_2.pop(index)
        new_tuple = (a, list[1], list[2])
        studentdata_2.insert(index, new_tuple)
        new = {'name': list[0]}
        dictionary.update(new)
    elif (choice == 2):
        list = studentdata_1[index]
        list[1] = input("Enter New branch: ")
        a = list[1]
        studentdata_2.pop(index)
        new_tuple = (list[0], a, list[2])
        studentdata_2.insert(index, new_tuple)
        new = {'branch': list[1]}
        dictionary.update(new)
    elif (choice == 3):
        list = studentdata_1[index]
        list[2] = input("Enter New name: ")
        a = list[2]
        studentdata_2.pop(index)
        new_tuple = (list[0], list[1], a)
        studentdata_2.insert(index, new_tuple)
        new = {'grade': list[2]}
        dictionary.update(new)
    else:
        pass


if __name__ == "__main__":
    while True:
        print("Enter operations for\n1.Add name\n2.Remove name\n3.Display\n4.Update")
        choice = int(input("Enter: "))
        if (choice == 1):
            add(input("Enter Name: "), input("Enter Branch: "), input("Enter Grade: "))
        elif (choice == 2):
            roll = int(input("Enter Roll Number of Student: "))
            print(remove(roll))
        elif (choice == 3):
            display()
        elif (choice == 4):
            roll = int(input("Enter Roll Number: "))
            change(roll)
        else:
            break
