import os
import json
import shutil
from colorama import Fore

def startup():
    os.chdir(os.path.dirname(__file__))
    write("Welcome to Micro Minecrat Mod Manager", Fore.YELLOW)
    while True:
        write("What do you want to do? New Mod, New Profile, Launch Profile, Exit (m, p, l, e)", Fore.BLUE)
        choice = input(f"{Fore.GREEN}>>> ")
        if choice == "m":
            new_mod()
        elif choice == "p":
            new_profile()
        elif choice == "l":
            launch_profile()
        elif choice == "e":
            input(f"{Fore.GREEN}Press any key to close...")
            break
        else:
            write("Invalid Command. Try Again", Fore.RED)

def new_mod():
    while True:
        write("Mod Location", Fore.YELLOW)
        mod_location = input(f"{Fore.GREEN}>>> ")
        write("Mod Name", Fore.YELLOW)
        mod_name = input(f"{Fore.GREEN}>>> ")
        write("Move or Copy? (m/c)", Fore.YELLOW)
        try:
            if input(">>> ").lower() == "m":
                shutil.move(mod_location, f"../Mods/{mod_name}.jar")
            else:
                shutil.copyfile(mod_location, f"../Mods/{mod_name}.jar")
            break
        except:
            write("Error: Try using Forward Slashes instead of Back Slashes", Fore.RED)

def new_profile():
    write("Profile Name", Fore.YELLOW)
    profile_name = input(">>> ")
    os.mkdir(f"../Profiles/{profile_name}")
    if len(os.listdir("../Mods")) == 0:
        write("You have no mods installed. How about adding some?", Fore.BLUE)
    else:
        write("Add Mods to your Profile (y/n)", Fore.YELLOW)
        for mod in os.listdir("../Mods"):
            if input(mod + ": ") == "y":
                shutil.copyfile(f"../Mods/{mod}", f"../Profiles/{profile_name}/{mod}")
            else:
                pass

def launch_profile():
    minecraftFolderLocation = json.load(open("user_info.json", "r"))[".minecraft_folder"]
    if len(os.listdir("../Profiles")) == 0:
        write("You have not made any Profiles. How about creating one?", Fore.BLUE)
    else:
        if len(os.listdir(minecraftFolderLocation)) != 0:
            if input(f"{Fore.GREEN}You already have mods installed? Replace them? (y/n) ") == "y":
                for mod in os.listdir(minecraftFolderLocation):
                    os.remove(f"{minecraftFolderLocation}/{mod}")

                write("Select your Desired Profile (y/n)", Fore.YELLOW)
                for profile in os.listdir("../Profiles"):
                    if input(f"{profile}: ") == "y":
                        for mod in os.listdir(f"../Profiles/{profile}"):
                            shutil.copyfile(f"../Profiles/{profile}/{mod}", f"{minecraftFolderLocation}/{mod}")
                        break
            else:
                write("Failed to Launch Profile", Fore.RED)
        else:
            write("Select your Desired Profile (y/n)", Fore.YELLOW)
            for profile in os.listdir("../Profiles"):
                if input(f"{profile}: ") == "y":
                    for mod in os.listdir(f"../Profiles/{profile}"):
                        shutil.copyfile(f"../Profiles/{profile}/{mod}", f"{minecraftFolderLocation}/{mod}")
                    break

def write(text=None, color=Fore.WHITE):
    print(f"{color}{text}")

startup()