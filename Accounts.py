from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import winsound
import os
os.environ["PATH"] += os.pathsep + 'C:/caminho/completo/do/diretorio/do/geckodriver'

# Define a function to generate a random email name using only letters
def generate_email_name():
    length = random.randint(15, 18)  # Length between 15 and 18 characters
    email_name = "".join(random.choice(string.ascii_lowercase) for _ in range(length))
    return email_name

# Create a loop to repeat the account creation process
for i in range(97):
    # Set up Firefox options if needed
    firefox_options = Options()

    # Définir la préférence pour la langue anglaise
    firefox_options.set_preference("intl.accept_languages", "en-us, en")

    # Uncomment the next line if you want to run Firefox in headless mode
    # firefox_options.add_argument('--headless')

    # Specify the path to the Firefox executable
    # Modify this path according to the location of your Firefox installation
    firefox_binary = "C:/Program Files/Mozilla Firefox/firefox.exe"
    firefox_options.binary = firefox_binary

    # Replace with your path to GeckoDriver
    geckodriver_path = 'C:\\Users\\andre\\OneDrive\\Área de Trabalho\\DADOS + FREELAS\\FREELAS\\Criação automatizada de contas\\Account_Script\\geckodriver.exe'
    service = Service(geckodriver_path)

    # Use Firefox as the driver
    driver = webdriver.Firefox(service=service, options=firefox_options)

    # Navigate to the site app.suno.ai with an automated browser
    driver.get("https://app.suno.ai/")  # Access the URL

    # Loop until the "Sign up" button is found and clicked
    while True:
        try:
            # Check if the "Sign up" button is present
            sign_up_button = driver.find_element(By.XPATH, "//button[text()='Sign up']")
            # If the button is found, click on it and exit the loop
            sign_up_button.click()
            break
        except NoSuchElementException:
            # If the button is not found, wait 0.5 seconds before retrying
            time.sleep(0.1)

    # Loop until the Microsoft button is found and clicked
    while True:
        try:
            # Check if the Microsoft button is present
            microsoft_button = driver.find_element(By.CLASS_NAME, "cl-socialButtonsIconButton__microsoft")
            # If the button is found, click on it and exit the loop
            microsoft_button.click()
            break
        except NoSuchElementException:
            # If the button is not found, wait 0.5 seconds before retrying
            time.sleep(0.1)

    # Loop to search and click on a link
    while True:
        try:
            # Search for the link by its text
            link = driver.find_element(By.XPATH, "//a[contains(text(), 'Create one')]")
            if link:
                link.click()
                break
        except Exception as e:
            time.sleep(0.1)

    # Loop until the "Get a new email address" link is found and clicked
    while True:
        try:
            # Check if the "Get a new email address" link is clickable
            live_switch_link = driver.find_element(By.ID, "liveSwitch")
            # If the link is found, click on it and exit the loop
            live_switch_link.click()
            break
        except NoSuchElementException:
            # If the link is not found, wait 0.5 seconds before retrying
            time.sleep(0.1)

    # Generate an email name
    email_name = generate_email_name()

    # Loop until the "MemberName" input field is found and is interactable
    while True:
        try:
            # Check if the "MemberName" input field is present and interactable
            email_input = driver.find_element(By.ID, "MemberName")
            # If found, enter the email name and exit the loop
            email_input.send_keys(email_name)
            break
        except NoSuchElementException:
            # If the field is not found, wait 0.5 seconds before retrying
            time.sleep(0.1)

    # Construct the full email address
    email_address = f"{email_name}@outlook.fr"

    # Loop until the "Next" button is found and clicked
    while True:
        try:
            # Check if the "Next" button is present and interactable
            next_button = driver.find_element(By.ID, "iSignupAction")
            # If the button is found, click on it and exit the loop
            next_button.click()
            break
        except NoSuchElementException:
            # If the button is not found, wait 0.5 seconds before retrying
            time.sleep(0.1)

    # Loop until the password input field is found
    while True:
        try:
            # Find the password input field
            password_input = driver.find_element(By.ID, "PasswordInput")
            # If found, enter the password and exit the loop
            password_input.send_keys("Lesages1!!!")
            break
        except NoSuchElementException:
            # If not found, wait 0.5 seconds before retrying
            time.sleep(0.1)

    # Loop to wait until the "Next" button is clickable
    while True:
        try:
            # Locate the "Next" button
            next_button = driver.find_element(By.ID, "iSignupAction")
            # Scroll to the button
            driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
            # Check if the button is clickable
            next_button.click()
            break
        except NoSuchElementException:
            # If the button is not found, wait 0.5 seconds before retrying
            time.sleep(0.1)
        except ElementNotInteractableException:
            # If the button is not yet clickable, wait 0.5 seconds before retrying
            time.sleep(0.1)

    # Attempt to fill out the birth date form
    try:
        # Check if the birth date form is present
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "BirthDateLabel")))

        # Select the day, month, and year
        # Replace '15', 'May', '1990' with desired values
        day_select = driver.find_element(By.ID, "BirthDay")
        day_select.send_keys('15')  # Enter the day

        month_select = driver.find_element(By.ID, "BirthMonth")
        month_select.send_keys('May')  # Enter the month in English

        year_input = driver.find_element(By.ID, "BirthYear")
        year_input.send_keys('1990')  # Enter the year

        # Click on the "Next" button
        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "iSignupAction")))
        next_button.click()  # Proceed to the next step

    except NoSuchElementException:
        # Birth date form is not present on the page
        # Output a message if the form is not found
        print("Birth date form is not present on the page.")

    # Wait a moment for the page to load
    time.sleep(2)

    # Check if the text "Add security information" is present
    try:
        time.sleep(2)
        security_info = driver.find_element(By.XPATH, "//div[contains(text(), 'Add security info')]")
        if security_info:
            # Emit a beep sound (440 Hz for 1/2 second)
            winsound.Beep(440, 500)
            print(
                "Change your IP address and relaunch the script.\n"
                "1. Connect your PC to the Internet via a Mobile Hotspot.\n"
                "2. Toggle airplane mode off and on on your mobile device. "
                "This will assign you a new IP address.\n"
                "3. Turn the hotspot back on.\n"
                "Please note that you need to repeat this process after every 3 accounts. "
            )

            driver.quit()
            exit()  # Stop script execution

    except NoSuchElementException:
        # The specified text is not found, continue script execution
        pass

    # Loop to wait until the captcha is manually solved
    while True:
        try:
            # Locate the button
            accept_button = driver.find_element(By.ID, "idBtn_Accept")
            time.sleep(2)
            # Scroll to the button
            driver.execute_script("arguments[0].scrollIntoView(true);", accept_button)
            # If the button is clickable, click on it and exit the loop
            accept_button.click()
            break
        except:
            # If the button is not yet clickable, wait 1 second before retrying
            time.sleep(0.1)

    # Save the email in a file
    with open("emails_accounts.txt", "a") as file:
        file.write(email_address + "\n")

    time.sleep(3)

    # Close the browser
    driver.quit()