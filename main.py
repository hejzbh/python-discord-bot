from modules.bot import DiscordBot
import os
from dotenv import load_dotenv


load_dotenv()

bot = DiscordBot(os.getenv("DISCORD_TOKEN"), os.getenv("OPENAI_API_KEY"))

bot.run()


