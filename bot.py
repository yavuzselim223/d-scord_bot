import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='B!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık.')

@bot.event
async def on_message(message):
    if message.author == bot.user:        
        return
    if message.content.startswith('Sa'):
        await message.channel.send("As Hg?")
    if message.content.startswith('B!yardım'):
        await message.channel.send("Komutlarım daha eklenmedi fakat oto cevaplarım var 😁: (Sizin yazabildikleriniz:(Sa), (sa), (bb), (Bb), (B! ?), (Nabersiniz?),(Naber chat?), (Naber chat), (prefix_bot), (B!yardım!) (B!Yardım!)")
    if message.content.startswith('B!Yardım'):
        await message.channel.send("Komutlarım daha eklenmedi fakat oto cevaplarım var 😁: (Sizin yazabildikleriniz:(Sa), (sa), (bb), (Bb), (Oyun_link), (B! ?), (Nabersiniz?),(Naber chat?), (Naber chat), (prefix_bot), (B!yardım!) (B!Yardım!)")        
    if message.content.startswith('B! ?'):
        await message.channel.send("Bu komut sayesinde bana çeşitli emirler verebilirsin 😋")
    if message.content.startswith('prefix_bot'):
        await message.channel.send("B!")
    if message.content.startswith('Naber chat?'):
        await message.channel.send("İyi senden naber?")
    if message.content.startswith('Naber chat'):
        await message.channel.send("İyi senden naber?")
    if message.content.startswith('Nabersiniz?'):
        await message.channel.send("İyi sen nasılsın?")
    if message.content.startswith('Naber chat?'):
        await message.channel.send("İyi senden naber?")
    if message.content.startswith('sa'):
        await message.channel.send("As Hg?")
    if message.content.startswith('bb'):
        await message.channel.send("Görüşmek üzere Kankam. ❤")
    if message.content.startswith('Bb'):
        await message.channel.send("Görüşmek üzere Kankam. ❤")
bot.run("TOKEN")
