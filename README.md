# Password Manager

A simple password manager built using Python and Tkinter to store and retrieve passwords securely. This application generates random passwords, saves them along with the website and email/username, and retrieves the saved password details for a particular website.

## Features

- **Password Generation**: Automatically generates a random password with a mix of letters, numbers, and symbols.
- **Password Storage**: Saves website, email, and password in a JSON file (`Day29_data.json`) for easy access.
- **Search Functionality**: Quickly retrieves saved password details for any website.
- **Clipboard Copying**: Generated password is automatically copied to the clipboard for convenience.
- **Data Persistence**: Saves all entries in a JSON file to retain data between sessions.

## Requirements

- Python 3.x
- Tkinter (included with standard Python distribution)
- Additional dependencies: `pyperclip` and `zipfile` for clipboard support and handling zip files.

## Installation

1. Clone or download the project to your local machine.
2. Install the required libraries:

pip install pyperclip

## How to Use

1. **Generate a Password**:

   - Click on the "Generate Password" button to create a strong random password.
   - The generated password will be automatically copied to your clipboard.

2. **Save Password**:

   - Enter the website name, your email/username, and the generated or custom password.
   - Click the "Add" button to save these details. The data will be saved in a file named `Day29_data.json`.

3. **Search for a Password**:

   - To retrieve the saved password for a particular website, type the website name in the "Website" field.
   - Click "Search" to display the email and password details for that website, if found.

4. **Clipboard Copying**:

   - After generating a password, it will automatically be copied to your clipboard for easy use.

5. **Data Storage**:
   - All your password data is stored in a JSON file (`Day29_data.json`), which will persist between sessions.

## License

This `README.md` provides a detailed description of the password manager project, including how to install and use it, its features, and dependencies. Let me know if you need further adjustments!

```bash

```
