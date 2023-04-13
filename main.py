import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Le bot est prêt  ')

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.lower() == 'quoi':
        await message.channel.send('coubeh')

bot.run('TOKEN ICI')