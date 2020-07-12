import discord
from discord import Client
from discord import utils
from discord.ext import commands
import config

from threading import Thread


class BotClient(discord.Client):
    # старт бота
    async def on_ready(self):
        print('logged on as {0.user}!'.format(self))

    # обработка сообщений
    async def on_message(self, message):
        if message.author.id != config.BOT_ID:  # что бы бот не читал свои сообщения
            if message.content == '!exit':
                if message.channel.id == config.chanel_voice_acting:
                    await myClient.close()
    # print('Massage from {0.author}: {0.content}: id = {0.id}'.format(message))

    # обработка подключения в канал
    async def on_voice_state_update(self, member, before, after):
        ch = self.get_channel(config.chanel_voice_acting)  # получение текстового канала

        if str(after.channel) != 'None':
            if after.channel.id in config.chanel_audio:
                await ch.send(
                    content=str('Потльзователь @{0} вошол в комнату {1.channel.name}').format(member, after),
                    tts=True)


myClient = BotClient()
myClient.run(config.TOKEN)

