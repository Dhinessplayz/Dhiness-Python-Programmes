import discord
from discord.ext import commands


TOKEN = 'ODkyNzM2NDc3MjY2NTkxNzU0.YVRPog.gXnihzIX7L8T_l-D-C5zPNheB90'

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot is ready")


@client.command()
async def ping(ctx):
    await ctx.reply("Pong!")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx,member:discord.Member):
    await ctx.guild.ban(member)
    await ctx.send(f"{member.mention} has been banned")


@client.command()
@commands.has_permissions(ban_members=True)
async def kick(ctx,member:discord.Member):
    await ctx.guild.kick(member)
    await ctx.send(f"{member.mention} has been kicked")

@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx,limit:int):
    await ctx.channel.purge(limit=limit)


client.run(TOKEN)
