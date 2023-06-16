from users import *
from contacts import *
from moduels import *
from os import system
from validators import email_validation,password_validation
import colorama
from colorama import Fore, Style, Back

colorama.init(autoreset=True)
system("clear")

while True:
    contacts_dict = Contact.loading()
    users_dict = User.loading()

    print(Back.BLACK + Fore.RED + Style.BRIGHT + 
          "====================================================== Contact Manager ======================================================")
    print(Fore.BLUE + Style.BRIGHT + Back.GREEN + "\n1.Sign Up: ")
    print(Fore.BLUE + Style.BRIGHT + Back.WHITE + "2.LogIn:   \n")
    option = int(input(Fore.RED + "Optin: "))

    if option == 1 :
        username = input("\nEnter Username: ")
        password = input("\nEnter Password: ")
        signup(username, password)
        users_dict = User.loading()

    
    
    #Begingig of Login

    if option == 2 :
        
        contacts_dict = Contact.loading()
        users_dict = User.loading()
        
        
        contacts_dict = Contact.loading()
        users_dict = User.loading()        
        username = input("\n\nEnter your username: ")
        password = input("Enter your password: ")
        
        if login(username, password) :
            
            current_user_id = users_dict[username].get("user_id")
            
            while True:
            
            
                print("\n\n1. Show all contacts ")
                print("2. Creat new contact ")
                print("3. Remove a contact ")
                print("4. Edit contacts ")
                print("5. User account settings")
                print("6. Export Contacts to CSV.File")
                print("7. Import Contacts from CSV.File")
                print("8. Find Contacts from Email Address")
                print("\n\n")
                option = int(input("Option: ")) 
                print("\n")
                system('clear')
                
                #Beginig of (show all contacts)
                if option == 1: 
                    Contact.show_contacts(current_user_id)
                #End of (show all contacts)
                        
                #Beging of (Creat new contact)
                if option == 2:
                    name = input("Enter name: ")
                    email = input("Enter email: ")
                    if (email_validation(email)):
                        phone = input("Enter phone: ")
                        new_contact = Contact.add_contact(name, email, phone, users_dict[username].get("user_id"))
                        new_contact_dict = {
                
                            "name"  : new_contact.name,
                            "email" : new_contact.email,
                            "phone" : new_contact.phone,
                            "user_id" : new_contact.user_id
                        }
                        
                        
                        contacts_dict.update({new_contact.name : new_contact_dict})
                        print("test:  " , contacts_dict)
                        Contact.dumping(contacts_dict)
                        contacts_dict = Contact.loading()
                        print("Contacts Dict:", contacts_dict)
                    else:
                        print("Not a Valid Email !")
                    
                        
                if option == 3 :
                        
                    del_name = input("Enter Contact Name to Remove: ")
                        
                    if contacts_dict[del_name].get("user_id") == current_user_id and contacts_dict.get(del_name) is not None :
                        Contact.delet_contact(del_name)
                        print("\n=========================================  Removed Successfully  =========================================\n")
                    else:
                        print("\n=========================================  Not found  =========================================\n")      
                        
                        
                    
                if option == 4 :
                    edit_name = input("Enter name of the contact you want to edit: ")

                    if contacts_dict[edit_name].get("user_id") == current_user_id and contacts_dict.get(edit_name) is not None :
                            
                        #print("Old Name: " , contacts_dict.get(edit_name).name)
                        name = input("Enter new name: ")
                        #print("Old Email: " , contacts_dict.get(edit_name).name)
                        email = input("Enter new email: ")
                        #print("Old Phone: " , contacts_dict.get(edit_name).name)
                        phone = input("Enter new phone: ")

                        #print(new_contact.name)
                        #print(new_contact.email)
                        
                        Contact.edit_contact(edit_name, name, email, phone, current_user_id)
                        contacts_dict = Contact.loading()
                        print("\n=========================================  Edited Succesfully =========================================\n")
                        
                    else:
                        print("f{del_name} not found !") 
                
                if option == 5 :
                    
                    print("1. Edit Username")
                    print("2. Edit Password")  
                    print("3. Delete Acount")      
                    option = int(input("Option: "))
                    
                    if option == 1 :
                        
                        new_username = input("Enter new username: ")
                        User.modify_user(1,username,new_username,password,"",users_dict[username]["user_id"])

                    if option == 2 :
                
                        new_password = input("Enter new password: ")
                        User.modify_user(2, username, "", "",new_password,users_dict[username]["user_id"])
                    
                    if option == 3 :
                        User.modify_user(3, username, "","","",users_dict[username]["user_id"])
                
                
                if option == 6 :
                    
                    Contact.export_csv(username,current_user_id)
                    print("CSV file created successfully !")

                if option == 7 :
                    
                    csv_filename = username + ".csv"
                    Contact.import_csv(csv_filename, current_user_id)
                
                if option == 8 :
                    search_email = input("Enter Email Address: ")
                    Contact.search_contact_eamil(search_email, current_user_id)
                            
            
        else :
            print("Invalid username or password, try again...")
            break
