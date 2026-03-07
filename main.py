from selenium import webdriver  # Import the Selenium WebDriver module
# Import the Service class for managing the ChromeDriver service
from selenium.webdriver.chrome.service import Service
# Import the Options class for configuring Chrome options
from selenium.webdriver.chrome.options import Options
# Import WebDriverWait for explicit waits
from selenium.webdriver.support.ui import WebDriverWait
# Import expected conditions for waits
from selenium.webdriver.support import expected_conditions as EC
# Import the By class for locating elements
from selenium.webdriver.common.by import By
import os  # Import the os module for handling file paths


class WebAutomation:
    def __init__(self):
        # Define driver options for Chrome
        self.chrome_options = Options()  # Create an instance of the Options class
        # Add an argument to disable the search engine screen in Chrome
        self.chrome_options.add_argument("--disable-search-engine-screen")
        download_path = os.getcwd()  # Get the current working directory
        self.prefs = {
            "download.default_directory": download_path
        }  # Set the default download directory to the current working directory
        # Add the preferences to the Chrome options
        self.chrome_options.add_experimental_option("prefs", self.prefs)

        # Set the path to the ChromeDriver executable
        # Create a Service object with the path to the ChromeDriver executable
        # Download the ChromeDriver for your version of Chrome
        self.service = Service('chromedriver-win64/chromedriver.exe')
        # Create a new instance of the Chrome WebDriver using the service
        self.driver = webdriver.Chrome(
            options=self.chrome_options, service=self.service)

    def login(self, username, password):
        # Load the web page
        # Navigate to the specified URL using the WebDriver
        self.driver.get('https://demoqa.com/login')

        # Locate the username field, password field, and login button using explicit waits
        # Wait for the username field to be visible on the page before proceeding
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'userName')))
        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'password')))
        login_button = self.driver.find_element(By.ID, 'login')

        # Fill in the username and password fields, then click the login button
        # Enter the username into the username field
        username_field.send_keys(username)
        # Enter the password into the password field
        password_field.send_keys(password)
        # Click the login button to submit the form
        # Use JavaScript to click the login button
        self.driver.execute_script("arguments[0].click();", login_button)

    def fill_form(self, fullname, email, current_address, permanent_address):
        # Locate the elements dropdown
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                          '//*[@id="root"]/div/div/div/div[1]/div/div/div[1]/span/div')))
        elements.click()  # Click the elements dropdown to expand it
        text_box = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'item-0')))
        text_box.click()  # Click the text box option to navigate to the form page

        # Locate the form fields
        fullname_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'userName')))
        email_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'userEmail')))
        current_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'currentAddress')))
        permanent_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'permanentAddress')))
        submit_button = self.driver.find_element(By.ID, 'submit')

        # Fill in the form fields and submit the form

        # Enter the full name into the fullname field
        fullname_field .send_keys(fullname)
        # Enter the email into the email field
        email_field.send_keys(email)
        # Enter the current address into the current address field
        current_address_field.send_keys(current_address)
        # Enter the permanent address into the permanent address field
        permanent_address_field.send_keys(permanent_address)
        self.driver.execute_script("arguments[0].click();", submit_button)

    def download(self):
        # Locate the upload and download section and download button
        upload_download = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'item-7')))
        upload_download.click()  # Click the elements dropdown to expand it

        download_button = self.driver.find_element(By.ID, 'downloadButton')
        self.driver.execute_script("arguments[0].click();", download_button)

    def close(self):
        self.driver.quit()  # Close the WebDriver and end the session


if __name__ == "__main__":
    webautomation = WebAutomation()  # Create an instance of the WebAutomation class
    # Call the login method to perform the login action
    webautomation.login('pythonusername', 'PythonStudent123$')
    # Call the fill_form method to fill in the form
    webautomation.fill_form(
        'John Doe', 'john.doe@test.com', 'street 123', 'street 123')
    webautomation.download()  # Call the download method to perform the download action
    webautomation.close()  # Call the close method to close the browser
