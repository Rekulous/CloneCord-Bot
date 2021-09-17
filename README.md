# CloneCord-Bot
A Discord.py bot for Running GClone, an RClone mod that allows multiple Google Service Account configuration. Inspired by Telegram MirrorBots and CloneBot.

Thanks to KushTheAppluser, TaskyLizard, Cerda, and Razorback for helping me develop the bot!

Original bot and code made by KushTheAppluser / BlackBeard. [GClone](https://github.com/donwa/gclone) created by Donwa. [GClone Linux](https://github.com/AndreVuillemot160/gclone) made by Cerda

## Features
Below are the features the bot currently has of now. New commands and features will be coming soon!
- **Clone** - Clones files / folders to other places
- **Move** - Moves files / folders to other places
- **Sync** - Sync source links to destination links
- **Emptdir** - Empty folder contents to the trash can
- **MD5** - Produce an MD5 File hash for all contents in a folder
- **Rmdi** - Remove empty directories
- **Dedupe** - Deduplicate files / folders
- **MKDir** - Create directories / folders
- **Purge** - Delete a directory and all its contents
- **Ping** - Get the bot's current websocket and API latency

## Prerequisites
Before you get started, you need [Python](https://python.org) 3.7 or later to run this script. Below are some extra things you need to download / install too:

- **[GClone](https://github.com/donwa/gclone)** - Run the shell / batch script if you are on Linux to install, or add the `gclone.exe` file to your system PATH variables if you are on Windows. I think putting the script in the same directory as GClone in Windows will work as well.
- **[AutoRClone](https://github.com/xyou365/autorclone)** - GClone requires service accounts. To generate and manage them, use AutoRClone. You can then configure GClone using the service accounts.
- **Pip requirements** - In the folder of this GitHub Repository, run `pip install -r requirements.txt` and wait for the Python requirements are finished installing

## How to run the bot
First you are going to have to go to the [Discord App Dev Portal](https://discord.com/developers/applications) and then create a new application. Then you are going to want to make it a bot and get its token. NEVER SHARE THIS WITH ANYBODY, IT IS THE WAY THE PYTHON SCRIPT GAINS ACCESS TO THE BOT. In the `config.json` file, you are going to want to put the token in where the `token` line is. After that, set the bot prefix you want and then save the file.

Now, you can continue on depending the steps for what platform you are running this on.

Open up your Terminal or Command Line and then run `python CloneCord.py` or `python3 CloneCord.py`. The output of the Terminal or Command Line should have no errors and show that everything is all ready.

## Repl.it
You are not able to run this bot on Replit because it cannot install or run GClone in the Shell or Python. Instead, use Heroku or run it on your system.
