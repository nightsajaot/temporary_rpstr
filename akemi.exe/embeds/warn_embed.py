import disnake
import datetime as dt


def GiveWarnEmbed(bot, interaction, member, warn_count):
    give_warn_embed = disnake.Embed(
        title=f"Предупреждение {member.name}",
        description=f"{interaction.user.mention} выдал предупреждение пользователю {member.mention}.",
        color=0x330452,
        timestamp=dt.datetime.now()
    )
    give_warn_embed.set_author(
        name=f"{bot.user.name}",
        icon_url=bot.user.display_avatar.url
    )
    give_warn_embed.set_footer(
        text=f"{interaction.user.name}",
        icon_url=interaction.user.display_avatar.url
    )
    give_warn_embed.set_image(
        url="https://media.discordapp.net/attachments/1227029465683464272/1361681297197764811/Anime_Speed_GIF.gif?ex=67ffa408&is=67fe5288&hm=fa30e2f40ad241550587840eaa8ddf265d3134b9b47e4dabd94d3436ff49857f&=&width=896&height=504"
    )
    return give_warn_embed


def UnWarnEmbed(bot, interaction, member, warn_count):
    un_warn_embed = disnake.Embed(
        title=f"Снятие предупреждения с {member.name}",
        description=f"{interaction.user.mention} снял предупреждение с пользователя {member.mention}.",
        color=0x330452,
        timestamp=dt.datetime.now()
    )
    un_warn_embed.set_author(
        name=f"{bot.user.name}",
        icon_url=bot.user.display_avatar.url
    )
    un_warn_embed.set_footer(
        text=f"{interaction.user.name}",
        icon_url=interaction.user.display_avatar.url
    )
    un_warn_embed.set_image(
        url="https://media.discordapp.net/attachments/1227029465683464272/1362162854815469829/Anime_Sahneleri.gif?ex=68016484&is=68001304&hm=574902b4cad42c672949a0ff10905a280054e7027c0ab867287914445302d19a&=&width=1000&height=562"
    )
    return un_warn_embed


def UnWarnEmbedErrorNoWarns(bot, interaction, member):
    un_warn_embed_error_nowarns = disnake.Embed(
        title=f"Снятие предупреждения с {member.name}",
        description=f"У {member.mention} отсутствуют предупреждения.",
        color=0x330452,
        timestamp=dt.datetime.now()
    )
    un_warn_embed_error_nowarns.set_author(
        name=f"{bot.user.name}",
        icon_url=bot.user.display_avatar.url
    )
    un_warn_embed_error_nowarns.set_footer(
        text=f"{interaction.user.name}",
        icon_url=interaction.user.display_avatar.url
    )
    un_warn_embed_error_nowarns.set_image(
        url="https://media.discordapp.net/attachments/1227029465683464272/1362162854815469829/Anime_Sahneleri.gif?ex=68016484&is=68001304&hm=574902b4cad42c672949a0ff10905a280054e7027c0ab867287914445302d19a&=&width=1000&height=562"
    )
    return un_warn_embed_error_nowarns

def WarnInfoEmbed(bot, interaction, member, warn_count):
    warn_info_embed = disnake.Embed(
        title=f"Информация о предупреждениях",
        description=f"У пользователя {member.mention} {warn_count} предупреждений.",
        color=0x330452,
        timestamp=dt.datetime.now()
    )
    warn_info_embed.set_author(
        name=f"{bot.user.name}",
        icon_url=bot.user.display_avatar.url
    )
    warn_info_embed.set_footer(
        text=f"{interaction.user.name}",
        icon_url=interaction.user.display_avatar.url
    )
    warn_info_embed.set_image(
        url="https://media.discordapp.net/attachments/1227029465683464272/1382725079959343225/7084c682f10716fcaf0469b550a92b6a.png?ex=684c3294&is=684ae114&hm=93b2711dac8158ada3bb0116ed085f4bbd5d4589987295d17c61b009abb3954f&=&format=webp&quality=lossless&width=900&height=506"
    )
    return warn_info_embed


def LocalBanEmbed(bot, interaction, member, reason):
    localban_embed = disnake.Embed(
        title=f"Локальный бан выдан",
        description=f"Пользователь {member.mention} получил локальную блокировку.",
        color=0x330452,
        timestamp=dt.datetime.now()
    )
    localban_embed.set_author(
        name=f"{bot.user.name}",
        icon_url=bot.user.display_avatar.url
    )
    localban_embed.set_footer(
        text=f"{interaction.user.name}",
        icon_url=interaction.user.display_avatar.url
    )
    localban_embed.set_image(
        url="https://media.discordapp.net/attachments/1227029465683464272/1383104888371941537/09ab205b1731fd2d5a171fa4d65a7618.png?ex=684d944e&is=684c42ce&hm=2f77a8c429f58ee604a2f37add14533546944cecafa360939ce46634bcd61e79&=&format=webp&quality=lossless&width=900&height=506"
    )
    return localban_embed
