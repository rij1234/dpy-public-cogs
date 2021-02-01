import discord
from discord.ext import commands
import re

class purgestuff(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.group()
    @commands.has_permissions(manage_messages=True)
    async def purge(self,ctx):
      if ctx.invoked_subcommand is None:
         embed = discord.Embed(title="Purge Command Syntax", description="""
         **Description:** The purge command deletes a number of messages in a channel
         **Uses:**
         -__purge count (count)__ --Deletes the specified number of messages
         -__purge bots (count)__ --Deletes messages by bots
         -__purge humans (count)__ --Deletes messages by non-bots
         -__purge links (count)__ --Deletes messages with http:// or https://
         -__purge invites (count)__ --Deletes messages with invites
         -__purge user (@user) (count)__ --Deletes messages made by that user
         -__purge match (count) [match_phrase]__ --Deletes all messages with match_phrase in them
         """)
         return await ctx.send(embed=embed)

    @purge.command()
    async def count(self, ctx, count:int):
        num = await ctx.channel.purge(limit=count)
        return await ctx.send(f"Purged {len(num)} messages")

    @purge.command()
    async def bots(self, ctx, count:int):
        check = lambda m: m.author.bot
        return await ctx.channel.purge(limit=count, check=check)

    @purge.command()
    async def humans(self, ctx, count:int):
        check = lambda m: not m.author.bot
        return await ctx.channel.purge(limit=count, check=check)

    @purge.command()
    async def user(self, ctx, user:discord.User, count:int):
       check = lambda m: m.author == user
       return await ctx.channel.purge(limit=count, check=check)
    @purge.command()
    async def match(self, ctx, count:int, *, match_phrase:str):
       check = lambda m: match_phrase.lower() in m.content.lower()
       return await ctx.channel.purge(limit=count, check=check)

    @purge.command()
    async def links(self, ctx, count:int):
       check = lambda m: "https://" in m.content.lower() or "http://" in m.content.lower()
       return await ctx.channel.purge(limit=count, check=check)

    @purge.command()
    async def invites(self,ctx,count:int):
       DISCORD_INVITE = r'discord(?:\.com|app\.com|\.gg)[\/invite\/]?(?:[a-zA-Z0-9\-]{2,32})'
       def get_invites(message):
            regex = re.compile(DISCORD_INVITE)
            invites = regex.findall(message)
            return invites or []
       check = lambda m: True if len(get_invites(m.content)) != 0 else False
       await ctx.channel.purge(limit=count, check=check)



def setup(bot):
    bot.add_cog(purgestuff(bot))
