# module to import into the program
import re
import json

# Contact Dictionary
contact_dict = {}


# function to add a new contact to the management system
def add_contact():
        email_address = input("Enter the email address of the new contact: ")
        if re.search(r"[A-za-z0-9._%t-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", email_address):
            print("The email address has been added to the contact system")
        else:
            print("Email address isn't valid. Please enter a valid email")

        name = input("Enter the name of the contact: ")

        
        phone_number = input("Enter the phone number of the contact: (XXX-XXX-XXXX)")
        if re.search(r"\d{3}-\d{3}-\d{4}", phone_number):
            print("Phone number has been entered in the contact info")
        else:
            print("Phone number isn't valid. Enter the properly formatted phone number!")
                
        home_address = input("Enter your home address: ")
            
        additional_notes = input("Do you want to add additional notes? (Yes/No) ")
        if additional_notes.lower() == "yes":
           notes = input("Enter additional notes: ")
        elif additional_notes.lower() == "no":
            print("No additional notes added!")
        else:
            print("You did not enter a valid option, try again!")
            
        contact_dict[email_address] = {
            "Unique ID": email_address,
            "Additional Info": {
                "Name": name,
                "Phone Number": phone_number,
                "Email": email_address,
                "Home Address": home_address,
                "Additional Notes": notes
                }
            }
        print(f"\n{email_address} has been added to the list")
        print("\nContact: ", contact_dict[email_address], sep="\n")

# function to edit existing contact
def edit_contact():
    email_address = input("\n Please enter the Unique ID (Email) you wish to edit: ")
    while True:
        if email_address in contact_dict:
            print("""
                    1. Edit name
                    2. Edit phone number
                    3. Edit email
                    4. Edit home address
                    5. Edit Notes
                    6. Back to main menu
                """)
            action = input("Enter a valid option: ")
            
            if action == "1":
                change_name = input("Please edit the name: ")
                contact_dict[email_address]["Additional Info"]["Name"] =  change_name
                print(f"Your name has been changed to {change_name}")
            elif action == "2":
                change_number = input("Please edit the phone number: ")
                contact_dict[email_address]["Additional Info"]["Phone Number"] = change_number
            elif action == "3":
                change_email = input("Please edit the email: ")
                contact_dict[email_address]["Additional Info"]["Email"] = change_email
            elif action == "4":
                change_address = input("Please edit the home address: ")
                contact_dict[email_address]["Additional Info"]["Home Address"] = change_address
            elif action == "5":
                change_notes = input("Please edit the notes: ")
                contact_dict[email_address]["Additional Info"]["Additional Notes"] = change_notes
            elif action == "6":
                break
            else:
                print("Please enter a valid option!")
        else:
            print("That email is not a unique ID, why not create a new one?")
            break

# function to delete a contact and all information associated with it
def delete_contact():
    email_address = input("Enter the Unique ID (Email) you wish to delete: ")
    
    if email_address in contact_dict:
        delete_address = input("Do you wish to delete this contact? (Yes/No) ")
        if delete_address.lower() == "yes":
            del contact_dict[email_address]
            print(f"{email_address} was deleted from the system.")
        else:
            print("Contact was not deleted.")
    else:
        print("There is no such emails in the system.")

# function to search for a specific contact
def search_contact():
    email_address = input("Please enter the Unique ID (Email) you wish to search for: ")
    while True:
        if email_address in contact_dict:
            print("Contact:", contact_dict)
            break
        else:
            print("There is no contacts in the system")
            break

# function to display a list of all the contacts
def display_contact():
    if contact_dict:
        print("Your current contact list:", contact_dict, sep="\n")
    else:
        print("No contacts in the current list")

# function to export the contacts to a file
def export_contact():
    with open("unique_id.txt", "w") as file:
        json.dump(contact_dict, file)
        print("File has been exported!")

# function to import contacts to a file
def import_contact():
    global contact_dict
    try:
        with open("unique_id.txt", "r") as file:
            contact_dict = json.load(file)
            print("Contacts have been imported")
            print("\n" , contact_dict, sep="\n")
    except FileNotFoundError:
        print("That file has not been created!")

    

# function that controls the main menu 
def main_menu():
    while True:
        print("""
                |====Welcome to the Contact Management System====|
                    
                    Menu:
                        1. Add a new contact
                        2. Editing an existing contact
                        3. Delete a contact
                        4. Search for a contact
                        5. Display all contacts
                        6. Export contacts to a text file
                        7. Import contacts from a text file
                        8. Quit Application
        
            """)
        
        choice = input("Please make a valid choice in the menu options: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            edit_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            display_contact()
        elif choice == "6":
            export_contact()
        elif choice == "7":
            import_contact()
        elif choice == "8":
            print("Application is closing down...")
            break
        else:
            print("Invalid Choice has been selected, try again!")

main_menu()