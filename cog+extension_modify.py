'''
[p]cog [reload|restart|reset] will reload ad cog
[p]cog [unload|stop] will unload a cog
[p]cog [load|start] will start a cog
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
