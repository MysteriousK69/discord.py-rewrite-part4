import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord import Game

bot = commands.Bot(command_prefix="!")
bot.remove_command('help')

@bot.event
async def on_ready(): # on_ready func
    print("The bot is online!")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('!help'))

@bot.command()
@commands.has_role('Admin')
@commands.cooldown(1, 3, commands.BucketType.user)
async def ban(ctx, member: discord.Member, content):
    await ctx.send("I Successfully Banned") # send msg in channel
    await member.send(f"You were banned for {content} get rekt") # send dm
    await member.ban() # ban

@bot.command()
@commands.has_role('Admin')
@commands.cooldown(1, 3, commands.BucketType.user)
async def hello(ctx):
    await ctx.send("sup kiddo :wave:")
    print("A random nerd used the hello command!")


@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def kick(ctx, member: discord.Member, content):
    try:
        await ctx.send("Kicked Them") # send msg in channel
        await member.send(f"You were kicked for {content} get rekt") # send dm
        await member.kick() # kick
    except:
        await ctx.send("Kicked Them")
        await member.kick()

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def purge(ctx, content):
    amount = int(content) # def amount var
    await ctx.channel.purge(limit=amount + 1) # purge

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def warn(ctx, content, member: discord.Member):
    await ctx.send("I Warned Them")
    await member.send(f"You were warned for {content}") # send dm

@bot.command()
async def help(ctx):
    embed = discord.Embed(title='Help', description='Meh', color=0xeee657)
    embed.add_field(name='Help', value='aaa', inline=False)
    embed.add_field(name='ban', value="Bans a memebr!", inline=True)

    await ctx.send(embed=embed)

bot.run("NzIyNzUwNTAyNjk3MzA0MDc0.XvHivw.vSs5aZtlOZa0VrTe3v-DOIXh0XI")