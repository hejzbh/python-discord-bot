import discord
from modules.scraper import NewsScraper
from modules.summarizer import Summarizer

class DiscordBot:
    def __init__(self, token, api_key):
        # storep rovided data
        self.token = token
        self.api_key = api_key
        
        # set up default intents for the Discord client
        intens = discord.Intents.default()
        intens.message_content = True  # Enable intent to read message content

        # Initialize the disc client with the specified intents
        self.client = discord.Client(intents=intens)

        # Register event listeners for the bot's lifecycle and incoming messages
        self.client.event(self.on_ready)
        self.client.event(self.on_message)

    async def on_ready(self):
        print(f"Logged in as {self.client.user}")

    async def on_message(self, message):
        if message.author == self.client.user:
            return
        
        if message.content == "!news":
            # Notify the user that news fetching is in progress
            await message.channel.send("Wait until fetching news is done...")

      
            scraper = NewsScraper("https://www.technewsworld.com/section/it")
            news_data = scraper.scrape()

            # If scraping fails or returns no data, exit the function
            if news_data is None:
                return

            # Use the Summarizer to generate a summary of the scraped news
            summarizer = Summarizer(self.api_key)
            summary = summarizer.summarize(news_data)
            
            # Send the generated summary to the dsc channel
            await message.channel.send(summary)

    def run(self):
       # start the bot using the provided token
        self.client.run(self.token)
