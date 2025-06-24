import disnake
from disnake import Embed
from disnake.ext import commands
import datetime
 

class SendArt(commands.Cog):
    def __init__(self, yuki: commands.Bot):
        self.yuki = yuki

    @commands.Cog.listener('on_message')
    async def send(self, message):
        if message.channel.id == 1120474261522501714:
            if message.author == self.yuki.user:
                return
            
            if message.attachments:
                for attachment in message.attachments:
                    if attachment.url.lower().endswith(('png', 'jpeg', 'jpg', 'gif')):

                        embed1 = disnake.Embed(
                            title=f'Арт предоставлен:',
                            description=f'{message.author.mention}',
                            color=disnake.Color.from_rgb(150, 134, 119),
                            timestamp = datetime.datetime.now(),
                        )
                        embed1.set_author(
                            name='Арт площадка | Каморка Ночнойсажи'
                        )
                        embed1.set_image(
                            url=attachment.url
                        )
                        embed1.set_footer(
                            text='Aiya',
                            icon_url='https://media.discordapp.net/attachments/1096159758332985435/1122265195797041172/0371e89235b0ec6e2cb889cf823454db4.jpg'
                        )

                        await message.channel.send(embed=embed1)
                        await message.delete()
            else:
                embed2 = disnake.Embed(
                    title=f'Ошибка распознавания:',
                    description='Пожалуйста, прикрепите изображение к сообщению!',
                    color=disnake.Color.from_rgb(150, 134, 119),
                    timestamp = datetime.datetime.now(),
                )
                embed2.set_author(
                    name='Арт площадка | Каморка Ночнойсажи'
                )
                embed2.set_footer(
                    text='Aiya',
                    icon_url='https://media.discordapp.net/attachments/1096159758332985435/1122265195797041172/0371e89235b0ec6e2cb889cf823454db4.jpg'
                )

                await message.author.send(embed=embed2)
                await message.delete()


def setup(bot:commands.Bot):
    bot.add_cog(SendArt(bot))
    print(f">| Cog Aiya {__name__} connected")
