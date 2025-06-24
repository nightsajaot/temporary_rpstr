from disnake.ext import commands
from embeds.greetings_embed import GreetingsEmbed #pyright: ignore
from disnake.ext.commands import Bot
from main import bot #pyright: ignore


class Greetings(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.Cog.listener('on_member_join')
    async def on_member_join(self, member):
        sendchannel = bot.get_channel(1227005755971080335)
        await sendchannel.send(embed=GreetingsEmbed(bot, member))


def setup(bot: commands.Bot):
    bot.add_cog(Greetings(Bot))
    print(f"|Cog {__name__} loaded")
