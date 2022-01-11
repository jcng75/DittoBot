import discord
from discord.ext import commands
# import youtube_dl

connect_bot = None
def setup(bot):
  global connect_bot
  connect_bot = bot
  bot.add_command(_join)
  bot.add_command(_leave)

@commands.command(name="join")
async def _join(ctx):
    guild = ctx.guild # discord server
    voice_channel_name = str(ctx.author.voice.channel)
    channel = discord.utils.get(guild.voice_channels, name=voice_channel_name) # <---- Object: Channel, the channel the user is in
    voice = discord.utils.get(connect_bot.voice_clients, guild=guild) # <---- Object: Voice_Client.channel, Voice_Client.guild
    if not voice: # if not in voice chat connect
        await channel.connect()
        await ctx.message.add_reaction("👌")
        return
    
    if voice.channel != channel: # if not in the right voice chat move
        await voice.move_to(channel)
        await ctx.message.add_reaction("👌")
        return
    
    await ctx.send(f"Already connected to {voice.channel}")    

@commands.command(name="leave")
async def _leave(ctx):
  guild = ctx.guild
  voice_channel_name = str(ctx.author.voice.channel)
  channel = discord.utils.get(guild.voice_channels, name=voice_channel_name)
  voice = discord.utils.get(connect_bot.voice_clients, channel=channel, guild=guild)
  if not discord.utils.get(connect_bot.voice_clients, guild=guild):
      await ctx.send("Not in a voice channel!")
      return
  if voice:
    await voice.disconnect()
    await ctx.message.add_reaction("👋")
    return
  await ctx.send("Not in the same voice channel!")

# @commands.command(name="play")
  # async def _play(ctx):
