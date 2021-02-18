'''
direct clone of the pypi project ezhook
run the function `await send_hook(bot = ctx.bot, channel = ctx.channel, ...)` for each arg
'''

from discord import Webhook, RequestsWebhookAdapter
import asyncio

async def send_hook(bot:object,channel:object, username:str, avatarURL:str, message:str=None, embed=None):


  async def get_hook(channel):
   for hook in await channel.webhooks():
    if hook.name == "py.hook":
      return hook
    
   return await channel.create_webhook(name="py.hook")
  
  hook = await get_hook(channel)

  webhook = Webhook.partial(hook.id, hook.token, 
  adapter=RequestsWebhookAdapter())

  send_webhook = lambda : webhook.send(content=message, embed=embed, avatar_url = avatarURL, username = username)

  loop = asyncio.get_running_loop()

  await loop.run_in_executor(None, send_webhook)
