import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

token = os.environ['BOT_TOKEN']
target = os.environ['TEST_ID']
log_channel = os.environ['LOG_CHANNEL']


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    client.status = discord.Status.invisible
    await client.change_presence(status=discord.Status.invisible)


@client.event
async def on_message(message):
    if message.author.id == int(target):
        channel = client.get_channel(int(log_channel))
        await channel.send(message.content)
        print(message.author.name)


client.run(token)
