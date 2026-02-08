from selenium import webdriver  # Import the Selenium WebDriver module
# Import the Service class for managing the ChromeDriver service
from selenium.webdriver.chrome.service import Service


# Set the path to the ChromeDriver executable
# Create a Service object with the path to the ChromeDriver executable
# Download the ChromeDriver for your version of Chrome
service = Service('chromedriver-win64/chromedriver.exe')
# Create a new instance of the Chrome WebDriver using the service
driver = webdriver.Chrome(service=service)
# Navigate to the specified URL using the WebDriver
driver.get('https://demoqa.com/login')

# Wait for user input before closing the browser
input("Press Enter to close the browser...")
driver.quit()  # Close the WebDriver and end the session
