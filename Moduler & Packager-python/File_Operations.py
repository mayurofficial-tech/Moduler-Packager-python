import os

path="C://Users//MAYUR MAKVANA//OneDrive//Desktop//files"
def create_new_file():
    print("=" * 30)
    new_file=input("Enter new file name:-")
    with open(path+"//"+new_file,"w") as f:
        print("File Created Successfully!")
    print("=" * 30)

def write_to_file():
    print("=" * 30)
    file_name=input("Enter file name:-")
    if os.path.exists(file_name):
        with open(path + "//" + file_name, "w") as f:
            content = input("Enter date to write:-")
            f.write(content)
    else:
        print("File Not Found,first Create this file")
    print("=" * 30)

def read_from_file():
    print("=" * 30)
    file_name=input("Enter file name:-")
    if os.path.exists(file_name):
        with open(path + "//" + file_name, "r") as f:
            content = f.read()
            print("File Content:-\n",content)
    else:
        print("File Not Found,first Create this file")
    print("=" * 30)

def append_to_file():
    print("=" * 30)
    file_name=input("Enter file name:-")
    if os.path.exists(file_name):
        with open(path + "//" + file_name, "a") as f:
            content = input("Enter date to write:-")
            f.write(content)
    print("=" * 30)
def main():
    while True:
        print("Welcome to File Operations!")
        print("1. Create a New File")
        print("2. Write to a File")
        print("3. Read from a File")
        print("4. Append to a File")
        print("5. Back to Menu")
        ch=int(input("Enter your choice:-"))
        if ch == 1:
            create_new_file()
        elif ch == 2:
            write_to_file()
        elif ch == 3:
            read_from_file()
        elif ch == 4:
            append_to_file()
        elif ch == 5:
            break
        else:
            print("Invalid Choice")

if __name__ == '__main__':
    main()