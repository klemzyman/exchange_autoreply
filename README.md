# Send Auto-Reply Mail For MS Exchange Server

This script connects to an Exchange server and automatically sends an auto-reply to unread emails received in the last 20 minutes. It marks the emails as replied by adding a category to them.

## Prerequisites

- Python 3.x
- `exchangelib` library
- `pytz` library

## Installation

1. Clone the repository:
	```sh
	git clone https://github.com/yourusername/send_autoreply_mail.git
	cd send_autoreply_mail
	pip install exchangelib pytz

## Configuration
Update the username, password, server, and mailbox variables in the script with your Exchange server credentials and mailbox information.

## Usage
Run the script:

	```python
	python send_autoreply_mail.py

## How It Works

- Connects to the Exchange server using the provided credentials.
- Retrieves unread emails from the inbox that were received in the last 20 minutes and are not marked with the category 'replied'.
- Sends an auto-reply to each unique sender.
- Marks the emails as replied by adding the category 'replied'.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

