import threading
import time

import discord
import discord.ext
from discord.ext import commands
from discord.ext.commands import Bot

import config


class BotClient(Bot):

    # старт бота
    async def on_ready(self):
        # self.add_command(self.test)
        print('logged on as {0.user}!'.format(self))

    # обработка сообщений
    async def on_message(self, message):
        if message.author.id != config.BOT_ID:  # что бы бот не читал свои сообщения
            if message.content == '!exit':
                if message.channel.id == config.chanel_systems:
                    await self.close()

        await self.process_commands(message)

    # print('Massage from {0.author}: {0.content}: id = {0.id}'.format(message))

    # обработка подключения в канал
    async def on_voice_state_update(self, member, before, after):
        ch = self.get_channel(config.chanel_systems)  # получение текстового канала

        if str(after.channel) != 'None':
            if after.channel.id in config.chanel_audio:
                await ch.send(
                    content=str(f'Пользователь  {member.mention} вошел в комнату {after.channel.name}'),
                    tts=True)


myClient = BotClient(command_prefix='!')


def thread_client():
    myClient.run(config.TOKEN)


@myClient.command(pass_context=True)
async def stopBot(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    author = ctx.message.author
    access = False
    for role in author.roles:
        for role_access_id in config.role_id_Full:
            if role.id == role_access_id:
                access = True

    if access:
        await ctx.send(f'Остановил бота {author.mention}')
        await myClient.close()
    else:
        await ctx.send(f'Отказано в доступе пользователю  {author.mention}')


@myClient.event
async def on_member_join(member):

    for id_role_def in config.the_default_roles:
        channel = myClient.get_channel(config.chanel_systems)
        role = discord.utils.get(member.guild.roles, id=id_role_def)
        text = f'Пользователь ``{member.name}``, получил роль ``{role.name}``'
        print(f'Пользователь {member.name}, получил роль ``{role.name}')
        await member.add_roles(role)
        # await channel.send(embed=discord.Embed(description=text, color=0x0c0c0c))
