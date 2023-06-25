# MTEyMjM0MzM2NzU5MDgyNjA5NQ.G_1Q3D.CkfvI0ILb6ZAqnEL3GF3zwHEMkFtwQIbEkfczc dicord token
# app id : 1122343367590826095
# public key: d5c32dc7e6b72b7af47b8ead91cf55aebbfdfc9eb59615682d94cb06eee70831

# JsSUhf4PQ7pr_6dwSK1F3hDGRWuHREUI secret key


# This example requires the 'message_content' intent.

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        channel = message.channel
        await channel.send('Hello I am Yo Boy!')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTEyMjM0MzM2NzU5MDgyNjA5NQ.G_1Q3D.CkfvI0ILb6ZAqnEL3GF3zwHEMkFtwQIbEkfczc')
