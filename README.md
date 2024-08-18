# Python Mailer

## Overview

This Python script allows you to send emails to multiple recipients using the Simple Mail Transfer Protocol (SMTP). It leverages Python's `smtplib` and `email.mime.text.MIMEText` modules to create and send email messages.

## Features

- Sends emails to a list of recipients.
- Configurable SMTP server (default is Gmail's SMTP server).
- Customizable email subject line.
- Simple and easy to use.

## Requirements

- Python 3.x
- A valid email account (Gmail recommended, but any SMTP server can be used with minor modifications).

## Setup

1. **Install Python**: Make sure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Set Up Your Email Account**:

   - For Gmail accounts, ensure that [Less Secure Apps](https://myaccount.google.com/lesssecureapps) access is enabled, or set up an [App Password](https://support.google.com/accounts/answer/185833).
   - If you are using another email provider, you will need to find the correct SMTP server and port for that provider.

3. **Configure the Script**:

   - Open the script file and locate the `sender` and `password` variables. Replace `"your_email@gmail.com"` with your email address and `"your_password"` with the password or app-specific password of your email account.
   - If you are using a different email provider, replace `"smtp.gmail.com"` with the appropriate SMTP server address and `587` with the corresponding port.

4. **Add Recipients**:
   - Update the `adresat` list with the email addresses of the recipients you want to send the email to.

## Usage

1. **Run the Script**:

   - Open a terminal or command prompt.
   - Navigate to the directory where the script is located.
   - Run the script with the following command:
     ```bash
     python script_name.py
     ```
   - Replace `script_name.py` with the actual name of the Python script file.

2. **Enter Your Message**:

   - When prompted, enter the message you want to send. Press `Enter` to send the email.

3. **Receive Confirmation**:
   - If the email is sent successfully, you will see the message: `"The message was sent successfully!"`.
   - If there is an issue with the login credentials or sending process, an error message will be displayed.

## Code Breakdown

- **Imports**: The script imports `smtplib` for connecting to the SMTP server and `MIMEText` from `email.mime.text` to construct the email message.

- **send_email Function**:

  - Configures the SMTP server and login credentials.
  - Creates a MIME text message.
  - Sends the email to the list of recipients.

- **main Function**:

  - Prompts the user for the message content.
  - Calls the `send_email` function with the provided message.

- **Error Handling**:
  - The script includes basic error handling to catch login failures or other issues during the sending process.

## Customization

- **Subject Line**:

  - You can modify the email subject by changing the `msg["Subject"] = "Test Subject"` line in the `send_email` function.

- **Additional Features**:
  - The script can be expanded to include attachments, HTML content, or other email features by utilizing additional modules from the `email` package.

## Security Considerations

- **Password Safety**:
  - Avoid using your main email account's password in the script. Instead, use an app-specific password if your email provider supports it.
  - Do not hardcode sensitive information in your script, especially if sharing the code. Consider using environment variables or a configuration file.

## Troubleshooting

- **Login Errors**:

  - Ensure that the email address and password are correct.
  - For Gmail users, make sure that either "Less Secure Apps" access is enabled or an app-specific password is used.

- **SMTP Server Issues**:
  - If using a non-Gmail SMTP server, ensure that the correct server address and port are configured.

## License

This script is free to use and modify. There is no warranty provided with this script. Use it at your own risk.

## Contributing

If you have suggestions for improving the script, feel free to fork the repository and submit a pull request.
