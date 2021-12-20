#version: python3
#Author: Gopalsamy Rajendran 
#Date: 15/12/2021
#version: V-1.0 
################################################################################################################### 
import pyfiglet
import os
import sys 
from termcolor import colored

print()
print(colored("Installing Requirements please wait........", "blue"))
cmd = "pip install pyfiglet >nul 2>&1 && pip install termcolor >nul 2>&1"
os.system(cmd)

result = pyfiglet.figlet_format("Incogtriver")
print(result)

print(colored("Author: Gopalsamy Rajendran", "red"))
print("version: 1.0" )

def main():
    menu()

def menu():
    print()
    
    choice = input(colored(""" 
        {1} Retrive Incognito Browsing History
        {2} Clear Incognito Browsing History 
        {3} Exit
        
>> Please enter your choice: """, "green"))

    if choice == "1":
        show_history()
    elif choice == "2":
        delete_history()
    elif choice == "3":
        sys.exit

def show_history():
    cmd = '''Powershell -noexit "ipconfig /displaydns | select-string 'Record Name' | foreach-object { $_.ToString().Split(' ')[-1] } | Sort | Out-Gridview"'''
    os.system(cmd)
    
def delete_history():
    cmd = " ipconfig /flushdns "
    os.system(cmd)

main()