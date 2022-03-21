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

# ----------------------------------------------------------------------------------------------------------------------

# CloneCord Bot V6 BETA by REKULOUS with help from taskylizard & Razorback! GClone made by Donwa on GitHub. Original Discord "GClone-Bot" by KushTheApplusser!

# Bot tested by MineRocker, Saaz, REKULOUS, and KushTheApplusser. Inspired by Telegram GClone, GDrive, and Mirror Bots.
# Also inspired by RoshanConnor and Tommmmyums GClone Batch Script for Windows.
# Thank you to all the testers, devs, and all the people over at BIOHAZARD, FREEMEDIAHECKYEAH, The MegaDrive! Thank you to the users of this bot too!

# If you want to help with the development of this bot, you can fork it on GitHub, edit the code you think needs work / add a feature, and create a pull request! Doing this helps me a lot!

import asyncio
import logging
import os
import platform
import subprocess
import sys
import time

import discord
from discord.ext import commands
from dotenv import load_dotenv

# Change CMD Text Color to Cyan, and Change CMD / Python Window Title Name
os.system(
    "title CloneCord Discord Bot V6 BETA by REKULOUS. Original code by KushTheApplusser"
)
os.system("color 0B")

# Fetch .env configuration. DO NOT TOUCH
if not os.path.isfile(".env"):
    sys.exit(
        "Your Discord bot '.env' was not found! Please add it and try again. Make sure you CD into the directory of this Python script before you run it and check .env is in there as well!\n\nYour bot config needs to have a prefix and a token for your bot to function and run. Make sure you also have edited your rclone.conf file in Notepad or a Text Editor to get your Service Accounts!"
    )
else:
    load_dotenv()

    TOKEN = os.getenv("TOKEN")
    PREFIX = os.getenv("PREFIX")

# Some sweet bot logging. I don't think it logs GClone commands and stuff like that
logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="bot.log", encoding="utf-8", mode="w")
handler.setFormatter(
    logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
)
logger.addHandler(handler)

# Bot prefix set to the one in your config.json file. Don't modify or touch this!
bot = commands.Bot(command_prefix=PREFIX)

# Print this if the bot is ready and start bot status + give GClone details.
@bot.event
async def on_ready():
    print(
        "<===============================|| Running CloneCord Version 5 BETA! ||===============================>"
    )
    print("Connected to bot: {}".format(bot.user.name))
    print("Bot ID: {}".format(bot.user.id))
    print("CloneCord is Ready!")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=PREFIX + "help to get help! CloneCord V6 BETA",
        )
    )
    print("CloneCord Status Ready!")
    print("Python Version: {}".format(platform.python_version()))
    print("Discord.py API version: {}".format(discord.__version__))
    print("GClone Version:")
    subprocess.run(["gclone", "version"])
    print("____________________")
    print("GClone Remotes:")
    print()
    subprocess.run(["gclone", "listremotes"])

@bot.check
async def globally_block_dms(ctx):
    return ctx.guild is not None

# GClone Folder / File Clone Command
@bot.command()
@commands.cooldown(1, 140, commands.BucketType.user)
async def clone(ctx, source, destination):
    s1 = "{" + source + "}"
    d1 = "{" + destination + "}"
    await ctx.send(
        "***Check the destination folder in 5 minutes if your clone is couple terabytes. If your clone is less than a terabyte, the clone will be complete within a couple of seconds!***"
    )
    proc = await asyncio.create_subprocess_exec(
        "gclone",
        "copy",
        f"GC:{s1}",
        f"GC:{d1}",
        "--transfers",
        "50",
        "-vP",
        "--stats-one-line",
        "--stats=15s",
        "--ignore-existing",
        "--drive-server-side-across-configs",
        "--drive-chunk-size",
        "128M",
        "--drive-acknowledge-abuse",
        "--drive-keep-revision-forever",
    )
    await proc.wait()
    await ctx.send("**Cloning Complete** --- https://drive.google.com/drive/folders/{destination}")

# GClone Folder / File Move Command
@bot.command()
@commands.cooldown(1, 140, commands.BucketType.user)
async def move(ctx, source, destination):
    s1 = "{" + source + "}"
    d1 = "{" + destination + "}"
    await ctx.send(
        "***Check the destination folder in 5 minutes if your transfer is couple terabytes. If your transfer is less than a terabyte, the clone will be complete within a couple of seconds!***"
    )
    proc = await asyncio.create_subprocess_exec(
        "gclone",
        "move",
        f"GC:{s1}",
        f"GC:{d1}",
        "--transfers",
        "50",
        "--tpslimit-burst",
        "50" "--checkers",
        "10",
        "-vP",
        "--stats-one-line",
        "--stats=15s",
        "--ignore-existing",
        "--drive-server-side-across-configs",
        "--drive-chunk-size",
        "128M",
        "--drive-acknowledge-abuse",
        "--drive-keep-revision-forever",
        "--fast-list",
    )
    await proc.wait()
    await ctx.send(f"**File Transfers Completed** --- https://drive.google.com/drive/folders/{destination}")

# GClone Sync Command
@bot.command()
@commands.cooldown(1, 140, commands.BucketType.user)
async def sync(ctx, source, destination):
    s1 = "{" + source + "}"
    d1 = "{" + destination + "}"
    await ctx.send(
        "***CloneCord is syncing... it should be done syncing in a couple of minutes!***"
    )
    proc = await asyncio.create_subprocess_exec(
        "gclone",
        "sync",
        f"GC:{s1}",
        f"GC:{d1}",
        "--transfers",
        "50",
        "--tpslimit-burst",
        "50",
        "--checkers",
        "10",
        "-vP",
        "--stats-one-line",
        "--stats=15s",
        "--drive-server-side-across-configs",
        "--drive-chunk-size",
        "128M",
        "--drive-acknowledge-abuse",
        "--drive-keep-revision-forever",
        "--fast-list",
    )
    await proc.wait()
    await ctx.send(f"**Sync Completed** --- https://drive.google.com/drive/folders/{destination}")


# GClone Empty / Clear Directory Command
@bot.command()
@commands.cooldown(1, 140, commands.BucketType.user)
async def emptdir(ctx, source):
    s1 = "{" + source + "}"
    await ctx.send(
        "*CloneCord is emptying the directory... it should be done in around 5 minutes if your directory is big!* **If you are worried about losing your deleted files forever, don't worry! You can recover stuff from your trash can!**"
    )
    proc = await asyncio.create_subprocess_exec(
        "gclone", "delete", f"GC:{s1}", "-vP", "--drive-trashed-only", "--fast-list"
    )
    await proc.wait()
    await ctx.send(f"**Emptying Directory Completed** --- https://drive.google.com/drive/folders/{source}")


# GClone md5sum file creation for all the objects in a directory
@bot.command()
@commands.cooldown(1, 140, commands.BucketType.user)
async def md5(ctx, source):
    s1 = "{" + source + "}"
    await ctx.send("***Producing MD5 Hash, please wait...***")
    proc = await asyncio.create_subprocess_exec(
        "gclone", "md5sum", f"GC:{s1}", "--fast-list"
    )
    await proc.wait()
    await ctx.send(f"**Finished Producing MD5** --- https://drive.google.com/drive/folders/{source}")

# GClone Remove Empty Directories
@bot.command()
@commands.cooldown(1, 140, commands.BucketType.user)
async def rmdi(ctx, source):
    s1 = "{" + source + "}"
    await ctx.send(
        "*Removing empty directories... this should take a few seconds or more.* **If you want to recover your empty folders, don't worry, they will be in your trash can!**"
    )
    proc = await asyncio.create_subprocess_exec(
        "gclone",
        "rmdirs" f"GC:{s1}",
        "-v",
        "--stats-one-line",
        "--stats=15s",
        "--fast-list",
    )
    await proc.wait()
    await ctx.send(f"**Finished removing empty dirs** --- https://drive.google.com/drive/folders/{source}")

# GClone Dedupe Files / Folders
@bot.command()
@commands.cooldown(1, 140, commands.BucketType.user)
async def dedupe(ctx, source):
    s1 = "{" + source + "}"
    await ctx.send(
        "*Deduplicating files... this should take a few seconds or more.* **If you want to recover your files / folders, don't worry, they will be in your trash can!**"
    )
    proc = await asyncio.create_subprocess_exec(
        "gclone", "dedupe", "--dedupe-mode", "newest", f"GC:{s1}", "-v", "--fast-list"
    )
    await proc.wait()
    await ctx.send(
        "**Finished Dedupe** --- https://drive.google.com/drive/folders/{}".format(
            source
        )
    )


# GClone Create Directory
@bot.command()
@commands.cooldown(1, 140, commands.BucketType.user)
async def mkdir(ctx, source):
    s1 = "{" + source + "}"
    await ctx.send("***Creating directory...***")
    proc = await asyncio.create_subprocess_exec("gclone", "mkdir", f"GC:{s1}")
    await proc.wait()
    await ctx.send(
        "**Created directory** --- https://drive.google.com/drive/folders/{}".format(
            source
        )
    )


# GClone Purge Folders
@bot.command()
@commands.cooldown(1, 140, commands.BucketType.user)
async def purge(ctx, source):
    s1 = "{" + source + "}"
    await ctx.send("***Purging directory...***")
    proc = await asyncio.create_subprocess_exec(
        "gclone",
        "purge",
        f"GC:{s1}",
        "-vP",
        "--stats-one-line",
        "--stats=15s",
        "--fast-list",
    )
    await proc.wait()
    await ctx.send(
        "**Purged Directory** --- https://drive.google.com/drive/folders/{}".format(
            source
        )
    )


# CloneCord Error Messages to make the bot have a command cooldown and send error messages about invalid commands / arguments
@clone.error
@move.error
@sync.error
@emptdir.error
@md5.error
@rmdi.error
@dedupe.error
@mkdir.error
@purge.error
# All commands by default have a 140 Second Cooldown. If you want, you can remove the code before "else:" to remove cooldowns. Don't remove @<command>.error stuff!
# Not recommended to remove this if you are using this bot in a server with other people than you though.
# Be sure to remove the @commands.cooldown(1, 140, commands.BucketType.user) stuff too in the code for commands if you want to remove cooldowns.
async def error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(error)
        return
    else:
        await ctx.send(
            "**There is an error in your command:** `{}`".format(error)
            + "\n**Use `?help` or `?help <command>` to get help on commands!**"
        )


# = = = = {EXTRA COMMANDS / BOT UTILITY} = = = =

# Ping Command to get the bot's current websocket and API latency
@bot.command()
async def ping(ctx: commands.Context):
    start_time = time.time()
    message = await ctx.send("Pinging...")
    end_time = time.time()

    await message.edit(
        content=f":ping_pong:    *Pong!*    **`{round(bot.latency * 1000)}ms`**    :ping_pong:\n:ping_pong:    **API Ping:** **`{round((end_time - start_time) * 1000)}ms`**  :ping_pong:"
    )


# Start the bot, DO NOT TOUCH!
bot.run(TOKEN, reconnect=True)
