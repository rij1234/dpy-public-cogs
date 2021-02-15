import discord
from discord.ext import commands

class Snipe(commands.Cog):
 def __init__(self, bot):
     self.recent_msgs = {}

 @commands.Cog.listener()
 async def on_message_delete(self, message):
    self.recent_msgs[str(message.channel.id)] = message

 @commands.command()
 async def snipe(self, ctx):

    if str(ctx.channel.id) not in self.recent_msgs:
         return await ctx.send("Nothing to snipe")
    msg = self.recent_msgs[str(ctx.channel.id)]

    embed = discord.Embed(title=msg.content, timestamp=msg.created_at)
    embed.set_author(name=f"{msg.author.name}#{msg.author.discriminator}", icon_url=msg.author.avatar_url)

    await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Snipe(bot))
