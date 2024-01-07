import os
import schedule
import time
import subprocess


def execute_python_file(file_path, loop_count=1, interval_seconds=60):
    for _ in range(loop_count):
        # Use subprocess to run the Python file as a separate process
        subprocess.run(['python', file_path])
        time.sleep(interval_seconds)


def job(file_path, loop_count=1, interval_seconds=60):
    print("-----------------------------------------------------------------")
    print(f"Executing {file_path} at {time.strftime('%Y-%m-%d %H:%M:%S')}...")
    execute_python_file(file_path, loop_count, interval_seconds)


def schedule_jobs(folder_path, schedule_dict):
    # Get a list of all Python files in the specified folder
    python_files = [file for file in os.listdir(folder_path) if file.endswith('.py')]

    # Schedule each Python file with its specific details
    for python_file in python_files:
        file_path = os.path.join(folder_path, python_file)

        if python_file in schedule_dict:
            details          = schedule_dict[python_file]
            scheduled_time   = details.get('scheduled_time', '00:00')
            loop_count       = details.get('loop_count', 1)
            interval_seconds = details.get('interval_seconds', 60)

            schedule.every().day.at(scheduled_time).do(job, file_path, loop_count, interval_seconds)


if __name__ == "__main__":
    # Specify the folder containing the Python files to be executed
    folder_path = 'C:\\Users\\zaina\\PyScripts\\Scripts\\Automations\\AutomationScripts'

    # Define the schedule and details for each Python file
    schedule_dict = {
        'dailyAutoCommits.py' : {'scheduled_time': '10:00', 'loop_count': 1, 'interval_seconds': 1}
        # 'script2.py' : {'scheduled_time': '10:49', 'loop_count': 6, 'interval_seconds': 2},
        # 'script3.py' : {'scheduled_time': '10:50', 'loop_count': 3, 'interval_seconds': 3},
    }

    # Schedule the jobs
    schedule_jobs(folder_path, schedule_dict)

    # Run the scheduler
    while True:
        schedule.run_pending()
        time.sleep(1)