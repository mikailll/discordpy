import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='.')
client.remove_command("help")


# region Startup
@client.event
async def on_ready():
    print('SuperBot is ready!')


# endregion


# region Help
@client.command()
async def help(ctx):
    message = '.help for a list of commands\n .ping to check your ping\n .eightball <question here> for the truth \n .netflix premium netflix account format: <email:password>\n Developer: venomst#5970\n'
    messageEmbed = (discord.Embed(description=message, colour=0x66b2ff, title="SuperBot Menu!"))
    messageEmbed.set_author(name="Help - SuperBot",
                            icon_url="https://www.iconbunny.com/icons/media/catalog/product/2/0/2021.9-robot-icon-iconbunny.jpg")
    await ctx.send(embed=messageEmbed)


# endregion


# region Commands
@client.command()
async def ping(ctx):
    ping = str(round(client.latency * 1000)) + ' ms'
    message = (discord.Embed(description=ping, colour=0x32CD32, title="Ping!"))
    message.set_author(name="Ping - SuperBot!",
                       icon_url="https://lh3.googleusercontent.com/xKUdbWyGGv4lbYH5Fzrz-USBEKk84Aw43IPmnl9VVq4jewz4y8JrwOivPsAYCtTbDbdt")
    await ctx.send(embed=message)


@client.command()
async def eightball(ctx, *, question: str):
    choices = (
        'Absolutely!',
        'Without a doubt.',
        'Most likely.',
        'Yes.',
        'Maybe.',
        'Perhaps.',
        'Nope.',
        'Very doubtful.',
        'Absolutely not.',
        'It is unlikely.'
    )
    message = (discord.Embed(description=random.choice(choices), colour=0x0000, title="Question: " + question))
    message.set_author(name="8Ball - SuperBot!", icon_url="https://cdn.emojidex.com/emoji/seal/8ball.png?1417132124")
    await ctx.send(embed=message)


# endregion


# region Generator
@client.command()
async def netflix(ctx):
    fileName = 'netflix.txt'
    with open(fileName) as file:
        lines = file.read().splitlines()
        if len(lines) > 1:
            random_lines = random.sample(lines, 1)
            result = "".join(random_lines)

            account = (discord.Embed(description=result, colour=0xFF4C4C, title="Netflix Generator - Email:Password"))
            account.set_author(name="Netflix - SuperBot!", icon_url="http://www.comicgeekos.com/blog/wp-content/uploads/2018/11/Netflix-Logo-small-Transparent.png")
            await ctx.send(embed=account)

            with open(fileName, 'w') as output_file:
                output_file.writelines(line + "\n"
                                       for line in lines if line not in random_lines)


# endregion


# region Logging
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server!')


# endregion

client.run('NTkwODYxMjczNTI5NDUwNTI5.XRZYBg.vCbijE0VwJxXXGZSe0xounq1-zU')
