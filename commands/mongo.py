import os
from discord.ext import commands
from pymongo import MongoClient
import certifi
 
# Setup mongoDB client
ca = certifi.where()
my_secret = os.environ['mongo_pass']
cluster = MongoClient(f"mongodb+srv://jcng:{my_secret}@cluster0.j8dzn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)
db = cluster["Discord"]
collection = db["DittoBot"]

def setup(bot):
    bot.add_command(_highscore)
    bot.add_command(_tophighscore)

# helper function to update highscore from guess command
# takes discord username and value (number of guesses)
# If the user is not in the database, create a new user and set the score as val
# If the user is in the database and the score value is higher than the inputted val, update the highscore stored
# ctx.send commands added for style
async def update_guesshs(ctx, name, val):
  if val == 1:
    ctx.send("You are a legend :scream_cat:")
  post = {"name": name, "score": val}
  result = collection.find_one({"name": name})
  if result == None:
    print(f'Highscore! User {name} doesn\'t exist in the database, adding new user!')
    await ctx.send("New Highscore! Congrats champion :sunglasses:!")
    collection.insert_one(post)
    return
  elif result["score"] > val:
    await ctx.send("New Highscore! Congrats champion :sunglasses:!")
    print(f'Highscore!  User {name} already exists, updating user!')
    collection.update_one({"name": name}, {"$set":{"score": val}})
    return
  await ctx.send(f'Your current highscore is: **{result["score"]}**! Try to beat it next time :triumph:!')

# highscore command to get user hs
# finds "score" field from database given ctx.author.name + # + ctx.author.discriminator
# if user doesn't exist in db, ctx.send that we can't find user
@commands.command(name="highscore", aliases=['hs'])
async def _highscore(ctx):
  result = collection.find_one({"name": f"{ctx.author.name}#{ctx.author.discriminator}"})
  if result == None:
    await ctx.send(f'<@{ctx.author.id}>, you don\'t have any highscores! :sob:')
    return
  await ctx.send(f'<@{ctx.author.id}>, your current guess highscore is: **{result["score"]}** :trophy:!')

# tophs finds tophighscore of the server!
# tophs can be multiple users, so we must first find the highscore
# afterwards, we do a for each loop on each post to check if they have the highscore
# if they do, we append the user to a list
# finally, return the list of users and the highscore
@commands.command(name="tophighscore", aliases=['tophs'])
async def _tophighscore(ctx):
  highscore = collection.find_one(sort=[("score", 1)])["score"]
  results = collection.find()
  users = ""
  for result in results:
    check = result["score"]
    if check == None:
      continue
    elif check == highscore:
      users += (f'{result["name"]}, ')
  users = users.rstrip(", ")
  users += "!  :100:"
  await ctx.send(f'The current highscore of the server is **{highscore}**, held by:')
  await ctx.send(users)





