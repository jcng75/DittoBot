from discord.ext import commands
from random import randint

def setup(bot):
  bot.add_command(_choose)
  bot.add_command(_best)

# given a range "a-b", we would take these values and plug it into the randomint method
#  afterwards, we return the value
def choose(string):
  r = string.split("-")
  if len(r) != 2:
    return "Incorrect syntax!"
  elif int(r[0]) > int(r[1]):
    return "Please flip the bounds!; a-b -> b-a"
  return randint(int(r[0]), int(r[-1]))

# calls choose command

@commands.command(name="choose")
async def _choose(ctx):
  rango = str(ctx.message.content).split(' ', 1)[1]
  print(f'Choose command called from {ctx.author}, {rango}')
  await ctx.send(choose(rango))

# secret command
@commands.command(name="bestgirl", aliases=['bg', 'best'])
async def _best(ctx):
  await ctx.send("Hyoon is the best girl :heart_eyes:")
  await ctx.send("https://cdn.discordapp.com/attachments/672809407964381184/930958198867910736/unknown.png")
  await ctx.send("https://cdn.discordapp.com/attachments/672809407964381184/930957951898890361/unknown.png")