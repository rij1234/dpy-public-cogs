import discord
from discord.ext import commands
import json
from prettytable import PrettyTable

class Log_Raw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.event_cache = {
                    "GUILD_CREATE":0,
                    "GUILD_UPDATE":0,
                    "GUILD_DELETE":0,
                    "GUILD_ROLE_CREATE":0,
                    "GUILD_ROLE_UPDATE":0,
                    "GUILD_ROLE_DELETE":0,
                    "CHANNEL_CREATE":0,
                    "CHANNEL_UPDATE":0,
                    "CHANNEL_DELETE":0,
                    "CHANNEL_PINS_UPDATE":0,
                    "GUILD_MEMBER_ADD":0,
                    "GUILD_MEMBER_UPDATE":0,
                    "GUILD_MEMBER_REMOVE":0,
                    "GUILD_BAN_ADD":0,
                    "GUILD_BAN_REMOVE":0,
                    "GUILD_EMOJIS_UPDATE":0,
                    "GUILD_INTEGRATIONS_UPDATE":0,
                    "WEBHOOKS_UPDATE":0,
                    "INVITE_CREATE":0,
                    "INVITE_DELETE":0,
                    "VOICE_STATE_UPDATE":0,
                    "PRESENCE_UPDATE":0,
                    "MESSAGE_CREATE":0,
                    "MESSAGE_UPDATE":0,
                    "MESSAGE_DELETE":0,
                    "MESSAGE_DELETE_BULK":0,
                    "MESSAGE_REACTION_ADD":0,
                    "MESSAGE_REACTION_REMOVE":0,
                    "MESSAGE_REACTION_REMOVE_ALL":0,
                    "MESSAGE_REACTION_REMOVE_EMOJI":0,
                    "TYPING_START":0,
                    "MESSAGE_CREATE":0,
                    "MESSAGE_UPDATE":0,
                    "MESSAGE_DELETE":0,
                    "CHANNEL_PINS_UPDATE":0,
                    "MESSAGE_REACTION_ADD":0,
                    "MESSAGE_REACTION_REMOVE":0,
                    "MESSAGE_REACTION_REMOVE_ALL":0,
                    "MESSAGE_REACTION_REMOVE_EMOJI":0,
                    "TYPING_START":0,
                    None:0
        }

    @commands.Cog.listener()
    async def on_socket_response(self, msg):
        event_type = msg.get("t")
        self.bot.event_cache[event_type] += 1

    @commands.command()
    async def events(self, ctx):
        data = dict(sorted(self.bot.event_cache.items(), key=lambda x: x[1], reverse=True))
        x = PrettyTable()
        x.field_names = ["Event", "Number"]
        for (key, value) in data.items():
            x.add_row([key, value])
        await ctx.send("```" + str(x) + "```")


def setup(bot):
    bot.add_cog(Log_Raw(bot))
