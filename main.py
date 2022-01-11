import os
import discord
from discord.ext import commands
from running import keep_alive
# import music

client = commands.Bot(command_prefix = '?')
token_key = os.environ['client_token']

# async means asynchronous programming, "juggling operations"
# await is used to freeze a function until needed again

@client.event
async def on_ready():
  print(f'Logged in as {client.user}')

for file in os.listdir("/home/runner/DittoBot/commands"):
  if file == "__pycache__":
    continue
  client.load_extension(f'commands.{file[:-3]}')

keep_alive()

client.run(token_key)
