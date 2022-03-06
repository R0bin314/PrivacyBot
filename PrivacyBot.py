from urllib.parse import urlparse
from discord.ext import commands

token = "TOKEN"
client = commands.Bot(command_prefix=";")


def replace_links(messagecontent):
    originalUrls = []
    redirectedUrls = []
    words = []

    for word in messagecontent.split(" "):
        wordsNL = word.split("\n")
        words.append(wordsNL[0])

    redirectDictionary = {
        "youtu.be": "redirect.invidious.io",
        "youtube.com": "redirect.invidious.io",
        "twitter.com": "nitter.net",
        "instagram.com": "bibliogram.snopyta.org",
        "reddit.com": "libredd.it"
    }

    for word in words:
        if "http" in word:
            originalUrls.append(word)

    for url in originalUrls:
        urlInfo = urlparse(url)
        website = urlInfo.netloc
        if website in redirectDictionary.keys():
            redirectedUrl = url.replace(website, redirectDictionary[website])
            redirectedUrls.append(redirectedUrl)

    replyString = "**Privacy friendly versions:**\n\n"
    for i in range(0, len(redirectedUrls)):
        replyString += redirectedUrls[i] + "\n"
    return replyString, redirectedUrls


@client.event
async def on_ready():
    print("Privacy bot online.")


@client.event
async def on_message(message):
    try:
        author = message.author
        if author == client.user:
            return
        else:
            replyContent, redirectedUrls = replace_links(message.content)
            if redirectedUrls:
                await message.reply(replyContent, mention_author=False)

    except TypeError:
        return


client.run(token)
