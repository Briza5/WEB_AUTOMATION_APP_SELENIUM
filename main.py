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

# Define driver options for Chrome
chrome_options = Options()  # Create an instance of the Options class
# Add an argument to disable the search engine screen in Chrome
chrome_options.add_argument("--disable-search-engine-screen")
# Set the path to the ChromeDriver executable
# Create a Service object with the path to the ChromeDriver executable
# Download the ChromeDriver for your version of Chrome
service = Service('chromedriver-win64/chromedriver.exe')
# Create a new instance of the Chrome WebDriver using the service
driver = webdriver.Chrome(options=chrome_options, service=service)

# Load the web page
# Navigate to the specified URL using the WebDriver
driver.get('https://demoqa.com/login')


# Locate the username field, password field, and login button using explicit waits
# Wait for the username field to be visible on the page before proceeding
username_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'password')))
login_button = driver.find_element(By.ID, 'login')

# Fill in the username and password fields, then click the login button
# Enter the username into the username field
username_field.send_keys('pythonusername')
# Enter the password into the password field
password_field.send_keys('PythonStudent123$')
# Click the login button to submit the form
# Use JavaScript to click the login button
driver.execute_script("arguments[0].click();", login_button)

# Locate the elements dropdown
elements = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                             '//*[@id="root"]/div/div/div/div[1]/div/div/div[1]/span/div')))
elements.click()  # Click the elements dropdown to expand it
text_box = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'item-0')))
text_box.click()  # Click the text box option to navigate to the form page

# Locate the form fields
fullname_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'userName')))
email_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'userEmail')))
current_address_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'currentAddress')))
permanent_address_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'permanentAddress')))
submit_button = driver.find_element(By.ID, 'submit')

# Fill in the form fields and submit the form

# Enter the full name into the fullname field
fullname_field .send_keys('John Doe')
# Enter the email into the email field
email_field.send_keys('john.doe@test.com')
# Enter the current address into the current address field
current_address_field.send_keys('123 Main St, Anytown, USA')
# Enter the permanent address into the permanent address field
permanent_address_field.send_keys('456 Elm St, Anytown, USA')
driver.execute_script("arguments[0].click();", submit_button)


# Wait for user input before closing the browser
input("Press Enter to close the browser...")
driver.quit()  # Close the WebDriver and end the session
