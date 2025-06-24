import disnake
from disnake.ext import commands
from disnake.ui import View, Button
from disnake import Embed


# Селект меню
class SelectInfo(disnake.ui.StringSelect):
    def __init__(self):
        options = [
            disnake.SelectOption(label='Каналы', description='Описание каналов сервера'),
            disnake.SelectOption(label='Роли', description='Описание ролей сервера'),
        ]
        super().__init__(placeholder='Что вы хотите узнать?', min_values=0, max_values=1, options=options,
                         custom_id='navig')


# Начальный эмбед
class StaticInfoMsg(Embed):
    def __init__(self, inter: commands.Context):
        super().__init__(
            title='Информация:',
            description='Благодаря данному сообщению, вы можете узнать дополнительную информацию по серверу. Для получения информации вам требуется выбрать один из пунктов в списке ниже.',
            color=disnake.Color.from_rgb(150, 134, 119),
        )
        self.set_author(
            name='Навигация | Каморка Ночнойсажи'
        )
        self.set_image(
            url='https://media.discordapp.net/attachments/1096159758332985435/1122938121789636701/info.png?width=1440&height=576'
        )
        self.set_footer(
            text='Автор - Aiya',
            icon_url='https://media.discordapp.net/attachments/1096159758332985435/1122265195797041172/0371e89235b0ec6e2cb889cf823454db4.jpg'
        )


# эмбед с каналами
class ChanInfoMsg(Embed):
    def __init__(self, inter: disnake.MessageInteraction):
        # Каналы
        rules = inter.guild.get_channel(1096154014560829521)
        dopinfo = inter.guild.get_channel(1120473418328973452)

        general = inter.guild.get_channel(1095864627121893377)
        games = inter.guild.get_channel(1120858818973270026)
        hlam = inter.guild.get_channel(1120474261522501714)
        helpp = inter.guild.get_channel(1120474391424286760)
        trash = inter.guild.get_channel(1095870397876019290)

        super().__init__(
            title='Информация о каналах сервера:',
            description=f'''{rules.mention} — правила сервера \n {dopinfo.mention} — доп информация \n 
            {general.mention} — основной чат для общения \n {games.mention} — общение на тему игр \n {hlam.mention} — чат для всякого хлама \n {helpp.mention} — чат для оказания помощи \n {trash.mention} — чат для использование команд ботов''',
            color=disnake.Color.from_rgb(150, 134, 119),
        )
        self.set_author(
            name='Навигация | Каморка Ночнойсажи'
        )
        self.set_footer(
            text='Автор - Aiya',
            icon_url='https://media.discordapp.net/attachments/1096159758332985435/1122265195797041172/0371e89235b0ec6e2cb889cf823454db4.jpg'
        )


# эмбед с ролями
class RoleInfoMsg(Embed):
    def __init__(self, inter: disnake.MessageInteraction):
        # Роли
        sm = inter.guild.get_role(1095865759005167638)
        md = inter.guild.get_role(1120845435075043428)
        bt = inter.guild.get_role(1118266281464954940)
        ok = inter.guild.get_role(1095866106557771808)

        super().__init__(
            title='Информация о ролях сервера:',
            description=f'''{sm.mention} — менеджер сервера \n {md.mention} — модератор сервера \n {bt.mention} — бот \n {ok.mention} — участник''',
            color=disnake.Color.from_rgb(150, 134, 119),
        )
        self.set_author(
            name='Навигация | Каморка Ночнойсажи'
        )
        self.set_footer(
            text='Автор - Aiya',
            icon_url='https://media.discordapp.net/attachments/1096159758332985435/1122265195797041172/0371e89235b0ec6e2cb889cf823454db4.jpg'
        )


class InfoCom(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    class VerifySystem(commands.Cog):
        def __init__(self, yuki: commands.Bot):
            self.yuki = yuki

    @commands.command(description='описание')
    @commands.has_role('Server Manager')
    async def infosend(self, inter: commands.Context):

        embed = StaticInfoMsg(inter)
        view = disnake.ui.View(timeout=None)
        view.add_item(SelectInfo())

        await inter.send(embed=embed, view=view)

    @commands.Cog.listener('on_dropdown')
    async def info_send(self, inter: commands.Context):
        if inter.component.custom_id == 'navig':

            if inter.values is None:
                view = disnake.ui.View(timeout=None)
                view.add_item(SelectInfo())
                await inter.response.edit_message(view=view)
                return
            value = inter.values[0]

            if value == 'Каналы':
                embed1 = ChanInfoMsg(inter)
                await inter.send(embed=embed1, ephemeral=True)
            if value == 'Роли':
                embed2 = RoleInfoMsg(inter)
                await inter.send(embed=embed2, ephemeral=True)


def setup(yuki: commands.Bot):
    yuki.add_cog(InfoCom(yuki))
    print(f">| Cog Aiya {__name__} connected")
