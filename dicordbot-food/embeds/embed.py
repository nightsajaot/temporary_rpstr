import disnake
import datetime as dt


def InformationEmbed(inter):
    information_embed = disnake.Embed(
        title="Актуальная инфомрация",
        description=F"- Тех. поддержка: del@gmail.com\n- Конт. телефон: +7 999 999 99 99\n\n- Адрес: Улица доставочная, дом 99",
        color=0xFFFFFF,
        timestamp=dt.datetime.now()
    )
    information_embed.set_author(
        name=f"Быстрая доставка",
        icon_url=None
    )
    information_embed.set_footer(
        text=inter.author
    )
    information_embed.set_image(
        url='https://media.discordapp.net/attachments/1226847584807686174/1237777269511032873/a0a47b04ddd6ac2d.png?ex=663ce169&is=663b8fe9&hm=f8f8a3731b784f48485c290ea999ecf9a0aabc5e6119d24f4309d2990a6f896c&=&format=webp&quality=lossless&width=314&height=89'
    )
    return information_embed


def StartEmbed(inter):
    start_embed = disnake.Embed(
        title="Справочное окно",
        description=f"Выберите информацию, которую хотите получить",
        color=0xFFFFFF,
        timestamp=dt.datetime.now()
    )
    start_embed.set_author(
        name=f"Быстрая доставка",
        icon_url=None
    )
    start_embed.set_footer(
        text=inter.author
    )
    return start_embed


def ActualActionCustomPage(inter, actllist, pagekey, imgurl):
    actual_action_custop_page_embed = disnake.Embed(
        title="Актуальные акции",
        description=f"{actllist[pagekey]}",
        color=0xFFFFFF,
        timestamp=dt.datetime.now()
    )
    actual_action_custop_page_embed.set_author(
        name=f"Быстрая доставка",
        icon_url=None
    )
    actual_action_custop_page_embed.set_footer(
        text=f"{inter.author}",
    )
    actual_action_custop_page_embed.set_image(
        url=f"{imgurl[pagekey]}"
    )
    return actual_action_custop_page_embed


def ActualSlotsCustomPage(inter, actlist1, actlist2, pagekey1):
    actual_slots_custom_page_embed = disnake.Embed(
        title="Актуальные позиции",
        color=0xFFFFFF,
        timestamp=dt.datetime.now()
    )
    actual_slots_custom_page_embed.set_author(
        name="Быстрая доставка"
    )
    actual_slots_custom_page_embed.set_footer(
        text=f"{inter.author}"
    )
    
    for i in range(pagekey1, len(actlist1)):
        actual_slots_custom_page_embed.add_field(
            name=str(actlist1[i]),
            value=str(actlist2[i]),
            inline=True
        )
    return actual_slots_custom_page_embed


def SeasonActionCustomPage(inter, actlist3, actlist4):
    season_action_custom_page_embed = disnake.Embed(
        title="Сезонные предложения",
        color=0xFFFFFF,
        timestamp=dt.datetime.now()
    )
    season_action_custom_page_embed.set_author(
        name="Быстрая доставка"
    )
    season_action_custom_page_embed.set_footer(
        text=f"{inter.author}"
    )
    season_action_custom_page_embed.set_image(
        url='https://t0.gstatic.com/licensed-image?q=tbn:ANd9GcSRA1VvVWshDqdk-IbClyNwWoUAjMnFQ5KQLb8eH0hu4gCCvfvqMEcQqOF-CTro2maW'
    )

    for i in range(0, 3):
        season_action_custom_page_embed.add_field(
            name=str(actlist3[i]),
            value=str(actlist4[i]),
            inline=True
        )
    return season_action_custom_page_embed
