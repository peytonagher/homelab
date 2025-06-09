import subprocess

def update():
    commands = [
        "sudo apt update",
        "sudo apt upgrade -y",
        "sudo apt autoremove -y",
        "sudo apt clean",
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
    print("1. Shutdown")
    print("2. Restart")
    print("3. Update")
    
    choice = input("Enter (1-3): ")

    if choice == '1':
        subprocess.run(['sudo', 'shutdown', 'now'])
    elif choice == '2':
        subprocess.run(['sudo', 'reboot'])
    elif choice == '3':
        update()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main();
