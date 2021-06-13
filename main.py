import discord
import os
client = discord.Client()
from keep_alive import keep_alive


@client.event
async def on_ready():
    print('logined as{0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
      return
    if 'saman' in message.content:
      await message.channel.send('Saman khafe sho', tts=True)

    if 'sepehr' in message.content:
      await message.channel.send('Sefide sag:unamused:', tts=True)

    if 'sina' in message.content:
      await message.channel.send('Man ghablan legend boodam vali alanam legendam', tts=True)

    if 'hamed' in message.content:
      await message.channel.send('Negaran nabash', tts=True)

    if 'erfan' in message.content:
      await message.channel.send('Frag akhar bastani', tts=True)

    if 'behnam' in message.content:
      await message.channel.send('CS sharti', tts=True)
      
keep_alive()
client.run(os.getenv("TOKEN"))
