import disnake
from disnake.ext import commands
from disnake import ApplicationCommandInteraction
from embeds.warn_embed import GiveWarnEmbed, UnWarnEmbed, UnWarnEmbedErrorNoWarns, WarnInfoEmbed, LocalBanEmbed #pyright: ignore

class Warnings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="warn", description="Выдать предупреждение пользотвателю")
    async def warn(
            self,
            inter: ApplicationCommandInteraction,
            member: disnake.Member =  commands.Param(name="пользователь", description="Кому выдать предупреждение")
    ):

        conn = self.bot.db
        cur = conn.cursor()

        cur.execute("SELECT warn FROM users_warning WHERE userid = %s", (str(member.id),))
        result = cur.fetchone()

        if result:
            warn_count = result[0] + 1
            cur.execute("UPDATE users_warning SET warn = %s WHERE userid = %s", (warn_count, str(member.id)))
        else:
            warn_count = 1
            cur.execute("INSERT INTO users_warning (userid, warn, warning) VALUES (%s, %s, %s)", (str(member.id), warn_count, 0))

        conn.commit()
        cur.close()
        #conn.close()

        embed = GiveWarnEmbed(self.bot, inter, member, warn_count)
        await inter.response.send_message(embed=embed)


    @commands.slash_command(name="unwarn", description="Снять предупреждение пользователю")
    async def unwarn(
            self,
            inter: ApplicationCommandInteraction,
            member: disnake.Member = commands.Param(name="пользотватель", description="С кого снять предупреждение")
    ):
        conn = self.bot.db
        cur = conn.cursor()

        cur.execute("SELECT warn FROM users_warning WHERE userid = %s", (str(member.id),))
        result = cur.fetchone()

        if not result or result[0] <= 0:
            embed1 = UnWarnEmbedErrorNoWarns(self.bot, inter, member)
            await inter.response.send_message(embed=embed1, ephemeral=True)
            cur.close()
            return

        warn_count = result[0] - 1
        cur.execute("UPDATE users_warning SET warn = %s WHERE userid = %s", (warn_count, str(member.id)))
        conn.commit()
        cur.close()

        embed2 = UnWarnEmbed(self.bot, inter, member, warn_count)
        await inter.response.send_message(embed=embed2)


    @commands.slash_command(name="warninfo", description="Показать количество предупреждений у пользователя")
    async def warninfo(
            self,
            inter: ApplicationCommandInteraction,
            member: disnake.Member = commands.Param(name="пользователь", description="Чей счет предупреждений показать")
    ):
        conn = self.bot.db
        cur = conn.cursor()

        cur.execute("SELECT warn FROM users_warning WHERE userid = %s", (str(member.id),))
        result = cur.fetchone()

        cur.close()

        warn_count = result[0] if result else 0

        embed = WarnInfoEmbed(self.bot, inter, member, warn_count)
        await inter.response.send_message(embed=embed, ephemeral=True)


    @commands.slash_command(name="localban", description="Выдать пользователю роль localban с указанием причины")
    async def localban(
            self,
            inter: ApplicationCommandInteraction,
            member: disnake.Member = commands.Param(name="пользователь", description="Кого локально забанить"),
            reason: str = commands.Param(name="причина", description="Причина локального бана")
    ):
        if not inter.guild:
            await inter.response.send_message("Эта команда может быть использована только на сервере.", ephemeral=True)
            return

        conn = self.bot.db
        cur = conn.cursor()

        # Вставка или обновление причины в таблице localban
        cur.execute("""
            INSERT INTO localban (id, reason)
            VALUES (%s, %s)
            ON CONFLICT (id) DO UPDATE SET reason = EXCLUDED.reason
        """, (str(member.id), reason))

        conn.commit()
        cur.close()

        # Получение роли по ID
        role_id = 1383100984221372526  # <-- замени на свой ID при необходимости
        role = inter.guild.get_role(role_id)

        if not role:
            await inter.response.send_message("Роль не найдена.", ephemeral=True)
            return

        try:
            await member.add_roles(role, reason=reason)
        except disnake.Forbidden:
            await inter.response.send_message("Недостаточно прав для выдачи роли.", ephemeral=True)
            return

        embed = LocalBanEmbed(self.bot, inter, member, reason)
        await inter.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(Warnings(bot))
    print(f"|Cog {__name__} loaded")
