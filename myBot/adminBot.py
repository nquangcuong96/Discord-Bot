import discord
import sys
import dictionary

"""
client ID: 613569837876117546
url: https://discordapp.com/oauth2/authorize?client_id={CLIENTID}&scope=bot&permissions={PERMISSIONINT}
adminBot infor:
    bot token: NjEzNTY5ODM3ODc2MTE3NTQ2.XVy33A.CsuFSXbCglnruyklJNPgaQo2dPI
    permission token: 202752
    adminBot url: https://discordapp.com/oauth2/authorize?client_id=613569837876117546&scope=bot&permissions=202752
"""

hello_text = ['hi bot', 'hello bot', 'chào bot']
guide_text = ['help me bot', 'cứu bot ơi', 'cuu bot oi', 'cứu bot oi', 'cuu bot ơi']
logout_text = ['bot logout']
help_text = ['help 1','help 2','help 3','help 4','help 5']
admin = ['Master#9577','Cú#3158']

client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} is ready")


@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    if message.content.lower() in hello_text:
        await message.channel.send(f"Chào {message.author.name}, một ngày vui vẻ")
    elif message.content.lower() in guide_text:
        await message.channel.send(f"{message.author.name}, chọn thông tin mà bạn cần giúp. Vui lòng nhập help + số thứ tự:")
        for i in dictionary.guide_dict:
            text = i + ": " + dictionary.guide_dict[i]
            await message.channel.send(text)
    elif message.content.lower() in help_text:
        for i in dictionary.help_dict:
            if message.content.lower() == i.lower():
                text = str(message.author.name) + ", " + dictionary.help_dict[i]
                await message.channel.send(text)
    elif message.content.lower() in logout_text:
        if str(message.author) in admin:
            await message.channel.send(f"{message.author.name}, liên hệ @Master#9577 để khởi động tôi")
            await client.close()
            sys.exit()
        else:
            await message.channel.send(f"{message.author.name}, bạn éo đủ trình để thực hiện lệnh này")


client.run("NjEzNTY5ODM3ODc2MTE3NTQ2.XVy33A.CsuFSXbCglnruyklJNPgaQo2dPI")
