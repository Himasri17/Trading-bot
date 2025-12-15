
# Binance Futures Testnet – Trading Bot (Python)

A simplified automated trading bot built for the **Binance Futures Testnet** using Python.
This project was developed as part of a hiring assignment for the role:

**“Junior Python Developer – Crypto Trading Bot”**

The bot supports  **Market** ,  **Limit** , and **Stop-Limit** orders with a clean modular structure,
user input validation, and full logging of API requests, responses, and errors.

---

## 🚀 Features

### ✔ Core Requirements

* Connects to Binance **USDT-M Futures Testnet**
* Place **Market Orders** (Buy/Sell)
* Place **Limit Orders**
* Input validation via CLI
* Logs all API actions into `logs/bot.log`
* Fully modular Python class (`BasicBot`)

### ⭐ Bonus Features

* Supports **Stop-Limit** orders
* Clean CLI interface
* Easy to extend for TWAP, Grid, OCO, etc.

---

## 🧩 Project Structure

```
trading-bot/
│── bot.py                 # Main trading logic (Market, Limit, Stop-Limit)
│── cli.py                 # Command-line interface for the bot
│── config_example.py      # Template for API key config
│── logs/
│    └── bot.log           # Log file generated while bot runs
│── requirements.txt       # Project dependencies
│── README.md              # Documentation (this file)
```

⚠️ **Never upload your real API keys.**
Create a private `config.py` with your credentials and keep it out of GitHub.

---

## 🛠 Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/<your-username>/crypto-trading-bot-testnet.git
cd crypto-trading-bot-testnet
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Create and configure `config.py`

Create a new file:

```
config.py
```

Add your Testnet API keys:

```
API_KEY = "your_testnet_api_key"
API_SECRET = "your_testnet_api_secret"
```

---

## ▶️ Running the Bot

Start the bot:

```
python3 cli.py
```

You will see:

```
=== Binance Futures Testnet Trading Bot ===
Enter trading pair (e.g., BTCUSDT):
```

Example inputs:

* **Symbol** → BTCUSDT
* **Order Type** → 1 (Market)
* **Side** → BUY
* **Quantity** → 0.001

You’ll get the Binance API response printed on screen.

---

## 📜 Logging

All events are automatically logged to:

```
logs/bot.log
```

The log contains:

* Order attempts
* Server responses
* Status updates
* Errors (if any)

This log file is part of the required assignment submission.

---

## 📦 Requirements

```
python-binance
```
