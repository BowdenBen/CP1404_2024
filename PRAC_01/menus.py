"""
display menu
get choice
while choice != quit option
    if choice == first option
        do first task
    else if choice == <second option>
        do second task
    ...
    else if choice == <n-th option>
        do n-th task
    else
        display invalid input error message
    display menu
    get choice
do final thing, if needed
"""

name = input("Enter your name: ")
Menu = """ (H)ello
(G)oodbye
(Q)uit"""
choice = input(">>> ").upper()
while choice != Q:
    if choice == "H":
        print(f"Hello {name}")
        choice = input(">>> ").upper()
    elif choice == "G":
        print(f"Goodbye {name}")
        choice = input(">>> ").upper()
    else:
        print("Invalid input")
        choice = input(">>> ").upper()
print("Finished")
