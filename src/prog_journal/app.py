from database import create_table, add_entry, get_entries

menu = """ Please select one of the following options: 
1) Add new entry for today 
2) view entries 
3) Exit 

Your selection: """

welcome = "Welcome to the programming diary"

def promp_new_entry():
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the data: ")
    add_entry(entry_content, entry_date)

def view_entries(entries):
    for entry in entries: 
        print(entry) 

print(welcome) 

create_table()

while (user_input := input(menu)) != "3":
    if user_input == '1':
        promp_new_entry()
    elif user_input == '2':
        view_entries(get_entries()) 
    else: 
        print('invalid option please try again!')

