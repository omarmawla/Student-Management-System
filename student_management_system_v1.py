#Welcome message

print("   Welcome to the Student Management System ")

names = []
marks = []

for i in range(5):
    name = input(f"Enter the name of student {i+1}: ")
    mark = int(input(f"Enter the mark of {name}: "))
    names.append(name)
    marks.append(mark)
#menu
menu = [
    "1. Show All Students",
    "2. Add Student",
    "3. Search Student",
    "4. Update Student",
    "5. Delete Student",
    "6. Exit"
]    

while True:
    print("\n========== Student Management System ==========")
    for item in menu:
        print(item)

        choice = input("What option would you like to choose? ")

        if choice == '1':
            print("\nStudent List:")
            print("----------------")
            for i in range(len(names)):
                print(f"{names[i]}: {marks[i]}")

        elif choice =='2':
             new_name = input("Enter the student name you want to add: ")
             new_mark = int(input(f"Enter the mark of {new_name}: "))
             names.append(new_name)
             marks.append(new_mark)
             print(f"{new_name} has been added with a mark of {new_mark}.")

        elif choice == '3':
            search_name = input("Enter the student name you want to search: ")
            if search_name in names:
                i = names.index(search_name)
                print(f"{search_name} has a mark of {marks[i]}.")
            else:
                print(f"{search_name} is not found in the student list.")
            
                
        elif choice == '4':
            update_name = input("Enter the student name you want to update: ")
            if update_name in names:
                i = names.index(update_name)
                new_mark = int(input(f"Enter the new mark for {update_name}: "))
                marks[i] = new_mark
                print(f"{update_name}'s mark has been updated to {new_mark}.")
            else:
                print(f"{update_name} is not found in the student list.")

        elif choice == '5':
            delete_name = input("Enter the student name you want to delete: ")
            if delete_name in names:
                i = names.index(delete_name)
                names.remove(delete_name)
                marks.pop(i)
                print(f"{delete_name} has been deleted from the student list.")
            else:
                print(f"{delete_name} is not found in the student list.")     


        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break        
        else:
            print("Invalid choice. Please select a valid option from the menu.")

    