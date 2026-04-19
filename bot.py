import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Kirbs is online as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Kirbs says hey")

bot.run(os.getenv("DISCORD_TOKEN"))
