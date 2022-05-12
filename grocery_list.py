grocery_list = []

def add_to_list(new_item):
    grocery_list.append(new_item)
    print("Added! Your list has {} item(s).".format(len(grocery_list)))

def show_help():
    print("What should we pick up at the store?")
    print("""
    Enter 'DONE' to stop adding items.
    Enter 'HELP' for help.
    Enter 'SHOW' to show your current list.
    """)

def show_list():
        print("Here's your list:")
        number = 1
        for grocery in grocery_list:
            print("{}. ".format(number) + grocery.capitalize())
            number += 1

show_help()
while True:
    new_item = input("> ")

    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()
        continue
    
    add_to_list(new_item)

show_list()