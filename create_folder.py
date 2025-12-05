import os 
folder="journal"


#create the folder if co
try:
    os.mkdir("folder")
    print("Folder is created.")
#
except Exception as a:
    print(f"{a}")


file= input("Enter the text file name: ")
os.makedirs("folder", exist_ok = 1)
print("folder is ready")

file_path= os.path.join("folder",file)
try:
    text=input("Enter the text which you want to write: ")
    with open(file_path,'w') as file:
        file.write(text)
        os.system('cls' if os.name =='nt'else "clear")
    print(f"File '{file_path}' created successfully.")

except IOError as a:
    print(a)

