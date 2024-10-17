import discord
from modules.scraper import NewsScraper
from modules.summarizer import Summarizer



class DiscordBot:
    def __init__(self, token, api_key):
        # Store token
        self.token = token
        self.api_key = api_key
        
        # Prepare intens for client
        intens = discord.Intents.default()
        intens.message_content = True

        # Store Client 
        self.client = discord.Client(intents=intens)

        # Add Event Listeners
        self.client.event(self.on_ready)
        self.client.event(self.on_message)

    async def on_ready(self):
        print(f"Logged in as {self.client.user}")

    async def on_message(self,message):
        if message.author == self.client.user:
            return
        
        if message.content == "!news":
            await message.channel.send("Wait until fetching news is done...")

            scraper = NewsScraper("https://www.technewsworld.com/section/it")
            news_data = scraper.scrape()  

            if news_data is None:
                return
            

            summarizer = Summarizer(self.api_key)

            summary = summarizer.summarize(news_data)
            
            await message.channel.send(summary)



    def run(self):
        self.client.run(self.token)
        


