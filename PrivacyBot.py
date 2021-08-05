import discord
from discord.ext import commands

token="TOKEN"
client=commands.Bot(command_prefix=";")

#TODO: use trigger word method so instead of doing
#if "youtu.be", etc, make it if triggerword in messagecontent, return with trigger word + replacement

def replace_links(messagecontent):
    
    if "youtu.be" in messagecontent:
        return ("youtu.be","invidious.io")
    if "youtube.com" in messagecontent:
        return("youtube.com","invidious.io")
    elif "twitter.com" in messagecontent:
        return ("twitter.com","nitter.net")
    elif "instagram.com" in messagecontent:
        return ("instagram.com","bibliogram.snopyta.org")
    elif "reddit.com" in messagecontent:
        return ("reddit.com","libredd.it")
    else:
        return
@client.event
async def on_ready():
    print("Privacy bot online.")

@client.event
async def on_message(message):
    try:
        author = message.author
        authorid = message.author.id
        if author == client.user:
            return
        else:
            if "goatsedance.com" in message.content:
                await message.reply("**DON'T CLICK ON THE REPLIED LINK. IT'S A SHOCK SITE.**\nAlso, congrats on finding this easter egg!\nHere's a family friendly version: https://hamster.dance/hamsterdance/ <:Yui:817547924707082280>") 
            await message.reply("Privacy friendly version: " + (message.content).replace((replace_links(message.content))[0],(replace_links(message.content))[1]), mention_author=False)
    except TypeError:
        return
client.run(token)
