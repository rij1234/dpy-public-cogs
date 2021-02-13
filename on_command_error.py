@bot.event
async def on_command_error(ctx,error):
    if hasattr(ctx.command, 'on_error'):
        return
    perms = ctx.channel.permissions_for(ctx.guild.me)
    if not perms.embed_links:
        await ctx.send("An error occured, but I must have permission to 'embed links' to send the error. Please enable it.")
    else:
        if isinstance(error, commands.MissingRequiredArgument):
           command = ctx.command
           return await ctx.reply(f"""```
{ctx.prefix}({command.name}{"|" if (len(command.aliases) != 0)  else ""}{"|".join(command.aliases)}) {command.signature}

{error}```""")
        embed=discord.Embed(title="Hmmm, an error occured.",color = 16711680)
        embed.add_field(name=error, value="""If you think this is a mistake, please [join our support server](https://example.com)""")
        await ctx.reply(embed=embed)
