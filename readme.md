# Website Change Detection Tool

## Overview
A Python tool to monitor changes on a specific webpage and notify users via email. It’s useful for tracking updates on websites like product listings or blogs.

## Features
- **Web Scraping**: Uses `BeautifulSoup` to extract and monitor content. 
- **Notification**: Sends email alerts on change detection.
- **Scheduling**: Runs checks at regular intervals using `schedule`.

## Usage
1. Install dependencies: `pip install -r requirements.txt`
2. Configure email settings in `config.json`.
3. Run `python monitor.py --url <website_url>`

## Technologies Used
- `requests` and `BeautifulSoup` for web scraping
- `smtplib` for email notifications
