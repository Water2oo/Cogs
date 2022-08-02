import discord
from discord.ext import commands

client = discord.Client()

if message.content.startswith(
'https://discord.gg'):
      await message.delete()
      await message.author.send("This Is What Is Will DM The User That Sent The Link")
