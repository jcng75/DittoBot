from discord.ext import commands
from random import randint
import asyncio

connected_bot = None

def setup(bot):
  global connected_bot
  bot.add_command(_guess)
  connected_bot = bot

# helper func to get guess for guess game
async def get_guess(ctx, original):
  def check(message):
    return message.author == original and message.content.isnumeric()
  try:
    user_guess = await connected_bot.wait_for('message', timeout=25.0, check=check)
  except asyncio.TimeoutError:
    await ctx.send("You ran out of time to guess!")
    return -1
  return int(user_guess.content)

@commands.command(name="guess")
async def _guess(ctx):
  await ctx.send(f"<@{ctx.author.id}> initiated the guess game!  Please guess a number from 1 - 100!")
  val = randint(1, 100)
  original_user = ctx.author
  user_guess = [await get_guess(ctx, original_user)]
  counter = 1
  while(val != user_guess[-1]):
    counter += 1
    if user_guess[-1] == -1:
      return
    elif val > user_guess[-1]:
      await ctx.send(f"Incorrect <@{ctx.author.id}>!  The number is larger!  You've guessed {user_guess} so far.")
    else:
      await ctx.send(f"Incorrect <@{ctx.author.id}>!  The number is smaller!   You've guessed {user_guess} so far.")
    user_guess.append(await get_guess(ctx, original_user))
  await ctx.send(f'Correct <@{ctx.author.id}>!  The number was {val}!  It took you {counter} guesses!')