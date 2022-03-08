# Imports
from urllib.parse import urlparse
from discord.ext import commands

# Create bot
token = "TOKEN"
client = commands.Bot(command_prefix=";")


# External functions
def replace_links(messagecontent):  # Replace links with privacy-friendly links
    originalUrls = []    # Normal URLs
    redirectedUrls = []  # Privacy-friendly URLs
    words = []  # Words in the message

    for word in messagecontent.split(" "):  # Remove new lines
        wordsNL = word.split("\n")
        words.append(wordsNL[0])

    redirectDictionary = {  # "normal.link": "private.link"
        "youtu.be": "redirect.invidious.io",
        "youtube.com": "redirect.invidious.io",
        "twitter.com": "nitter.net",
        "instagram.com": "bibliogram.snopyta.org",
        "reddit.com": "libredd.it"
    }

    for word in words:                  # For every word,
        if "http" in word:              # Indicates that it's a link
            originalUrls.append(word)   # Append to list of normal URLs

    for url in originalUrls:        # For every normal URL,
        urlInfo = urlparse(url)     # retrieve website name
        website = urlInfo.netloc
        if website in redirectDictionary.keys():                                 # If there's a private alternative,
            redirectedUrl = url.replace(website, redirectDictionary[website])    # replace URL with private version
            redirectedUrls.append(redirectedUrl)                                 # Add private URl to list

    replyString = "**Privacy friendly versions:**\n\n"  # Send a message containing
    for i in range(0, len(redirectedUrls)):             # private URLs
        replyString += redirectedUrls[i] + "\n"
    return replyString, redirectedUrls


# Client events
@client.event
async def on_ready():
    print("Privacy bot online.")


@client.event
async def on_message(message):
    author = message.author
    if author == client.user:
        return
    else:
        replyContent, redirectedUrls = replace_links(message.content)  # Reply + list of privacy-friendly URLs
        if redirectedUrls:  # If there are any privacy-friendly alternatives
            await message.reply(replyContent, mention_author=False)  # Reply with replyContent + don't mention them


client.run(token)
