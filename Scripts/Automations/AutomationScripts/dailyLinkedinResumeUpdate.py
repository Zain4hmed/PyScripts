import time
import pyautogui
from PIL import Image
import subprocess
import os





def open_chrome():
    # Wait for a few seconds to give time for the user to focus on the appropriate window
    time.sleep(3)

    # Press the Windows key to open the Start menu
    pyautogui.press('win')

    # Wait for a short time
    time.sleep(3)

    # Type 'chrome' and press Enter
    pyautogui.write('chrome')
    pyautogui.press('enter')

    # Wait for a short time
    time.sleep(3)

    # Type the link and press Enter
    pyautogui.write('link')  # Replace with your actual link
    pyautogui.press('enter')





def find_and_click_icon(icon_path):
    # Wait for a few seconds to allow time for the page to load
    time.sleep(2)

    # Load the icon image
    icon_image = Image.open(icon_path)

    # Search for the icon on the screen
    location = pyautogui.locateOnScreen(icon_path)

    if location is not None:
        # Get the center coordinates of the icon
        center_x, center_y = pyautogui.center(location)

        # Click on the center of the icon
        pyautogui.click(center_x, center_y)
    else:
        print(f"Icon not found on the screen.")





def downloadResumeFromLinkedin():
        
    time.sleep(2)
    # look for job icon
    icon_path1 = 'C:\\Users\\zaina\\PyScripts\\Scripts\\Automations\\AutomationScripts\\LinkedinIconResources\\Screenshot 2024-01-03 112032.png'
    find_and_click_icon(icon_path1)

    # Wait for a few seconds before attempting to click the second icon
    time.sleep(2)
    # look for the Application settings icon
    icon_path2 = 'C:\\Users\\zaina\\PyScripts\\Scripts\\Automations\\AutomationScripts\\LinkedinIconResources\\Screenshot 2024-01-03 113137.png'
    find_and_click_icon(icon_path2)

    # Wait for a few seconds before attempting to click the second icon
    time.sleep(2)
    # look for the 3 dots ...
    icon_path3 = 'C:\\Users\\zaina\\PyScripts\\Scripts\\Automations\\AutomationScripts\\LinkedinIconResources\\Screenshot 2024-01-03 113658.png'
    find_and_click_icon(icon_path3)

    
    # Wait for a few seconds before attempting to click the second icon
    time.sleep(2)
    # look for the download button
    icon_path4 = 'C:\\Users\\zaina\\PyScripts\\Scripts\\Automations\\AutomationScripts\\LinkedinIconResources\\Screenshot 2024-01-03 141149.png'
    find_and_click_icon(icon_path4)

    

def updateResume():
    #impliment the code of the other pyt hon file here // chat gpt please complete it here


def uploadUpdatedResume():

    # Wait for a few seconds before attempting to click the second icon
    time.sleep(2)
    # look for the 3 dots ...
    icon_path3 = 'C:\\Users\\zaina\\PyScripts\\Scripts\\Automations\\AutomationScripts\\LinkedinIconResources\\Screenshot 2024-01-03 113658.png'
    find_and_click_icon(icon_path3)

    # Wait for a few seconds before attempting to click the second icon
    time.sleep(2)
    # look for the dustbin icon
    icon_path4 = 'C:\\Users\\zaina\\PyScripts\\Scripts\\Automations\\AutomationScripts\\LinkedinIconResources\\Screenshot 2024-01-03 113820.png'
    find_and_click_icon(icon_path4)

    # Wait for a few seconds before attempting to click the second icon
    time.sleep(2)
    # look for the upload icon
    icon_path4 = 'C:\\Users\\zaina\\PyScripts\\Scripts\\Automations\\AutomationScripts\\LinkedinIconResources\\Screenshot 2024-01-03 142449.png'
    find_and_click_icon(icon_path4)

    # Wait for a few seconds before attempting to click the second icon
    time.sleep(2)
    # Type 'chrome' and press Enter
    pyautogui.write('ZainAhmedResume.pdf')
    pyautogui.press('enter')

    

if __name__ == "__main__":
    resume_path = 'C:\\Users\\zaina\\Downloads\\ZainAhmedResume.pdf'
    target_text = 'Zain Ahmed'
    text_color = (1, 1, 1)  # RGB values between 0 and 1 for white
    open_chrome()

    downloadResumeFromLinkedin()

    updateResume()

    uploadUpdatedResume()