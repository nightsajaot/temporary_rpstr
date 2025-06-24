import disnake
import psycopg2
from disnake.ext import commands
from disnake.ext.commands import Bot
from disnake.ui import View, Button
from embeds.embed import InformationEmbed, StartEmbed, ActualActionCustomPage, ActualSlotsCustomPage, SeasonActionCustomPage

connection = None
cursor = None
actllist = []
actllist1 = []
actllist2 = []
actllist3 = []
actllist4 = []
poslist = []
imgurl = []

with open('C:/Users/Ultre/OneDrive/Документы/nightidk/PROJECT/DiscordBots/StudyBot/token.txt') as f:
    log_string = f.readlines()

try:
    conn_string = "postgres://postgres:" + str(log_string[1]) + "@localhost:5432/MireaDB"
    connection = psycopg2.connect(conn_string)
    cursor = connection.cursor()

    select_query = """ SELECT action, url FROM actualaction """
    select_query1 = """ SELECT name, description, act FROM actualposition """
    select_query2 = """ SELECT name, description FROM seasonaction """

    cursor.execute(select_query)

    records = cursor.fetchall()
    
    for row in records:
        actllist.append(row[0])
        imgurl.append(row[1])
            
    cursor.execute(select_query1)
    
    records = cursor.fetchall()
    
    for row in records:
        if row[2] == 1:
            actllist1.append(row[0])
            actllist2.append(row[1])

    cursor.execute(select_query2)
    
    records = cursor.fetchall()

    for row in records:
        actllist3.append(row[0])
        actllist4.append(row[1])
            
except (Exception, psycopg2.Error) as error:
    print("Error during operation DB", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("| Connection close")
        print("| Data connection compite")


class ViewStartButton(View):
    def __init__(self):
        super().__init__()

        self.add_item(Button(label='Контактная информация', custom_id='1', style=disnake.ButtonStyle.gray))
        self.add_item(Button(label='Предложения и акции', custom_id='2', style=disnake.ButtonStyle.gray))
        self.add_item(Button(label='Доступные для заказа позиции', custom_id='3', style=disnake.ButtonStyle.gray))


class ViewBeckToStartButton(View):
    def __init__(self):
        super().__init__()

        self.add_item(Button(label='Назад', custom_id='4', style=disnake.ButtonStyle.red))


class ViewBackAndSeasonActionButton(View):
    def __init__(self):
        super().__init__()

        self.add_item(Button(label='Назад', custom_id='4', style=disnake.ButtonStyle.red))
        self.add_item(Button(label='Сезонные товары', custom_id='7', style=disnake.ButtonStyle.blurple))


class ViewSlidePageButton(View):
    def __init__(self):
        super().__init__()

        self.add_item(Button(label='Предыдущая страница <-', custom_id='6', style=disnake.ButtonStyle.green))
        self.add_item(Button(label='Следующая страница ->', custom_id='5', style=disnake.ButtonStyle.green))
        self.add_item(Button(label='Назад', custom_id='4', style=disnake.ButtonStyle.red))


class ViewSlidePageButton1(View):
    def __init__(self):
        super().__init__()

        self.add_item(Button(label='Следующая страница ->', custom_id='5', style=disnake.ButtonStyle.green))
        self.add_item(Button(label='Назад', custom_id='4', style=disnake.ButtonStyle.red))


class ViewSlidePageButton2(View):
    def __init__(self):
        super().__init__()

        self.add_item(Button(label='Предыдущая страница <-', custom_id='6', style=disnake.ButtonStyle.green))
        self.add_item(Button(label='Назад', custom_id='4', style=disnake.ButtonStyle.red))


class StartSend(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot
        self.pagekey = 0
        self.pagekey1 = 0

    @commands.slash_command(decription="Start using bot")
    async def start(self, inter: disnake.ApplicationCommandInteraction):
        await inter.send(embed=StartEmbed(inter), view=ViewStartButton())

    @commands.Cog.listener('on_button_click')
    async def button_active(self, inter: disnake.MessageInteraction):
        custom_id = inter.component.custom_id
        
        if '1' in custom_id:
            await inter.response.edit_message(embed=InformationEmbed(inter), view=ViewBeckToStartButton())
        if '2' in custom_id:
            await inter.response.edit_message(embed=ActualActionCustomPage(inter, actllist, self.pagekey, imgurl), view=ViewSlidePageButton1())
        if '3' in custom_id:
            await inter.response.edit_message(embed=ActualSlotsCustomPage(inter, actllist1, actllist2, self.pagekey1), view=ViewBackAndSeasonActionButton())
            
        if '4' in custom_id:
            self.pagekey = 0
            await inter.response.edit_message(embed=StartEmbed(inter), view=ViewStartButton())
        if '5' in custom_id:
            if self.pagekey == 2:
                self.pagekey += 1
                await inter.response.edit_message(embed=ActualActionCustomPage(inter, actllist, self.pagekey, imgurl), view=ViewSlidePageButton2())
            else:
                self.pagekey += 1
                await inter.response.edit_message(embed=ActualActionCustomPage(inter, actllist, self.pagekey, imgurl), view=ViewSlidePageButton())
        if '6' in custom_id:
            if self.pagekey == 1:
                self.pagekey -= 1
                await inter.response.edit_message(embed=ActualActionCustomPage(inter, actllist, self.pagekey, imgurl), view=ViewSlidePageButton1())
            else:
                self.pagekey -= 1
                await inter.response.edit_message(embed=ActualActionCustomPage(inter, actllist, self.pagekey, imgurl), view=ViewSlidePageButton())
        if '7' in custom_id:
            await inter.response.edit_message(embed=SeasonActionCustomPage(inter, actllist3, actllist4), view=ViewBeckToStartButton())


def setup(bot: commands.Bot):
    bot.add_cog(StartSend(Bot))
    print(f"| Cog {__name__} connected")
