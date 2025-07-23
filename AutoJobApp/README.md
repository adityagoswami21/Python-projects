# 🔁 AutoJobApp – LinkedIn Auto Apply Bot

A simple Python automation script that logs into LinkedIn and applies to the first job listed using the "Easy Apply" button. Built using Selenium and secured with environment variables.

---

## 🚀 Features

- Opens LinkedIn with pre-defined job search filters.
- Logs in using credentials stored in a `.env` file.
- Clicks the first job post and applies via "Easy Apply".

---

## 📂 Files

- `main.py` – Main script that runs the automation.
- `.env` – Stores your LinkedIn email and password.
- `.gitignore` – Ensures `.env` and other sensitive files are not tracked by Git.

---

## ⚙️ Requirements

- Python 3.x  
- Google Chrome  
- ChromeDriver (added to PATH)  
- Python packages:
```bash
pip install selenium python-dotenv
  ```

## 🔐 Setup
Clone the repository and move into the folder:
```bash
git clone https://github.com/yourusername/AutoJobApp.git
cd AutoJobApp
```

Create a .env file:

```bash
EMAIL=your_email@example.com
PASSWORD=your_linkedin_password
```

Run the script:

```bash
python main.py
```

## ⚠️ Disclaimer
This script is for educational purposes only. Automating interactions on LinkedIn may violate their terms of service. Use at your own risk.