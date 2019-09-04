
checklist = []


def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)


def list_all_items():
    #index = 1
    for value in checklist:
        print(f"{value}")
        #input += 1

def uncheckedFunction(index):
    checklist[index] = checklist[index][1:len(checklist[index])]
    return checklist

def mark_completed(index):

    for list_item in checklist:
        checklist[index]  = "√" + checklist[index]
        return checklist
    # Add code here that marks an item as completed




def test():
    # Add your testing code here

    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))

    list_all_items()

    mark_completed(0)


def select(function_code):
    # Create item
    if function_code == "C":
        input_item = input("Input item:")
        create(input_item)

        # Print all items
    elif function_code == "P":
        list_all_items()


    # Read item
    elif function_code == "R":
        item_index = int(input("Index Number?"))
        print(read(item_index))

    # Remember that item_index must actually exist or our program will crash.

    elif function_code == "D":
        destroy(int(input("Index Number?")))


    elif function_code == "U":
        userinput = int(input("Enter index"))
        userstring = str(input("Replace with"))
        update(userinput, userstring)

    elif function_code == "M":

        userResponse = input("Enter C to check, Enter Z to uncheck")

        if userResponse == "C":
            list_all_items()
            checked = int(input(" wat index?"))
            mark_completed(checked)

        elif userResponse == "Z":
            list_all_items()
            checked = int(input("Index to uncheck"))
            uncheckedFunction(checked)

        else:
            print("you enter a wrong key")

    elif function_code == "Z":
        return False


    # Catch all
    else:
        print("Unknown Option")

    return True

#test()


running = True
while running:
    selection = input("Press C to add to list, R to Read from list and P to display list, M to check & unchec, U to update list, D to delete:  ")
    running = select(selection) #need explanation
