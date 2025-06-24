import disnake
import datetime as dt


def GreetingsEmbed(bot, member):
    greetings_embed = disnake.Embed(
        title=f"{member.name}",
        description=f"{member.mention}, присоединяется к нашему проекту. Поприветствуйте нового участника!",
        color=0xf2a74b,
        timestamp=dt.datetime.now()
    )
    greetings_embed.set_author(
        name=f"{bot.user.name}",
        icon_url=bot.user.display_avatari.url
    )
    greetings_embed.set_footer(
        text=f"{member.name}",
        icon_url=member.display_avatar.url
    )
    greetings_embed.set_image(
        url="https://media.discordapp.net/attachments/1227029465683464272/1227029662710894612/6a8becf23a5e3cb47a0020db91b44cd1.gif?ex=6626eb6c&is=6614766c&hm=2761a81b3bcf19fef601db80dd7de74fc656c4f7678e3287d785bc4896384bd7&=&width=485&height=273"
    )
    return greetings_embed
