
class Contact:
    def __init__(self,name,num,email):
        self.__name=name
        self.__number=num
        self.__email=email
    def EditContact(self,name,num,email):
        self.__name=name
        self.__number=num
        self.__email=email
        print("Contact updated successfully")



clist=[]
cname=[]
phlist=[]
elist=[]

while True:
    print("Enter\n1.Add new contact\n2.View contact list\n3.Edit contact\n4.Delete Contact\n5.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        name=input("Enter the name:")
        if name in cname:
            print("Contact Already Exist")
        else:
            num=int(input("Enter the phone number:"))
            email=input("Enter the email address:")
            new=Contact(name,num,email)
            clist.append(new)
            cname.append(name)
            phlist.append(num)
            elist.append(email)
    elif ch==2:
        c=1
        print("-----------Contact list-----------")
        for i in cname:
            print(c,".",i)
            c=c+1
    elif ch==3:
        name=input("Enter the contact name to edit:")
        if name in cname:
            idx=cname.index(name)
            name=input("Enter the name:")
            num=int(input("Enter the phone number:"))
            email=input("Enter the email address:")
            cname[idx]=name
            clist[idx].EditContact(name,num,email)
        else:
            print("Contact Dosent Exist")
    elif ch==4:
        name=input("Enter the contact name to delete:")
        if name in cname:
            idx=cname.index(name)
            clist.remove(clist[idx])
            cname.remove(cname[idx])
            elist.remove(elist[idx])
            print("Contact Deleted Successfully")
        else:
            print("Contact Dosent Exist")
    else:
        break