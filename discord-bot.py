import discord
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()

@client.event
async def on_ready():
    datum = datetime.now().strftime("%A - %d-%m-%Y - %X")
    print(f"""Eingeloggt als {client.user.name};\nID:{client.user.id};\nDatum: {datum};\n""")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    async def vid_example():
        await message.delete()
        link = "https://www.youtube.com/watch?v=bxqLsrlakK8"
        await message.channel.send(f"""{message.author.mention} \nVideo: {link}""")

    async def gif_example():
        link = "https://giphy.com/gifs/rick-roll-gotcha-mod-miny-kFgzrTt798d2w"
        await message.reply(f"""GIF: {link}""")

    async def pic_example():
        link = "https://imgl.krone.at/scaled/2347804/v0780ce/og_image.jpg"
        await message.reply(f"""Picture: {link}""")

    async def txt_example():
        link = "Never gonna give you up"
        await message.reply(f"""Text: {link}""")

    async def help():
        embed = discord.Embed(title="Hilfemenu", description=f"""Auflistung der Befehle {message.author.mention}""", color=0x014b06)
        embed.add_field(name="!vid", value="Video", inline="True")
        embed.add_field(name="!gif", value="GIF", inline="True")
        embed.add_field(name="!pic", value="Bild", inline="True")
        embed.add_field(name="!txt", value="Text", inline="True")
        embed.add_field(name="!help", value="Dieses Hilfemenu", inline="True")
        await message.delete()
        await message.channel.send(embed=embed)

    functions = {"!vid": vid_example, "!gif": gif_example, "!pic": pic_example, "!txt": txt_example, "!help": help}
    commands = set(functions.keys())
    msg = set(message.content.lower().split())
    cmds = msg.intersection(commands)
    for cmd in cmds:
        await functions[cmd]()

client.run(os.getenv('DISCORD_TOKEN'))