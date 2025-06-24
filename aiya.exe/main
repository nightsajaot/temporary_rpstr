import disnake
from disnake.ext import commands

intents = disnake.Intents(messages=True, guilds=True)

yuki = commands.Bot(command_prefix='.', intents=disnake.Intents.all(),
                    activity=disnake.Game('null', status=disnake.Status.idle))


yuki.load_extension("cogs.verify")
yuki.load_extension("cogs.information")
yuki.load_extension("cogs.art")
# yuki.load_extension("cogs.support")
# yuki.load_extension("cogs.voice")


yuki.remove_command('help')


@yuki.event
async def on_ready():
    print(f'Aiya started!')
    await yuki.change_presence(activity=disnake.Game(name='<3', type=1 - 4), status=disnake.Status.idle)
