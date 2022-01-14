from discord.ext import commands
from math import log, sqrt
from re import compile 
from utility import replace_function
from numpy import pi, e

def setup(bot):
  bot.add_command(_calculate)

def calc(string):
  # list of inputted characters to replace with it's python complement
  fix_list = {"x":"*", "^": "**", "=": "=="}
  # replace them using this function
  new_string = replace_function(string, fix_list)
  # get all possible "illegal characters using regex"
  prog = compile(r"[a-zA-Z]+")
  check_list = prog.findall(new_string)
  # list of words that are allowed, any others are not
  suitable_words = ["log", "sqrt", "pi", "e"]
  # using for each loop, check if these regex patterns are in the 
  # suitable words list.  If invalid, return "invalid expression"
  for pattern in check_list:
    if pattern not in suitable_words:
      return "Invalid expression!"
  try:
    return eval(new_string)
  except:
    return "Invalid expression!"


# calls the calculate command

@commands.command(name="calculate", aliases=['c', 'calc'])
async def _calculate(ctx):
  expression = str(ctx.message.content).split(' ', 1)[1]
  print(f'Calculate command called from {ctx.author.name}, {expression}')
  await ctx.send(calc(expression))