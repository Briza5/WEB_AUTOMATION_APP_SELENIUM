# Web Automation App with Selenium

This project is part of **The Python Mega Course** - a learning journey into web browser automation using the Selenium library.

## Project Overview

This application demonstrates how to:
- Control web browsers programmatically with Selenium WebDriver
- Use explicit waits for reliable element location
- Automate website login with form filling
- Handle edge cases (e.g., ad banners blocking elements)
- Submit web forms programmatically
- Download files automatically (upcoming)
- Build a desktop GUI for web automation (optional)

## Course Sections Covered

- **Lesson 370**: Today (Introduction)
- **Lesson 371**: Installing the Tools
- **Lesson 372**: Automating Website Login
- **Lesson 373**: Automating Form Filling and Submission
- **Lesson 374**: Automating File Downloading
- **Lesson 375**: Refactoring the Code to OOP (Optional)
- **Lesson 376**: Building a Desktop GUI for the Web Automation Tool (Optional)

## Prerequisites

- Python 3.x
- Chrome browser
- ChromeDriver (compatible with your Chrome version)

## Installation

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download ChromeDriver for your Chrome version and place it in the `chromedriver-win64/` folder

## Usage

Run the main script:
```bash
python main.py
```

The script will:
1. Open Chrome browser with custom options
2. Navigate to the demo login page (https://demoqa.com/login)
3. Wait for username and password fields to be visible
4. Fill in the credentials
5. Submit the login form using JavaScript click (to avoid ad banner interference)
6. Wait for user input before closing the browser

## Project Status

🚧 **Work in Progress** - This project is being developed incrementally as part of the course curriculum.

## Current Features

- ✅ Chrome WebDriver setup with custom options
- ✅ Explicit waits using `WebDriverWait` and `EC`
- ✅ Form field location by ID
- ✅ Automated login with credentials
- ✅ JavaScript-based click to handle ad banners

## Notes

- Uses explicit waits instead of implicit waits for better reliability
- JavaScript click is used for the login button to bypass potential ad banner overlays
- Chrome option `--disable-search-engine-screen` prevents initial search engine selection
- More features will be added in upcoming lessons (file downloading, OOP refactoring, GUI)

## Resources

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)