import discord
from discord.ext import commands
import youtube_dl

class music(commands.Cog):

  def __init__(self, client):
    self.client = client
  
  @commands.command()

  async def play(self, cmd, url):
