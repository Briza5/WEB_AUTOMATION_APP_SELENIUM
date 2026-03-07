# Web Automation App with Selenium

This project is part of **The Python Mega Course** - a learning journey into web browser automation using the Selenium library.

## Project Overview

This application demonstrates how to:

- Control web browsers programmatically with Selenium WebDriver
- Use explicit waits for reliable element location
- Automate website login with form filling
- Handle edge cases (e.g., ad banners blocking elements)
- Submit web forms programmatically
- Set custom Chrome download preferences
- Download files automatically
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

1. Open Chrome with download directory set to the current working directory
2. Navigate to the demo login page at `https://demoqa.com/login`
3. Fill in credentials and submit the login form using JavaScript click
4. Navigate to Elements > Text Box, fill in the form and submit
5. Navigate to Elements > Upload and Download section
6. Click the download button to trigger file download
7. Wait for user input before closing the browser

## Project Status

Work in Progress - This project is being developed incrementally as part of the course curriculum.

## Code Structure

The code is organized into a `WebAutomation` class with the following methods:

| Method | Description |
| --- | --- |
| `__init__()` | Sets up Chrome options, download preferences, and initializes the WebDriver |
| `login(username, password)` | Navigates to the login page and authenticates |
| `fill_form(fullname, email, current_address, permanent_address)` | Navigates to Text Box and submits the form |
| `download()` | Navigates to Upload & Download section and triggers a file download |
| `close()` | Closes the browser session |

## Current Features

- OOP design with `WebAutomation` class
- Chrome WebDriver setup with custom options and download preferences
- Explicit waits using `WebDriverWait` and `EC`
- Element location by ID and XPath
- Automated login with credentials
- JavaScript-based click to handle ad banners
- Navigation via hamburger menu (XPath locator)
- Automated form filling and submission
- Custom download directory via `add_experimental_option`
- Automated file downloading

## Notes

- Uses explicit waits instead of implicit waits for better reliability
- JavaScript click is used for buttons to bypass potential ad banner overlays
- Chrome option `--disable-search-engine-screen` prevents initial search engine selection
- XPath is used when elements don't have a unique ID attribute
- Download path is set to `os.getcwd()` — files download to the project folder
- Entry point guarded with `if __name__ == "__main__":` for reusability

## Resources

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)
