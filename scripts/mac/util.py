#!/usr/bin/env python3
import subprocess

def update():
    commands = [
        "softwareupdate -l",
        "brew update",
        "brew upgrade",
        "neofetch"
    ]

    for command in commands:
        print(f"Running: {command}")
        process = subprocess.run(command, shell=True)

        if process.returncode != 0:
            print(f"Error: {command} failed.")
            break
    else:
        print("OS update completed successfully!")

def main():
    print("Select an option:")
    print("1. Sleep")
    print("2. Restart")
    print("3. Shutdown")
    print("4. Update")
    
    option = input("Enter your choice (1-4): ")

    if option == '1':
        subprocess.run('pmset sleepnow')
    elif option == '2':
        subprocess.run('sudo shutdown -r +1')
    elif option == '3':
        subprocess.run('sudo shutdown -h +1')
    elif option == '4':
        update()
    else:
        print("Invalid option. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
