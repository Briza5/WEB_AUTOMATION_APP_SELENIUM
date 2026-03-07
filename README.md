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

Run the GUI application:

```bash
python gui.py
```

The GUI will:

1. Display a form with login credentials and Text Box form fields
2. On Submit — open Chrome, log in, fill the form, and download the sample file
3. On Close Browser — close the Chrome session and show a confirmation dialog

Alternatively, run the automation directly without GUI:

```bash
python main.py
```

## Project Status

Complete - All course sections implemented.

## Code Structure

**`main.py`** — `WebAutomation` class handling all browser automation:

| Method | Description |
| --- | --- |
| `__init__()` | Sets up Chrome options, download preferences, and initializes the WebDriver |
| `login(username, password)` | Navigates to the login page and authenticates |
| `fill_form(fullname, email, current_address, permanent_address)` | Navigates to Text Box and submits the form |
| `download()` | Navigates to Upload & Download section and triggers a file download |
| `close()` | Closes the browser session |

**`gui.py`** — `App` class building the desktop GUI with tkinter:

| Frame | Contents |
| --- | --- |
| `login_frame` | Username and password entry fields |
| `form_frame` | Full name, email, current and permanent address fields |
| `button_frame` | Submit and Close Browser buttons |

## Current Features

- OOP design with `WebAutomation` class (`main.py`) and `App` class (`gui.py`)
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
- GUI built with tkinter — split into `login_frame`, `form_frame`, and `button_frame`
- `WebAutomation` instance created on Submit button click, keeping GUI and automation decoupled

## Resources

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)
