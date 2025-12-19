# Obfuscation and Deobfuscation App

This is a simple Streamlit application that allows you to obfuscate and deobfuscate text using various encoding methods.

## Features

- **Obfuscate**: Convert plain text into obfuscated text using Base64 or ROT13 encoding.
- **Deobfuscate**: Convert obfuscated text back to plain text.
- Supports two methods: Base64 and ROT13.

## Installation

1. Ensure you have Python installed.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the application with:
```
streamlit run main.py
```

Open the provided URL in your browser to use the app.

Select the obfuscation method from the dropdown, enter your text, and click the appropriate button.

## Notes

- Base64: Standard base64 encoding/decoding.
- ROT13: A simple letter substitution cipher that shifts letters by 13 positions.
- Ensure the obfuscated text matches the selected method for deobfuscation to work.