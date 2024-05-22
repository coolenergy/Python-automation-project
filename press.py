import pyautogui
import keyboard
import subprocess
import random


# Create a new git branch
def create_branch(branch_name):
    return subprocess.check_output(["git", "branch", branch_name])


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
def git_push():
    return subprocess.check_output(["git", "push"])


# Replace these with your values
file_path = "app.js"
branch_name = "branch"
commit_message = "This is the commit message for pull request"
remote_name = ""
number = 0

create_branch(branch_name)
modify_file(file_path)
git_commit(commit_message)
git_push(remote_name, branch_name)


def click_screen1():
    create_branch(f"{branch_name}-{number}")
    modify_file(file_path)
    git_commit(commit_message)
    git_push(remote_name, branch_name)


# start listening for the hotkey
keyboard.add_hotkey("ctrl+shift+2", click_screen1)

# this line is necessary to keep the script running
keyboard.wait()
