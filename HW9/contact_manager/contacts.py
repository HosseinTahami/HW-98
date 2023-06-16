from users import *
import os
import pickle
import csv

contacts_dict = {}

if os.path.getsize("contacts.pickle") > 0:
    with open("contacts.pickle", "rb") as pf :
        contacts_dict = pickle.load(pf)
class Contact :
    
    def __init__ (self,
                  name:str,
                  email:str,
                  phone:str,
                  user_id:str,
                  #note:str,
                  #categorie:str
                   ):
        
        self.name = name
        self.email = email
        self.phone = phone
        self.user_id = user_id
        #self.note = note
        #self.categorie = categorie
        
        
    @classmethod
    def add_contact(cls, name, email, phone, user_id):
        
        return cls(name, email, phone, user_id)
        

    
    def edit_contact(edit_name : str , new_name : str , new_email : str , new_phone : str , current_user_id):
        
        contacts_dict = Contact.loading()
        if Contact.repeat_contact is not None :
            new_contact = Contact.add_contact(new_name, new_email, new_phone, current_user_id)
            new_contact_dict = {
        
                "name"  : new_name,
                "email" : new_email,
                "phone" : new_phone,
                "user_id" : current_user_id

            }
            
            contacts_dict.update({new_name : new_contact_dict})
            Contact.dumping(contacts_dict)
            contacts_dict = Contact.delet_contact(edit_name)
            


    
    @staticmethod
    def delet_contact(del_name):
        contacts_dict = Contact.loading()
        contacts_dict.pop(del_name)
        contacts_dict = Contact.dumping(contacts_dict)




    @staticmethod
    def repeat_contact(name):
        if contacts_dict.get(name) is None :
            return True
        return False

    @staticmethod
    def loading():
        if os.path.getsize("contacts.pickle") > 0:
            with open("contacts.pickle", "rb") as pf :
                contacts_dict = pickle.load(pf)
                return contacts_dict
        contacts_dict = {}
        return contacts_dict

        
    @staticmethod
    def dumping(contacts_dict):
        with open("contacts.pickle", "wb") as pf :
            pickle.dump(contacts_dict,pf)
    
    
    @staticmethod
    def export_csv(username,user_id):
        filename = username + '.csv'
        with open(filename,'w') as csvfile:
            data = csv.DictWriter(csvfile, fieldnames=['name', 'email', 'phone'])
            data.writeheader()
            contacts_dict = Contact.loading()
            for contact in contacts_dict.values():
                if contact["user_id"] == user_id :
                    contact.pop("user_id")
                    data.writerow(contact)

    @staticmethod
    def import_csv(filename, user_id):
        with open(filename,'r') as csvfile:
            data = csv.DictReader(csvfile)
            contacts_dict = Contact.loading()
            for line in data:
                name = line["name"]
                email = line["email"]
                phone = line["phone"]
                new_contact = Contact.add_contact(name, email, phone,user_id)
                new_contact_dict = {

                    "name"  : new_contact.name,
                    "email" : new_contact.email,
                    "phone" : new_contact.phone,
                    "user_id" : new_contact.user_id
                }
                
                contacts_dict.update({new_contact.name : new_contact_dict})
                #print("test:  " , contacts_dict)
                Contact.dumping(contacts_dict)
                contacts_dict = Contact.loading()
    
    @staticmethod
    def search_contact_eamil(email, user_id):
        contacts_dict = Contact.loading()
        for contact in contacts_dict.values():
            if contact["email"] == email and contact["user_id"] == user_id:
                print("Name: ", contact["name"], " , ", "Phone: ", contact["phone"], " , " , "Email: ", contact["email"])
            else:
                print("Not Found")    
    
    @staticmethod
    def show_contacts(user_id):
        print("\n==============================================================  All Contacts  ==============================================================\n")
        contacts_dict = Contact.loading()
        c = 1
        for contact in contacts_dict.values() :
            if contact["user_id"] == user_id:
                print(c,"-","Name: ",contact["name"],"Email: " , contact["email"],"Phone: " ,contact["phone"])
                c += 1
        print("\n============================================================================================================================================\n")
        if c  == 1: 
            os.system('cls' if os.name == 'nt' else 'clear')
            print("==============================================================  No Contact  ==============================================================")