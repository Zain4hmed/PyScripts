import time
import pyautogui
from PIL import Image
import subprocess
import os
import fitz
import random
import string

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
    # Add the code from the other Python file here
    import fitz
    import os
    import random
    import string

    def add_random_character_to_pdf(input_pdf_path, target_text, text_color=(1, 1, 1)):
        doc = fitz.open(input_pdf_path)

        for page_num in range(doc.page_count):
            page = doc[page_num]
            text_instances = page.get_text("text")

            if target_text in text_instances:
                rect = page.rect

                # Remove any previous added single character
                for annot in page.annots():
                    if annot.info == target_text and len(annot["text"]) == 1:
                        annot.delete()

                # Add a single random character with the specified color
                random_char = random.choice(string.ascii_letters)
                page.insert_text((rect.x0, rect.y1 - 20), random_char, fontsize=12, color=text_color)

        # Save incrementally to the original file
        doc.saveIncr()
        doc.close()

    # Example usage
    resume_path = 'C:\\Users\\zaina\\Downloads\\ZainAhmedResume.pdf'
    target_text = 'Zain Ahmed'
    text_color = (1, 1, 1)  # RGB values between 0 and 1 for white

    add_random_character_to_pdf(resume_path, target_text, text_color)

    print("resume updated...")

def uploadUpdatedResume():
    # Add your code for uploading the updated resume here
    
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
    open_chrome()
    downloadResumeFromLinkedin()
    updateResume()
    uploadUpdatedResume()
