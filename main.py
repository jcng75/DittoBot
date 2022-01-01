import os
import discord
from discord.ext import commands
from calculator import calc
# import music
# from replit import db

client = commands.Bot(command_prefix = '?')
token_key = os.environ['client_token']

# async means asynchronous programming, "juggling operations"
# await is used to freeze a function until needed again

@client.event
async def on_ready():
  print(f'Logged in as {client.user}')


@client.command(name="calculate", aliases=['c', 'calc'])
async def _calculate(ctx):
  expression = str(ctx.message.content).split(' ', 1)[1]
  print(f'Calculate command called from {ctx.author}, {expression}')
  await ctx.send(calc(expression))

client.run(token_key)
