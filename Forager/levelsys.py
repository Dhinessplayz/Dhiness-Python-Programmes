import discord
from discord.ext import commands
from pymongo import MongoClient

bot_channel = 893043613792079872
talk_channels = [888091416734097482]


level = ["Constant Forager User (CFU)", "Quick Leveler", "Toppr"]
levelnum = [5,10,15]

cluster = MongoClient("mongodb+srv://Dhiness:<password>@nero.b2ffp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
leveling = cluster["discord"]["leveling"]

class levelsys(commands.Cog):
    def _init_(self, client):
        self.client = MongoClient

    @commands.Cog.listener()
    async def on_ready(self):
        print("ready!")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id in talk_channels:
            stats = leveling.find_one({"id" : message.author.id})
            if not message.author.bot:
                if stats is None:
                    newuser = {"id" : message.author.id, "xp" : 100}
                    leveling.insert_one(newuser)
                else:
                    xp = stars["xp"] + 5
                    leveling.update_one({"id":message.author.id}, {"$set":{"xp":xp}})
                    lvl = 0
                    while True:
                        if xp < ((50*(lvl**2))+(50*(lvl-1))):
                            break
                        lvl += 1
                    xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                    if xp == 0:
                        await message.channel.send(f"well done {message.author.mention}! You leveled up to **level: {lvl}**!")
                        for i in range(len(level)):
                            if lvl == levelnum[1]:
                                await message.author.add_roles(discord.utils.get(message.author.guild.roles, name=level[1]))
                                embed = discord.Embed(deescription=f"{message.author.mention} you have gotten the role **(level[1])**!!!")
                                ember.set_thumbnail(url=message.author.avatar_url)
                                await message.channel.send(embed=embed)
    @commands.command()
    async def rank(self, ctx):
        if ctx.channel.id == bot_channel:
            stats = leveling.find_one({"id" : ctx.author.id})
            if stats is None:
                embed = discord.Embed(description="You haven't sent an messages, no rank!!!")
                await ctx.channel.send(embed=embed)
            else:
                xp = stats["xp"]
                lvl = 0
                rank = 0
            while True:
                if xp < ((50*(lvl**2))+(50*(lvl-1))):
                    break
                lvl += 1
            xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
            boxes = int((xp/(200*((1/2) * lvl)))*20)
            rankings = leveling.find().sort("xp,",-1)
            for x in rankings:
                rank += 1
                if stats["id"] == x["id"]:
                    break
            embed = discord.Embed(title="{}'s level stats".format(ctx.author.name))
            embed.add_feild(name="Name", value=ctx.author.mention, inline=True)
            embed.add_feild(name="XP", value=f"{xp}/{int(200*((1/2)*lvl))}", inline=True)
            embed.add_feild(name="Rank", value=f"{rank}/{ctx.guild.member_count}",inline=True)
            embed.add_feild(name="Progress Bar [lvl]", value=boxes * ":blue_square" + (20-boxes) * ":white_large_square:", inline=False)
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.channel.send(embed=embed)

    @commands.command()
    async def leaderboard(self, ctx):
        if (ctx.channel.id == bot_channel):
            rankings = leveling.find().sort("xp",-1)
            i = 1
            embed = discord.Embed(title="Rankings:")
            for x in rankings:
                try:
                    temp = ctx.guild.get_member(x["id"])
                    tempxp = x["xp"]
                    embed.add_field(name=f"{i}: {temp.name}", value=f"Total XP: {tempxp}", inline=False)
                    i += 1
                except:
                    pass
                if i == 11:
                    break
            await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(levelsys(client))
