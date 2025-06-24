import disnake 
import psycopg2
from disnake.ext import commands

config = {}
with open("token.txt") as f:
    for line in f:
        if "=" in line:
            key, value = line.strip().split("=", 1)
            config[key.strip()] = value.strip()

TOKEN = config["TOKEN"]
DB_PASSWORD = config["DB_PASSWORD"]

conn = psycopg2.connect(
    dbname="nightsaj",
    user="nightsaj",
    password=DB_PASSWORD,
    host="localhost",
    port="5432"
)

intents = disnake.Intents.all()

bot = commands.Bot(command_prefix='.', intents=disnake.Intents.all())

bot.remove_command('help')
bot.db = conn # type: ignore

bot.load_extension("cogs.greetings")
bot.load_extension("cogs.warnings")

@bot.event
async def on_ready():
    print(f"Akemi is started")
    await bot.change_presence(
        activity=disnake.Activity(type=disnake.ActivityType.watching, name="за сервером"),
        status=disnake.Status.do_not_disturb
    )

bot.run(TOKEN)
