import discord
from modules.scraper import NewsScraper
from modules.summarizer import Summarizer

class DiscordBot:
    def __init__(self, token, api_key):
        # Store the Discord bot token and API key for the summarizer
        self.token = token
        self.api_key = api_key
        
        # Set up default intents for the Discord client
        intens = discord.Intents.default()
        intens.message_content = True  # Enable intent to read message content

        # Initialize the Discord client with the specified intents
        self.client = discord.Client(intents=intens)

        # Register event listeners for the bot's lifecycle and incoming messages
        self.client.event(self.on_ready)
        self.client.event(self.on_message)

    async def on_ready(self):
        # Triggered when the bot is logged in and ready
        print(f"Logged in as {self.client.user}")

    async def on_message(self, message):
        # Avoid responding to the bot's own messages to prevent loops
        if message.author == self.client.user:
            return
        
        # Handle the "!news" command
        if message.content == "!news":
            # Notify the user that news fetching is in progress
            await message.channel.send("Wait until fetching news is done...")

            # Scrape news articles from the given URL
            scraper = NewsScraper("https://www.technewsworld.com/section/it")
            news_data = scraper.scrape()

            # If scraping fails or returns no data, exit the function
            if news_data is None:
                return

            # Use the Summarizer class to generate a summary of the scraped news
            summarizer = Summarizer(self.api_key)
            summary = summarizer.summarize(news_data)
            
            # Send the generated summary to the Discord channel
            await message.channel.send(summary)

    def run(self):
        # Start the Discord bot using the provided token
        self.client.run(self.token)
