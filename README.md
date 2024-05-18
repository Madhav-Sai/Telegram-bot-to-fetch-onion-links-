

# Dark Web Scraper Telegram Bot

This Telegram bot allows users to search for information on the dark web using the Ahmia search engine. It scrapes .onion links based on user queries and provides them in a text file.

## Getting Started

### Creating a Telegram Bot

1. **Create a Telegram Account:**
   If you don't have a Telegram account, you need to create one. You can download the Telegram app from your device's app store or use the web version at [web.telegram.org](https://web.telegram.org/).

2. **Start a Chat with BotFather:**
   BotFather is the official bot by Telegram to create and manage bots. Search for "@BotFather" in the Telegram app and start a chat with it.

3. **Create a New Bot:**
   Send the "/newbot" command to BotFather to create a new bot. Follow the instructions provided by BotFather, including providing a name for your bot and a username. The username must end in "bot" and be unique.

4. **Obtain the Bot Token:**
   After creating the bot, BotFather will provide you with a token. This token is essential for authenticating your bot with the Telegram Bot API. Keep this token secure, as it's like a password for your bot.

5. **Set Up Your Bot's Profile (Optional):**
   You can set up your bot's profile picture, description, and other details through BotFather using commands like "/setuserpic" and "/setdescription".

### Installing and Running the Dark Web Scraper Bot

1. **Clone the repository:**

   ```
   git clone https://github.com/Madhav-Sai/.git
   ```

2. **Install dependencies:**

   ```
   pip install -r requirements.txt
   ```

3. **Replace `'YOUR_BOT_TOKEN'` with your Telegram Bot API token in the script.**

4. **Start the bot:**

   ```
   python bot.py
   ```

5. **Interact with the bot on Telegram:**
   - Use `/start` or `/hello` to initiate the bot.
   - Use `/darkweb <query>` to search for information on the dark web.

6. **Make sure to have TOR installed and running to access the .onion links provided by the bot.**

## Contributing

Contributions are welcome! If you'd like to improve this project, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a new Pull Request

## Acknowledgments

- This bot uses the [Ahmia search engine](https://ahmia.fi/) for scraping dark web links.
- Thanks to the developers of Telebot for the Telegram Bot API wrapper.

