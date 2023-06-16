        
            username = input("\n\nEnter your username: ")
            password = input("Enter your password: ")
            
            if login(username, password) :
                
                current_user_id = users_dict[username].get("user_id")
                
                option = int(input("Option: ")) 

                #Beginig of (show all contacts)
                if option == 1: 