'''
*COGS MUST BE IN FOLDER TITLED "cogs"!!!
[p]cog [reload|restart|reset] will reload an extension
[p]cog [unload|stop] will unload an extension
[p]cog [load|start] will start an extension
'''
@bot.command()
async def cog(ctx,type,arg):
  if ctx.author.id in bot.admin_id:
    if type.lower() in ['reload', 'restart', 'reset']:
        bot.reload_extension(f'cogs.{arg}')
        await ctx.send(f'{arg} reloaded')
    elif type.lower() in ['unload', 'stop']:
        bot.unload_extension(f'cogs.{arg}')
        await ctx.send(f'{arg} stopped')
    elif type.lower() in ['load', 'start']:
        bot.load_extension(f'cogs.{arg}')
        await ctx.send(f'{arg} start')
  else:
    await ctx.send('Only those with admin access to the bot may use this command')
