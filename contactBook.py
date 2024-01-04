#contact book
contactList = []
class Contact:
    def __init__(self):
        self.name = ''
        self.phone = 0
        self.email = ''
        self.address = ''

    #add new conatcts with their details
    def addContact(self):
        self.name = input("Enter name : ")
        self.phone = int(input("Enter phone number : "))
        self.mail = input("Enter email : ")
        self.address = input("Enter address : ")
        contactList.append([self.name, self.phone, self.mail, self.address])

    #view the list of all saved contacts
    def viewContacts(self):
        savedList = []
        for i in range(len(contactList)):
            savedList.append([contactList[i][0],contactList[i][1]])

        print("List of all saved names and their phone numbers.")
        print(savedList)


    #search by name or phone number
    def searchContact(self):
        ch = int(input("Search by name or function  - Enter 1 for name and 2 for phonenumber : "))
        if ch == 1:
            flag = 0
            nm = input("Enter name to search : ")
            for i in contactList:
                if i[0] == nm:
                    flag = 1
                    print("Contact details found!!")
                    print(f"Name : {i[0]}\nPhone number : {i[1]}\nEmail : {i[2]}\nAddress : {i[3]}")
                    break
            if flag == 0:
                print("No contact details found!!")

        elif ch == 2:
            flag = 0
            ph = int(input("Enter phone number to search : "))
            for i in contactList:
                if i[1] == ph:
                    flag = 1
                    print("Contact details found!!")
                    print(f"Name : {i[0]}\nPhone number : {i[1]}\nEmail : {i[2]}\nAddress : {i[3]}")
                    break
            if flag == 0:
                print("No contact details found!!")


    #update contact
    def updateContact(self):
        nm = input("Enter student name to update : ")
        flag = 0
        for i in contactList:
            if i[0] == nm:
                flag = 1
                i[0] = input("Enter updated name : ")
                i[1] = int(input("Enter updated phone number : "))
                i[2] = input("Enter updated email : ")
                i[3] = input("Enter updated address : ")
                print("Contact details updated!!")
                break
        if flag == 0:
                print("No contact details found!!")


    #delete the contact
    def deleteContact(self):
        nm = input("Enter student name whose details has to be deleted : ")
        flag = 0
        for i in contactList:
            if i[0] == nm:
                flag = 1
                contactList.remove(i)
                print("Contact deleted successfully.")
                break
        if flag == 0:
            print("No such contact found.")

c = Contact()
while(True):
    print("-"*50,"MENU","-"*50)
    print("1. ADD CONTACT")
    print("2. VIEW CONTACT LIST")
    print("3. SEARCH CONTACT")
    print("4. UPDATE CONTACT")
    print("5. DELETE CONTACT")
    print("-"*105)
    ch = int(input("Enter your choice : "))
    if ch == 1:
        c.addContact()
    elif ch == 2:
        c.viewContacts()
    elif ch == 3:
        c.searchContact()
    elif ch == 4:
        c.updateContact()
    elif ch == 5:
        c.deleteContact()
    else:
        print("Invalid choice")

    cnt = input("Do you want to continue (y/n)?")
    if cnt.lower() == 'n':
        break
            
        

                
        
        
