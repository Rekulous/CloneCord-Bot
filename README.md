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

- **[GClone](https://github.com/donwa/gclone)** - Run the shell / batch script if you are on Linux to install, or add the `gclone.exe` file to your system PATH variables if you are on Windows. Putting the script in the same directory as GClone in Windows will work as well. If you are on MacOS, download the Darwin build of GClone.
- **[AutoRClone](https://github.com/xyou365/autorclone)** - GClone requires service accounts. To generate and manage them, use AutoRClone. You can then configure GClone using the service accounts.
- **Pip requirements** - In the folder of this GitHub Repository, run `pip install -r requirements.txt` and wait for the Python requirements are finished installing
- **[Docker (OPTIONAL)](https://docker.com) & [Docker-Compose (OPTIONAL)](https://docs.docker.com/compose)** - If you want to run the bot in a containerized Docker environment, you have to install Docker and Docker-Compose first. You can use Heroku too! **THIS IS OPTIONAL AND YOU DON'T HAVE TO USE DOCKER OR HEROKU!**
- **[Git (OPTIONAL)](https://git-scm.com)** - You can use this tool to contribute to development of CloneCord or by cloning the repo for your own use.

## How to run the bot

1. Download the repository as a zip file and extract it (Click on the green `Code` button on the front page of this GitHub repo and then click `Download Zip`). You can also use Git to `git clone https://github.com/rekulous/clonecord-bot` and get the repo.
2. Go to the [Discord App Dev Portal](https://discord.com/developers/applications) and then create a new application.
3. Turn the application into a bot and copy its token. **NEVER SHARE THIS WITH ANYBODY, IT IS THE WAY THE PYTHON SCRIPT GAINS ACCESS TO THE BOT!!!**
4. In the `config.json` file, you are going to want to put the token in where the `token` line is. After that, set the bot prefix you want and then save the file.
5. Open up your Terminal or Command Line and then `cd` into the directory of the Cloned GitHub Repo.
6. Run `python CloneCord.py` or `python3 CloneCord.py`. The output of the Terminal or Command Line should have no errors and show that everything is all ready!

**Enjoy using CloneCord!**

## Docker

1. Follow the first five steps of [How to run the bot](#How-to-run-the-bot)
2. Feel free to edit `Dockerfile` or `docker-compose.yml` to your preferences and desire if you want
3. Run `docker-compose up -d` and wait for docker-compose to build the container and Docker image
4. Run `docker conatainer ls` and `docker image ls` to check if the CloneCord container and image is running

**If the image and container exists, and the container is running, CloneCord is working! Check to see if your bot is working and enjoy!**

## Heroku

**Deploy to Heroku:**

 [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Rekulous/CloneCord-Bot/blob/main)

## Repl.it

You are not able to run this bot on Replit because it cannot install or run GClone in the Shell or Python. Instead, use Heroku or run it on your system.
