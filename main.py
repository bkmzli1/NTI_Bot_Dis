import discord
from discord import Client
from discord import utils
from discord.ext import commands
import config

bot = commands.Bot(command_prefix='!')


class MyClient(discord.Client):
    # старт бота
    async def on_ready(self):
        print('logged on as {0.user}!'.format(self))

    # обработка сообщений
    async def on_message(self, message):
        if message.author.id != config.BOT_ID:  # что бы бот не читал свои сообщения
            print('Massage from {0.author}: {0.content} {0.id}'.format(message))

    # обработка подключения в канал
    async def on_voice_state_update(self, member, before, after):
        ch = self.get_channel(config.chanel_voice_acting)  # получение текстового канала

        if str(after.channel) != 'None':  # если пользоатель вышел то получем None
            for id_channel in config.chanel_audio:  # получаем каналы прослушки аудио каналов
                if after.channel.id == id_channel:  # сравнение id каналов
                    await ch.send(
                        content=str('Потльзователь {0} вошол в комнату {1.channel.name}').format(member, after),
                        tts=True)
        else:
            await ch.send(
                content=str('Потльзователь {0} вышел в комнату {1.channel.name}').format(member, before),
                tts=True)


myClient = MyClient()
myClient.run(config.TOKEN)
