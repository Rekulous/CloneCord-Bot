#   This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import asyncio
import logging
import os
import sys
import time

import discord
from discord.ext import commands
from dotenv import load_dotenv

if not os.path.isfile(".env"):
    sys.exit(
        "Your Discord bot '.env' was not found! Please add it and try again.\
                Make sure you CD into the directory of this Python script before you run it and check .env is in there as well!\n\n\
                Your bot config needs to have a prefix and a token for your bot to function and run. Make sure you also have edited your rclone.conf file in Notepad or a Text Editor to get your Service Accounts!"
    )
else:
    load_dotenv()

    TOKEN = os.getenv("TOKEN")
    PREFIX = os.getenv("PREFIX")


class Bot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(command_prefix=commands.when_mentioned_or(f"{TOKEN}"), **kwargs)

    async def setup_hook(self) -> None:
        pass

    async def on_ready(self) -> None:
        print(f"Logged in as {self.user}")
        await self.change_presence(
            activity=discord.Activity(
                name="with gclone", type=discord.ActivityType.playing
            )
        )


bot = Bot()


logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="bot.log", encoding="utf-8", mode="w")
handler.setFormatter(
    logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
)
logger.addHandler(handler)


@bot.command()
@commands.cooldown(1, 140, commands.BucketType.user)
async def clone(ctx, source: str, destination: str):
    await ctx.send(
        "***Check the destination folder in 5 minutes***"
    )
    proc = await asyncio.create_subprocess_exec(
        "gclone",
        "copy",
        f"GC:{source}",
        f"GC:{destination}",
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
    await ctx.send(
        f"**Cloning Complete** --- https://drive.google.com/drive/folders/{destination}"
    )


# GClone Folder / File Move Command
@bot.command()
@commands.cooldown(1, 140, commands.BucketType.user)
async def move(ctx, source: str, destination: str):
    await ctx.send(
        "***Check the destination folder!***"
    )
    proc = await asyncio.create_subprocess_exec(
        "gclone",
        "move",
        f"GC:{source}",
        f"GC:{destination}",
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
    await ctx.send(
        f"**File Transfers Completed** --- https://drive.google.com/drive/folders/{destination}"
    )


@bot.command()
@commands.cooldown(1, 140, commands.BucketType.user)
async def sync(ctx, source: str, destination: str):
    await ctx.send(
        "***CloneCord is syncing... it should be done syncing in a couple of minutes!***"
    )
    proc = await asyncio.create_subprocess_exec(
        "gclone",
        "sync",
        f"GC:{source}",
        f"GC:{destination}",
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
    await ctx.send(
        f"**Sync Completed** --- https://drive.google.com/drive/folders/{destination}"
    )


# GClone Empty / Clear Directory Command
@bot.command()
@commands.cooldown(1, 140, commands.BucketType.user)
async def emptdir(ctx, source: str):
    await ctx.send(
        "***Clearing Directory...***"
    )
    proc = await asyncio.create_subprocess_exec(
        "gclone", "delete", f"GC:{source}", "-vP", "--drive-trashed-only", "--fast-list"
    )
    await proc.wait()
    await ctx.send(
        f"**Emptying Directory Completed** --- https://drive.google.com/drive/folders/{source}"
    )


# GClone md5sum file creation for all the objects in a directory
@bot.command()
@commands.cooldown(1, 140, commands.BucketType.user)
async def md5(ctx, source: str):
    await ctx.send("***Producing MD5 Hash, please wait...***")
    proc = await asyncio.create_subprocess_exec(
        "gclone", "md5sum", f"GC:{source}", "--fast-list"
    )
    await proc.wait()
    await ctx.send(
        f"**Finished Producing MD5** --- https://drive.google.com/drive/folders/{source}"
    )


# GClone Remove Empty Directories
@bot.command()
@commands.cooldown(1, 140, commands.BucketType.user)
async def rmdi(ctx, source: str):
    await ctx.send(
        "*Removing empty directories... this should take a few seconds or more.* **If you want to recover your empty folders, don't worry, they will be in your trash can!**"
    )
    proc = await asyncio.create_subprocess_exec(
        "gclone",
        "rmdirs" f"GC:{source}",
        "-v",
        "--stats-one-line",
        "--stats=15s",
        "--fast-list",
    )
    await proc.wait()
    await ctx.send(
        f"**Finished removing empty dirs** --- https://drive.google.com/drive/folders/{source}"
    )


# GClone Dedupe Files / Folders
@bot.command()
@commands.cooldown(1, 140, commands.BucketType.user)
async def dedupe(ctx, source: str):
    await ctx.send("***Deduplicating files...***")
    proc = await asyncio.create_subprocess_exec(
        "gclone", "dedupe", "--dedupe-mode", "newest", f"GC:{source}", "-v", "--fast-list"
    )
    await proc.wait()
    await ctx.send(f"**Finished Dedupe** --- https://drive.google.com/drive/folders/{source}")

# GClone Create Directory
@bot.command()
@commands.cooldown(1, 140, commands.BucketType.user)
async def mkdir(ctx, source: str):
    await ctx.send("***Creating directory...***")
    proc = await asyncio.create_subprocess_exec("gclone", "mkdir", f"GC:{source}")
    await proc.wait()
    await ctx.send(f"**Created directory** --- https://drive.google.com/drive/folders/{source}")

# GClone Purge Folders
@bot.command()
@commands.cooldown(1, 140, commands.BucketType.user)
async def purge(ctx, source: str):
    await ctx.send("***Purging directory...***")
    proc = await asyncio.create_subprocess_exec(
        "gclone",
        "purge",
        f"GC:{source}",
        "-vP",
        "--stats-one-line",
        "--stats=15s",
        "--fast-list",
    )
    await proc.wait()
    await ctx.send(f"**Purged Directory** --- https://drive.google.com/drive/folders/{source}")

# Ping Command to get the bot's current websocket and API latency
@bot.command()
async def ping(ctx: commands.Context):
    start_time = time.time()
    message = await ctx.send("Pinging...")
    end_time = time.time()

    await message.edit(
        content=f"*Pong!*\
                **`{round(bot.latency * 1000)}ms`**\
                **API Ping:** **`{round((end_time - start_time) * 1000)}ms`**"
    )

bot.run(TOKEN)
