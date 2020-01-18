# bot.py
import os
import json

import discord
from discord.ext.commands import Bot
from dotenv import load_dotenv
import random

BOT_PREFIX = ("?", "!", ".")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
parsed_json = (json.loads(open("url.json", "r").read()))


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content is not None and len(message.content) > 0 and message.content[0][:1] in BOT_PREFIX:
        if message.content[1:] == "help":
            embed = discord.Embed(title="Current Configuration",
                                  description="https://github.com/Y0ngg4n/Techtelmechtel-Discord-Bot/blob/master/url.json")
            await message.channel.send(embed=embed)
            return

        if message.mentions is not None and len(message.mentions) > 0 and message.channel.nsfw:
            args = message.content[1:].split(' ');
            action = args[0]
            if action.endswith("ss"):
                action = action + "es"
            else:
                action = action + "s"

            if args[1] != "<@!" + str(message.mentions[0].id) + ">":
                embed = discord.Embed(
                    description=message.author.name + " " + action + " the " + args[1] + " of " + message.mentions[
                        0].mention)
                embed.set_image(url=random.choice(parsed_json[args[0]][args[1]]))
            else:
                embed = discord.Embed(
                    description=message.author.name + " " + action + " " + message.mentions[0].mention)
                embed.set_image(url=random.choice(parsed_json[args[0]]["main"]))

            await message.channel.send(embed=embed)
        # else:
        #     embed = discord.Embed(description="Please make shure that you are in a NSFW Channel and you enter the command like this:\n```!command @Mention\nor\n!command command @Mention```")
        #     await message.channel.send(embed=embed)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
