from discord.ext import commands
from random import randint

def setup(bot):
  bot.add_command(_choose)

# given a range "a-b", we would take these values and plug it into the randomint method
#  afterwards, we return the value
def choose(string):
  r = string.split("-")
  if len(r) != 2:
    return "Incorrect syntax!"
  elif int(r[0]) > int(r[1]):
    return "Please flip the bounds!; a-b -> b-a"
  return randint(int(r[0]), int(r[-1]))


@commands.command(name="choose")
async def _choose(ctx):
  rango = str(ctx.message.content).split(' ', 1)[1]
  print(f'Choose command called from {ctx.author}, {rango}')
  await ctx.send(choose(rango))
