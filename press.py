import pyautogui
import keyboard
import subprocess
import random
import time

# Replace these with your values
file_path = "app.js"
branch_name = "sharkbranch"
commit_message = "This is the commit message for pull request"
remote_name = "origin"
global number
number = 0


# Create a new git branch
def create_branch(branch_name):
    return subprocess.check_output(["git", "checkout", "-b", branch_name])


# Modify the specified file by adding random JavaScript code
def modify_file(file_path):
    with open(file_path, "a") as file:
        random_js_code = (
            f"\nconsole.log({random.randint(1, 100)});"  # Random JavaScript code
        )
        file.write(random_js_code)


# Commit with the message
def git_commit(commit_message):
    subprocess.check_output(["git", "add", "."])
    return subprocess.check_output(["git", "commit", "-m", commit_message])


# Push the code
def git_push(remote_name, branch_name):
    return subprocess.check_output(["git", "push", remote_name, branch_name])


def click_screen1(number):
    name = f"{branch_name}{number}"
    create_branch(name)
    modify_file(file_path)
    git_commit(commit_message)
    git_push(remote_name, name)


def main():
    for i in range(120):
        click_screen1(i)
        time.sleep(20)
        print("---------------------------", i)


main()
