from pathlib import Path
def readfileandfolder():
    path=Path('')
    items=list(path.rglob('*'))
    print("your files are:")
    for i, items in enumerate(items):
        print(f"{i+1}:{items}")

def createfile():
    try:
        readfileandfolder()
        name=input("enter name of your file:")
        p=Path(name)
        if not p.exists():
           data=input("enter data to enter:")
           with open(p,"w") as f:
            f.write(data)
            print(f"File Created Successfully")
        else:
            print("this file already exists")
        
    except Exception as err:
        print(f"error occured as {err}")
def readfile():
    try:
        readfileandfolder()
        name=input("enter name of file:")
        p=Path(name)
        if  p.exists() and p.is_file():
          with open(name,"r") as f:
           print(f.read())
           print("File read Successfully")
        else:
            print("file does not exist")
    except Exception as err:
        print(f"error occured as {err}")
def updatefile():
    try:
        readfileandfolder()
        name = input("Enter name of the file: ")
        p = Path(name)

        if p.exists() and p.is_file():

            print("Choose 1 for renaming the file")
            print("Choose 2 for overwriting file")
            print("Choose 3 for appending file")

            choice = int(input("Enter option: "))

            if choice == 1:
                new_name = input("Enter new file name: ")
                p.rename(new_name)
                print("File renamed successfully.")

            elif choice == 2:
                data = input("Enter new data to overwrite: ")
                with open(p, "w") as f:
                    f.write(data)
                print("File overwritten successfully.")

            elif choice == 3:
                data = input("Enter data to append: ")
                with open(p, "a") as f:
                    f.write(" " + data)
                print("File appended successfully.")

            else:
                print("Invalid choice.")

        else:
            print("File does not exist.")

    except Exception as err:
        print(f"Error occurred: {err}")
def delfile():
    try:
        readfileandfolder()
        name = input("Which file to delete: ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(p)
            print("File removed successfully.")
        else:
            print("File does not exist.")

    except Exception as err:
        print(f"Error occurred: {err}")
print("Enter 1 for creating a File.")
print("Enter 2 for reading a File")
print("Enter 3 for updating a File")
print("Enter 4 for deleting a File")
check=int(input("Enter your response:"))
if check==1:
    createfile()
if check==2:
    readfile()
if check==3:
   updatefile()





    





