import discord
from discord.ext import commands
from colorama import init, Fore
import json

print(Fore.YELLOW + 'DISCORD BOT TROL TOOL' )
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

with open('config.json' , 'r') as f:
    config = json.load(f)
token = config['token']
channel_id = config['channel_id']

@bot.event
async def on_ready():
    print(Fore.LIGHTCYAN_EX + f'BOT HAS BEEN STARTED \nLogged in as {bot.user}')

@bot.event
async def on_message(msg):
    if msg.channel.id == channel_id:
        if msg.content.startswith(f'<@{bot.user.id}>'):
            print(Fore.LIGHTBLUE_EX + 'Message Received By' , msg.author , "\nMessage Content" , msg.content )
            ry = input(Fore.LIGHTGREEN_EX + 'What To Reply? ')
            embed = discord.Embed(title=f"Response From Ai\n{ry}" , description="Loda Ai Knows Everything" , color=discord.Color.green())
            embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7cA1KHFA4ciXmWJfAA6Yk4bFE0GusgeRHWw&s")
            await msg.channel.send(embed=embed)
            print(Fore.LIGHTYELLOW_EX + 'Reply Sent')
            print(Fore.LIGHTRED_EX + 'Waiting For Next Commend...')


bot.run(token)
