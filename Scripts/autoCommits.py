import os
import subprocess
from datetime import datetime, timedelta
import random

def random_date(start, end):
    """Generate a random datetime between `start` and `end`."""
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds()))
    )

def update_streak_file(repo_path, streak_number, commit_date):
    """Update the streak file with the streak number and commit date."""
    streak_file_path = os.path.join(repo_path, 'streak.txt')

    # Read existing content from the file
    with open(streak_file_path, 'a+') as file:
        file.seek(0)
        lines = file.readlines()

        # Append the new entry to the file
        new_entry = f'{streak_number}\t{commit_date.strftime("%Y-%m-%d %H:%M:%S")}\n'
        file.write(new_entry)

def commit_and_push_changes(repo_path, commit_message, commit_date):
    """Commit and push changes with the given commit message and date."""

    # Change working directory to the repository
    os.chdir(repo_path)

    # Stage changes
    subprocess.run(['git', 'add', 'streak.txt'])

    # Commit changes with the specific commit date
    # Set the GIT_AUTHOR_DATE and GIT_COMMITTER_DATE environment variables
    env = os.environ.copy()
    env['GIT_AUTHOR_DATE'] = commit_date.strftime('%Y-%m-%d %H:%M:%S')
    env['GIT_COMMITTER_DATE'] = commit_date.strftime('%Y-%m-%d %H:%M:%S')
    subprocess.run(['git', 'commit', '-m', commit_message], env=env)

    # Push changes to the main branch
    subprocess.run(['git', 'push', 'origin', 'main'])

if __name__ == "__main__":
    # Specify the path to the cloned repository
    repo_path = 'C:\\Users\\zaina\\green-fill'

    # Define the start and end dates for random commits
    start_date = datetime(2023, 9, 1)
    end_date = datetime(2024, 6, 7)

    # Number of commits you want to make
    num_commits = 95

    for streak_number in range(1, num_commits + 1):
        # Generate a random commit date within the range
        commit_date = random_date(start_date, end_date)

        # Update the streak file
        update_streak_file(repo_path, streak_number, commit_date)

        # Commit and push changes to the repository
        commit_and_push_changes(repo_path, f'Commit {streak_number} on {commit_date.strftime("%Y-%m-%d %H:%M:%S")}', commit_date)

        print(f'Committed and pushed: Commit {streak_number} on {commit_date.strftime("%Y-%m-%d %H:%M:%S")}')
