import discord
from discord.ext import commands

# Initialize bot
bot = commands.Bot(command_prefix='!')

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.yellowdog2006}')

# Command: !hello
@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

# Run the bot
bot.run('YOUR_TOKEN_HERE')