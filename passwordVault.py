# PasswordVault (20180809) using OTP for Python 3.6 

# Import sys to exit the program, random to generate a master key and io to read and write to files
import sys
import random
import io

# Global list containing encrypted passwords and key 
passwords = []
keystring = ""

# masterPassword for the example text file containing passwords "hello" and "why" - I advise you choose better passwords for sites!
# masterPassword = ,B3U*]Y)gO'aC(B|gGx1

# Opens the password file and writes each password to the passwords list
def start():
    global passwords
    # Try and open the file 
    try:
        file = io.open("pwd.txt", 'r', encoding="utf8")
    # If it doesn't exist, create it 
    except IOError:
        file = io.open("pwd.txt", 'w', encoding="utf8")  
    # Take each stored password and add it to the list 
    for line in file:
        passwords.append(line[:-1])
    # Close the file 
    file.close()

    # Promps the user to enter their master password 
    print("""If this is your first run, here is your master password, otherwise
you should already know it""")     
    print(genMasterPassword())
    print("Enter the master password")
    global keystring
    keystring = input(">")
    choice()

# Prompts the user to choose what they want to do next (default is Add Password)
def choice():
    print("Add Password, Remove Password, Show Passwords or Quit? (A/r/s/q)")
    try:
        choice = input(">").lower()[0]
    except:
        choice = 'a'
    if choice == 'q':
        myquit()
    elif choice == 's':
        decrypt()
    elif choice == 'r':
        remove()
    else:
        encrypt()

# Writes the passwords to the password file and exits the program (save and quit)
def myquit():
    out = ""
    # Adds the passwords to a single string to write to pwd.txt
    for password in passwords:
         out += (password + "\n")
    # Write to pwd.txt
    with io.open("pwd.txt", 'w', encoding="utf8") as file:
        file.write(out)
    # Close the program 
    sys.exit()

# Prompts the user to select the index that they wish to remove and then removes that password
def remove():
    # Show the passwords 
    decrypt_part()
    global passwords
    print("Select a password to remove:")
    i = int(input(">"))
    i -=  1
    # Delete the password at a specified index
    try:
        del passwords[i]
    except:
        print("Unsuccessful removal of password")
    # Show the passwords again 
    decrypt_part()
    choice()

# Takes a password, encrypts it using the master password and writes it to the passwords list 
def encrypt():
    global keystring
    outstring = ""
    # Ask the user for a password to encrypt 
    print("Add a password:")
    messagestring = input(">")
    # Encrpyts each character using OTP 
    for index in range(len(messagestring)):
        if index >= len(keystring):
            keystring += keystring
        charint = ord(messagestring[index]) + ord(keystring[index]) - 1
        outstring += chr(charint)
    # Add the password to the 'vault'
    passwords.append(outstring)
    # Show the encrypted password to the user 
    print(outstring)
    choice()

# Runs decrypt_part (the bit that actually decrypts and then choice) - not particularly good but saved me rewriting code 
def decrypt():
    decrypt_part()
    choice()

# Takes all encrypted passwords from the list, decrypts and prints them (password list stays encrypted)
def decrypt_part():
    global keystring
    print("Passwords:")
    # Take each password
    for i in range(len(passwords)):
        outstring = ""
        ncrstring = passwords[i]
        # Decrypts each character using OTP 
        for index in range(len(ncrstring)):
            if index >= len(keystring):
                keystring += keystring
            charint = ord(ncrstring[index]) - ord(keystring[index]) + 1
            outstring += chr(charint)
        # Show each password to the user along with it's index
        print(str(i + 1) + ": " +  outstring)
    
# Generates the master password (20 characters long)
def genMasterPassword():
    masterPassword = ""
    # Generate each character
    for index in range(20):
        masterPassword += chr(random.randint(36,124))
    return masterPassword

# Starts the program 
start()


