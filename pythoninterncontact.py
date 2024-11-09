cb=[]
while True:
    name=input("enter the name")
    num=int(input("enter the number"))
    email=input("enter the email id")
    Address=input("enter the address")
    entry=[name,num,email,Address]
    cb.append(entry)
    ask=input("Do you want to add to contacts?")
    if ask.lower()!="yes":
        break
for i in range(0,len(cb)):
    for j in cb[i]:
        print(j)
    print(" ")
def search_contacts():
    search_term=input("Enter the name or number to search")
    found=False
    for entry in cb:
        if entry[0].lower()==search_term.lower() or str(entry[1])==search_term:
            print("Contact found")
            print(f"""
                      {entry[0]}
                      {entry[1]}
                      {entry[2]}
                      {entry[3]}""")
            asks=input("Do you want to update this contact?")
            if asks.lower()=="yes":
                entry[0]=input("enter new name(leave blank to keep the current):")or entry[0]
                new_num=input("enter new number(leave blank to keep current):")
                if new_num:
                    entry[1]=int(new_num)
                entry[2]=input("enter new email id (leave blank to keep current):") or entry[2]
                entry[3]=input("enter new address (leave blank to keep current):")or entry[3]
                print("contact updates successfully")
            elif asks.lower()=="delete":
                cb.remove(entry)
            for i in range(0,len(cb)):
                for j in cb[i]:
                    print(j)
            found=True
            break
        if not found:
            print("contact not found.")
search_contacts()
        
    

        

