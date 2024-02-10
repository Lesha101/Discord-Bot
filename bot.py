import discord
import random
from main import gen_pass

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$hey'):
        await message.channel.send("Hey!")
    elif message.content.startswith('$pasword'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$money'):
        monetka = random.randint(1,10)
        await message.channel.send(monetka)
    else:
        await message.channel.send(message.content)
