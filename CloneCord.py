# This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

# CloneCord Bot V4 BETA by KushTheApplusser and REKULOUS with help from Tasky Lizard & Razorback! GClone made by Donwa on GitHub.
import json
import logging
import subprocess
import sys
import platform
import os
import random
import struct
import time
from time import sleep
from typing import Optional

import discord
from discord.ext import commands
from discord.utils import get


# Get config.json
if not os.path.isfile("config.json"):
    sys.exit("Your Discord bot 'config.json' was not found! Please add it and try again. Make sure you CD into the directory of this Python script before you run it and check config.json is in there as well!")
else:
    with open("config.json", "r") as config:
        data = json.load(config)
        token = data["token"]
        prefix = data["prefix"]


# Sweet ass bot logging
logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="bot.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

bot = commands.Bot(command_prefix='?')



# Print this if the bot is ready and start bot status
@bot.event
async def on_ready():
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))
    print('CloneCord is Ready!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="?help to get help! CloneCord V4 BETA"))
    print('CloneCord Status Ready!')
    print('Python Version: {}'.format(platform.python_version()))
    print('Discord.py API version: {}'.format(discord.__version__))
    print("==================================================================================================================================================")
    print("--------------------")
    print("GClone Remotes:")
    print()
    subprocess.run(
        f"gclone listremotes"
    )
    print("--------------------")
    print("==================================================================[ALL READY!!!]==================================================================")


# Block commands in bot DMs
@bot.check
async def globally_block_dms(ctx):
    return ctx.guild is not None


# Remove default help message and replace it with embed one
bot.remove_command("help")
@bot.command()
async def help(ctx, command: Optional[str]):
    list_of_commands = [
        {
            "command": "clone",
            "value": "<source id> <destination id>"
        },
        {
            "command": "move",
            "value": "<source id> <destination id>"
        },
        {
            "command": "sync",
            "value": "<source id> <destination id>"
        },
        {
            "command": "emptdir",
            "value": "<source id>"
        },
        {
            "command": "md5",
            "value": "<source id>"
        },
        {
            "command": "rmdi",
            "value": "<source id>"
        },
        {
            "command": "dedupe",
            "value": "<source id>"
        },
        {
            "command": "mkdir",
            "value": "<source id>"
        },
        {
            "command": "purge",
            "value": "<source id>"
        },
        {
            "command": "ping",
            "value": ""
        },
    ]

    helpEmbed = discord.Embed(
        title="Here are the available bot commands:",
        description="**CloneCord is a Discord bot made to run GClone, an RClone mod for Multiple Service Account support in Discord.** *Note:* All commands below are performed synchronously, so the bot can only run one command at a time!"
        ,color=0x87CEEB)
    helpEmbed.set_author(
        name="CloneCord V4 BETA",
        icon_url="https://1.bp.blogspot.com/-M5PLcSana6M/XgBHF7jUjiI/AAAAAAAAUzs/S24qhuijluwKlzIOnc2gntoI-U83ZsrJACLcBGAsYHQ/s1600/rclone_logo.png")
    helpEmbed.set_footer(
        text="Bot originally created by Kush The A++er#2976. Revamped version by REKULOUS#5580. Thanks to Pratyush.#6969 and Razorback#4637 for the help!",
        icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
    helpEmbed.add_field(
        name='help',
        value="Shows this message. Message ?help <command> to get more info on a command",
        inline=False)
    helpEmbed.add_field(
        name='clone',
        value="Clone files / folders to other places"
    )
    helpEmbed.add_field(
        name='move',
        value="Move files / folders to other places"
    )
    helpEmbed.add_field(
        name='sync',
        value="Sync source links to destination links"
    )
    helpEmbed.add_field(
        name='emptdir',
        value="Empty folder contents to the trash can"
    )
    helpEmbed.add_field(
        name='md5',
        value="Produce an MD5 File hash for all contents in a folder"
    )
    helpEmbed.add_field(
        name='rmdi',
        value="Remove empty directories"
    )
    helpEmbed.add_field(
        name='dedupe',
        value="Deduplicate files / folders"
    )
    helpEmbed.add_field(
        name='mkdir',
        value="Create directories / folders"
    )
    helpEmbed.add_field(
        name='purge',
        value="Delete a directory and all its contents" 
    )
    helpEmbed.add_field(
        name='ping',
        value="Get the bot's current websocket and API latency"
    )
    if command:
        for com in list_of_commands:
            if com["command"] == command:
                embed1 = discord.Embed(title=command, description=f"?{command} {com['value']}",color=0x87CEEB)
                embed1.set_author(name="CloneCord V4 BETA",icon_url="https://1.bp.blogspot.com/-M5PLcSana6M/XgBHF7jUjiI/AAAAAAAAUzs/S24qhuijluwKlzIOnc2gntoI-U83ZsrJACLcBGAsYHQ/s1600/rclone_logo.png")
                embed1.set_footer(text="Source and Destination IDs can be found by finding the jumbled up letters & numbers at the end of a GDrive folder / file URL. Example: 1Zsh8DctvvWZzJgiEI_sqxVoxvKv9VsYp",icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Google_Drive_logo.png/1200px-Google_Drive_logo.png")
                await ctx.send(embed=embed1)
    else:
        await ctx.send(embed=helpEmbed)




# = = = = {GCLONE BOT COMMANDS } = = = =


# GClone Folder / File Clone Command
@bot.command()
async def clone(ctx, source, destination):
    s1 = "{" + source + "}"
    d1 = "{" + destination + "}"
    await ctx.send(
        "***Check the destination folder in 5 minutes if your clone is couple terabytes. If your clone is less than a terabyte, the clone will be complete within a couple of seconds! The bot will go offline during the clone!***"
    )
    subprocess.run(
        f"gclone copy GC:{s1} GC:{d1} --transfers 50 -vP --stats-one-line --stats=15s --ignore-existing --drive-server-side-across-configs --drive-chunk-size 128M --drive-acknowledge-abuse --drive-keep-revision-forever"
    )
    sleep(2)
    await ctx.send("**Cloning Complete** --- https://drive.google.com/drive/folders/{}".format(destination))
    print("===========================================================================[CLONING COMPLETE]===========================================================================")


# GClone Folder / File Move Command
@bot.command()
async def move(ctx, source, destination):
    s1 = "{" + source + "}"
    d1 = "{" + destination + "}"
    await ctx.send(
        "***Check the destination folder in 5 minutes if your transfer is couple terabytes. If your transfer is less than a terabyte, the clone will be complete within a couple of seconds! The bot will go offline during the transfer!***"
    )
    subprocess.run(
        f"gclone move GC:{s1} GC:{d1} --transfers 50 --tpslimit-burst 50 --checkers 10 -vP --stats-one-line --stats=15s --ignore-existing --drive-server-side-across-configs --drive-chunk-size 128M --drive-acknowledge-abuse --drive-keep-revision-forever --fast-list"
    )
    sleep(1)
    await ctx.send("**File Transfers Completed** --- https://drive.google.com/drive/folders/{}".format(destination))
    print("===========================================================================[FILE TRANSFERS COMPLETED]===========================================================================")


# GClone Sync Command
@bot.command()
async def sync(ctx, source, destination):
    s1 = "{" + source + "}"
    d1 = "{" + destination + "}"
    await ctx.send(
        "***CloneCord is syncing... it should be done syncing in a couple of minutes! The bot will go offline during the sync!***"
    )
    subprocess.run(
        f"gclone sync GC:{s1} GC:{d1} --transfers 50 --tpslimit-burst 50 --checkers 10 -vP --stats-one-line --stats=15s --drive-server-side-across-configs --drive-chunk-size 128M --drive-acknowledge-abuse --drive-keep-revision-forever --fast-list"
    )
    sleep(1)
    await ctx.send("**Sync Completed** --- https://drive.google.com/drive/folders/{}".format(destination))
    print("===========================================================================[SYNC COMPLETED]===========================================================================")


# GClone Empty / Clear Directory Command
@bot.command()
async def emptdir(ctx, source):
    s1 = "{" + source + "}"
    await ctx.send(
        "*CloneCord is emptying the directory... it should be done in around 5 minutes if your directory is big!* **If you are worried about losing your deleted files forever, don't worry! You can recover stuff from your trash can! The bot will go offline during emptying the directory!**"
    )
    subprocess.run(
        f"gclone delete GC:{s1} -vP --drive-trashed-only --fast-list"
    )
    sleep(1)
    await ctx.send("**Emptying Directory Completed** --- https://drive.google.com/drive/folders/{}".format(source))
    print("===========================================================================[FINISHED EMPTYING DIRECTORY]===========================================================================")


# GClone md5sum file creation for all the objects in a directory
@bot.command()
async def md5(ctx, source):
    s1 = "{" + source + "}"
    await ctx.send(
        "***Producing MD5 Hash, please wait...***"
    )
    await ctx.send(
        "**The bot will go offline during the MD5Sum!**"
    )
    subprocess.run(
        f"gclone md5sum GC:{s1} --fast-list"
    )
    sleep(1)
    await ctx.send("**Finished Producing MD5** --- https://drive.google.com/drive/folders/{}".format(source))
    print("===========================================================================[FINISHED PRODUCING MD5]===========================================================================")


# GClone Remove Empty Directories
@bot.command()
async def rmdi(ctx, source):
    s1 = "{" + source + "}"
    await ctx.send(
        "*Removing empty directories... this should take a few seconds or more.* **If you want to recover your empty folders, don't worry, they will be in your trash can!**"
    )
    subprocess.run(
        f"gclone rmdirs GC:{s1} -v --stats-one-line --stats=15s --fast-list"
    )
    sleep(1)
    await ctx.send("**Finished removing empty dirs** --- https://drive.google.com/drive/folders/{}".format(source))
    print("===========================================================================[FINISHED REMOVING EMPTY DIRECTORIES]===========================================================================")


# GClone Dedupe Files / Folders
@bot.command()
async def dedupe(ctx, source):
    s1 = "{" + source + "}"
    await ctx.send(
        "*Deduplicating files... this should take a few seconds or more.* **If you want to recover your files / folders, don't worry, they will be in your trash can!**"
    )
    subprocess.run(
        f"gclone dedupe --dedupe-mode newest GC:{s1} -v --fast-list"
    )
    sleep(1)
    await ctx.send("**Finished Dedupe** --- https://drive.google.com/drive/folders/{}".format(source))
    print("===========================================================================[FINISHED DEDUPING FILES]===========================================================================")


# GClone Create Directory
@bot.command()
async def mkdir(ctx, source):
    s1 = "{" + source + "}"
    await ctx.send(
        "***Creating directory...***"
    )
    subprocess.run(
        f"gclone mkdir GC:{s1}"
    )
    sleep(1)
    await ctx.send("**Created directory** --- https://drive.google.com/drive/folders/{}".format(source))
    print("===========================================================================[CREATED DIRECTORY]===========================================================================")


# GClone Purge Folders
@bot.command()
async def purge(ctx, source):
    s1 = "{" + source + "}"
    await ctx.send(
        "***Purging directory...***"
    )
    subprocess.run(
        f"gclone purge GC:{s1} -vP --stats-one-line --stats=15s --fast-list"
    )
    sleep(1)
    await ctx.send("**Purged Directory** --- https://drive.google.com/drive/folders{}".format(source))
    print("===========================================================================[PURGED DIRECTORY]===========================================================================")


# CloneCord Error Messages
@clone.error
@move.error
@sync.error
@emptdir.error
@md5.error
@rmdi.error
@dedupe.error
@mkdir.error
@purge.error
async def error(ctx, error):
  await ctx.send("**There is an error in your command:** `{}`".format(error) + "\n**Use `?help` or `?help <command>` to get help on commands!**")



# = = = = {EXTRA COMMANDS / BOT UTILITY} = = = =

# Ping Command
@bot.command()
async def ping(ctx: commands.Context):
    start_time = time.time()
    message = await ctx.send("Pinging...")
    end_time = time.time()
    
    await message.edit(content=f":ping_pong:    *Pong!*    **`{round(bot.latency * 1000)}ms`**\n**API Ping:** **`{round((end_time - start_time) * 1000)}ms`**  :ping_pong:")
    print("||=- - - - - - - - > Pinged! < - - - - - - - -=||")


bot.run(token)
