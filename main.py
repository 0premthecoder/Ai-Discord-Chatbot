# MTEyMjM0MzM2NzU5MDgyNjA5NQ.G_1Q3D.CkfvI0ILb6ZAqnEL3GF3zwHEMkFtwQIbEkfczc dicord token
# app id : 1122343367590826095
# public key: d5c32dc7e6b72b7af47b8ead91cf55aebbfdfc9eb59615682d94cb06eee70831

# JsSUhf4PQ7pr_6dwSK1F3hDGRWuHREUI secret key


# This example requires the 'message_content' intent.

import discord
import os
import openai


from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY")


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if self.user!=message.author:
            if self.user in message.mentions:
                channel = message.channel
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=f"{message.content}",
                    temperature=1,
                    max_tokens=256,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                messageTosend = response.choices[0].message
                await channel.send(messageTosend)
        


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
