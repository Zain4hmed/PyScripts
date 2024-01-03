import os
import schedule
import time
import subprocess


def execute_python_file(file_path):
    # Use subprocess to run the Python file as a separate process
    subprocess.run(['python', file_path])


def job(file_path):
    print(f"Executing {file_path} at {time.strftime('%Y-%m-%d %H:%M:%S')}...")
    execute_python_file(file_path)


def schedule_jobs(folder_path, schedule_dict):
    # Get a list of all Python files in the specified folder
    python_files = [file for file in os.listdir(folder_path) if file.endswith('.py')]

    # Schedule each Python file to run at its specified time
    for python_file in python_files:
        file_path = os.path.join(folder_path, python_file)

        if python_file in schedule_dict:
            scheduled_time = schedule_dict[python_file]
            schedule.every().day.at(scheduled_time).do(job, file_path)


if __name__ == "__main__":
    # Specify the folder containing the Python files to be executed
    folder_path = 'C:\\Users\\zaina\\PyScripts\\Scripts\\Automations\\AutomationScripts'

    # Define the schedule for each Python file (replace with your desired times)
    schedule_dict = {
        'script1.py': '08:50',
        'script2.py': '08:51',
        'script3.py': '08:52',
    }

    # Schedule the jobs
    schedule_jobs(folder_path, schedule_dict)

    # Run the scheduler
    while True:
        schedule.run_pending()
        time.sleep(1)
