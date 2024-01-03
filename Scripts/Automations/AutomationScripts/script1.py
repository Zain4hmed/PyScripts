import os

def get_current_file_path():
    # Use os.path.realpath to get the absolute path of the current script
    return os.path.realpath(__file__)

if __name__ == "__main__":
    current_file_path = get_current_file_path()
    print(f"The current Python file is located at: {current_file_path}")
