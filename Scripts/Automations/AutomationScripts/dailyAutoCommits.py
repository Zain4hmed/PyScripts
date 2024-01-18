import os
import subprocess
from datetime import datetime

def update_streak_file(repo_path):
    streak_file_path = os.path.join(repo_path, 'streak.txt')

    # Read existing content from the file
    with open(streak_file_path, 'a+') as file:
        file.seek(0)
        lines = file.readlines()

        # Calculate the new streak number
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        streak_number = len(lines) + 1

        # Append the new entry to the file
        new_entry = f'{streak_number}\t{current_date}\n'
        file.write(new_entry)

    return current_date

def commit_and_push_changes(repo_path, commit_message):

    # Change working directory to the repository
    os.chdir(repo_path)

    # Stage changes
    subprocess.run(['git', 'add', 'streak.txt'])

    # Commit changes with the current date as the commit message
    subprocess.run(['git', 'commit', '-m', commit_message])

    # Push changes to the main branch
    subprocess.run(['git', 'push', 'origin', 'main'])

if __name__ == "__main__":
    # Specify the path to the cloned repository
    repo_path = 'C:\\Users\\zaina\\green-fill'

    # Update the streak file and get the current date
    commit_message = update_streak_file(repo_path)

    # Commit and push changes to the repository
    commit_and_push_changes(repo_path, commit_message)

    print(f'Changes committed and pushed with the message: {commit_message}')
