from discord.ext import commands
from random import randint
from .mongo import update_guesshs
import asyncio

connected_bot = None

def setup(bot):
  global connected_bot
  bot.add_command(_guess)
  connected_bot = bot

# helper func to get guess for guess game
# has a check function that confirms if the original user is guessing and if the input is numeric only
# gets input, sets timer for 25 seconds to type something
# returns the message back as an integer
async def get_guess(ctx, original):
  def check(message):
    return message.author == original and message.content.isnumeric()
  try:
    user_guess = await connected_bot.wait_for('message', timeout=25.0, check=check)
  except asyncio.TimeoutError:
    await ctx.send("You ran out of time to guess! :alarm_clock:")
    return -1
  return int(user_guess.content)

# the guess game goes as follows:
# The user guesses a random number from 1-100
# After guessing correctly, the user's total guesses are displayed
# If the number is a highscore for the specific user, the Mongo database is updated with that score (update func in mongo.py)
@commands.command(name="guess")
async def _guess(ctx):
  await ctx.send(f"<@{ctx.author.id}> initiated the guess game!  Please guess a number from **1 - 100**! :question:")
  val = randint(1, 100) # get random val
  original_user = ctx.author # get the user to be checked in helper function
  user_guess = [await get_guess(ctx, original_user)]
  counter = 1 # intialize counter at 1, guess was already made above ^^

  # Loop continues to iterate until the guess is hit
  # Within the loop:
  # Increase the counter
  # If the value guessed is too high, say its too high
  # If the value guessed is too low, say its too low 
  # Display the values already guessed
  while(val != user_guess[-1]): 
    counter += 1
    if user_guess[-1] == -1:
      return
    elif val > user_guess[-1]:
      await ctx.send(f"Incorrect <@{ctx.author.id}>!  The number is **larger**!  You've guessed {user_guess} so far.")
    else:
      await ctx.send(f"Incorrect <@{ctx.author.id}>!  The number is **smaller**!   You've guessed {user_guess} so far.")
    user_guess.append(await get_guess(ctx, original_user))
  await ctx.send(
      f'''Correct <@{ctx.author.id}>!  The number was **{val}**!  It took you **{counter}** {"guesses" if counter > 1 else "guess"} :trophy:!''')
  # update the database, assume name as Username#ID
  # in discord, everyone has a unique username+id, so no need to
  # check by ids, but only name
  await update_guesshs(ctx, (f'{ctx.author.name}#{ctx.author.discriminator}'), counter)
  