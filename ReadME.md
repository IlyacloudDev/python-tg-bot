# Converting Telegram Bot


[Read in Russian](README_ru.md)
___


ConvertingTgBot is a Telegram bot for currency conversion written in Python.

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running](#running)
- [Obtaining API_TOKEN from BotFather](#obtaining-api_token-from-botfather)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Project Description

This project is a Telegram bot that allows users to convert currencies. The bot accepts commands to get information about available currencies and to convert currencies.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ConvertingTgBot.git
    ```
2. Navigate to the project directory:
    ```sh
    cd ConvertingTgBot
    ```
3. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # For Windows use `venv\Scripts\activate`
    ```
4. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Create a `config.py` file in the root directory of the project with the following content:
    ```python
    TOKEN = "YOUR_API_TOKEN"
    lst_ofcurrency = {
        "ruble": "RUB",
        "euro": "EUR",
        "dollar": "USD"
    }
    ```
    Replace `YOUR_API_TOKEN` with your API token from BotFather.

## Running

Run the bot:
```sh
python main.py
```


## Obtaining API_TOKEN from BotFather

1. Open Telegram and find @BotFather.
2. Send the /start command to start working with BotFather.
3. Send the /newbot command and follow the instructions to create a new bot.
4. After creating the bot, you will receive an API token, which should be inserted into the config.py file.


## Usage

To start working with the bot, send the /start or /help command to get instructions. To get a list of available currencies, use the /values command.

Example conversion command:
```text
dollar ruble 35
```
The bot will return the cost of 35 dollars in rubles.


## Dependencies

requirements.txt:
   ```python
    certifi==2024.7.4

    charset-normalizer==3.3.2

    idna==3.7
    
    pyTelegramBotAPI==4.21.0

    requests==2.32.3

    urllib3==2.2.2
   ```

---
# Happy using!
