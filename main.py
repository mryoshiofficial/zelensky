import discord
from discord.ext import commands , tasks
import requests
import random
import re # i dont remember why i need this , but andrewnyan said don't touch this fdafakosdffsafsasfsa

# libs

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='%', intents=intents)
token = 'put there your token'
approvedusers = [put there your id , this is used for only some commands]

badwords = ["блять", "бля", "хуй", "пизда", "пиздец" , "хуесос" , "пидор" , "сука" , "Блять", "Бля", "Хуй", "Пизда", "Пиздец" , "Хуесос" , "Пидор" , "Сука" , "БЛЯТЬ", "БЛЯ", "ХУЙ", "ПИЗДА", "ПИЗДЕЦ" , "ХУЕСОС" , "ПИДОР" , "СУКА"]
pon = ['понятно' , 'понятненько' , 'понял' , 'Понял' , 'Понятно']
banned = ['бан' , 'Бан' , 'БАН']
boshe = ['Боже' , 'боже']
klass = ['класс' , 'Класс' , 'КЛАСС']
zeleny = ['зеленый' , 'зелёный' , 'зеленка' , 'зеленый']
lox = ['лох' , 'ЛОХ' , 'Лох']
cho = ['чо' , 'чё' , 'че']
tochki = ['...']
funy = ['xd' , 'хд' , 'XD' , 'хд']
breakevery = ["l.daily", "l.d", "l.work", "l.w", "l.s", "l.sell" , "cc.ban" , ".tr" , ".avatar" , ".transcribe" , ".imagine" , ".dl" , ".download"]
votkomy = ["linux" , "линукс" , "Linux" , "Линукс" , "линь" , "убунту" , "минт" , "арч" , "федора" , "линус" , "gnome" , "кде"]
# word trigger , maybe i will improve this(NO LOL)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    slow_count.start()

@bot.event
async def on_member_join(member):
	guild = member.guild
	if guild.system_channel is not None:
		to_send = f'**Здарова, {member.mention}. Ты попал в наш экстремистский чат. \n \n Перед тем, как что-то написать в чат, не забывай что на этом сервере правят наркоманы убийцы , поэтому будь здесь осторожнее. \n \n Приятного общения :3** \n \n \n || https://cdn.discordapp.com/attachments/1209788395627216938/1313093751685517373/image.png ||'
		await guild.system_channel.send(to_send)

@tasks.loop(seconds=3.0, count=50000000000) # i don't care about this loop
async def slow_count():
	print(slow_count.current_loop)




@bot.event # for cooldowns
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"`Повтори команду через {round(error.retry_after, 2)} секунд!`" , delete_after=5)

@bot.command(name="say")
async def say(ctx, *, text):
    await ctx.send(f"{text}")


@bot.command(name="avatar")
async def say(ctx, *, text : discord.Member=None):
	userAvatarUrl = text.avatar.url
	await ctx.send(userAvatarUrl)

@bot.command(name="emoji")
async def emoji(ctx, emoji: discord.Emoji):
    embed=discord.Embed(title=f"**Эмодзи : {emoji.name}**")
    embed.set_thumbnail(url=f"{emoji.url}")
    embed.add_field(name="URL", value=f"{emoji.url}", inline=False)
    await ctx.send(embed=embed)

@bot.command(name="hoststatus")
async def hoststatus(ctx):
    embed=discord.Embed(title="Состояние хостинга", description=f"`Аптайм : ` {(slow_count.current_loop * 3) // 3600} часов {((slow_count.current_loop * 3) // 60) % 60} минут {(slow_count.current_loop * 3) % 60} секунд  \n `Хостинг который используется в данный момент : ` samsung SM-A015F" , color=0xe8ccff)
    embed.set_author(name="Зеленский", icon_url="https://cdn.discordapp.com/avatars/1312386610909937735/9e0f470f2c4a1910d06b7633259cf255.png?size=1024")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1312386610909937735/9e0f470f2c4a1910d06b7633259cf255.png?size=1024")
    await ctx.send(embed=embed , delete_after=120)

@bot.command(name="хелп")
async def хелп(ctx):
    embed=discord.Embed(title="Доступные команды", description="`%say` - **Бот пишет фразу** \n `%avatar` - **Отображает аватарку** \n `%emoji` - *Отображает эмодзи* \n 📰 - **Создаётся ветка для обсуждения**(только для доверенных людей , и добавлять вначале сообщения) \n 2️⃣3️⃣4️⃣ - **Ставит реакцию** (только для доверенных людей ) \n ❓ - **Создаёт голосование**(✅ ❌ , ставить вначале сообщения и только для доверенных людей) \n \n БОТ **НЕ** ПЕРЕСТАНЕТ РАБОТАТЬ <t:1710665700:R> `Бот создан : ` ~~@phibiiscool__.~~ , @ebalpixel", color=0xe8ccff)
    embed.set_author(name="Зеленский", icon_url="https://cdn.discordapp.com/attachments/905721004704296970/1207260782815875092/fd7a723bdeba999ba0f0a05277ee9422.png?ex=65df0038&is=65cc8b38&hm=93042d8bb33836fa9876ee78508d2cd3c90cca2093b50c4abb2fd79a34014dad&")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/905721004704296970/1207260782815875092/fd7a723bdeba999ba0f0a05277ee9422.png?ex=65df0038&is=65cc8b38&hm=93042d8bb33836fa9876ee78508d2cd3c90cca2093b50c4abb2fd79a34014dad&")
    await ctx.send(embed=embed, delete_after=15) # help command

cho = ['чо' , 'чё' , 'ЧЁ' , 'Чо']
xoxol = ['хохол' , 'хохлина' , 'хохлы' , 'Хохол' , 'Хохлина' , 'Хохлы' , 'ХОХОЛ' , 'ХОХЛИНА' , 'ХОХЛЫ' ,]

@bot.event
async def on_message(message):
	author = message.author
	randmnumber = random.randint(0, 5)
	randmeme = "https://tenor.com/view/%D0%B0-4-gif-14211769093273171637" , "https://media.discordapp.net/attachments/749768163968811081/1171875655651184701/speed.gif" , "https://tenor.com/view/sad-cat-gif-26067066" , "https://tenor.com/view/cat-berg-cat-orange-cat-swimming-gif-25177582" , "https://tenor.com/view/cat-kitty-pussycat-feline-gif-26001328" , "https://tenor.com/view/oneshot-spin-gif-8295119798900423556"
	if message.content == "б":
		await message.channel.send("__**БУБУН ЁБAНЫЙ ЧO НАДО? САМЫЙ УМНЫЙ ТУТ??? РЕАКЦИИ МОИ ЧЕКАТЬ РЕШИЛ!**__")
	elif message.content == "Б":
		await message.channel.send("__**БУБУН ЁБAНЫЙ ЧO НАДО? САМЫЙ УМНЫЙ ТУТ??? РЕАКЦИИ МОИ ЧЕКАТЬ РЕШИЛ!**__")
	elif any(word in message.content for word in badwords):
			await message.channel.send ('**ТЫ ЧO МАТЕРИШЬСЯ?! СОВСЕМ СТРАХ ПОТЕРЯЛ?! Разбейник ты! Уходи отсюдово! Це плoхo материться!**!')
	elif any(word in message.content for word in pon):
		await message.channel.send ("**МНЕ ПЛЕВАЦ ПОН ТЫ ИЛЕ НЕ ПОН! Я НЕ ПОН И ТОЧЬКА ЗОТКНИС ЖЫВА**")
	elif any(word in message.content for word in banned):
		await message.channel.send ("**СЛЫШ! ЩЯЗ ТИБЯ ЗОБAНИМ ТУТ, ПОНЕЛ?!!**")
	elif any(word in message.content for word in boshe):
		await message.channel.send ("**ГДЕ БОХ САЛА?**")
	elif any(word in message.content for word in klass):
		await message.channel.send ("**ТЫ В 1 КЛАCСЕ ЯСНА**")
	elif any(word in message.content for word in zeleny):
		await message.channel.send ("**СЛЫШЬ?? КОГО ТЫ ЗЕЛЕНЫМ НАЗВАЛ?**")
	elif any(word in message.content for word in lox):
		await message.channel.send ("**ТЫ ЛOХ, ЯСНО???**")
	elif message.content == "Б":
		await message.channel.send ("**БУБУН ЁБАНЫЙ ЧО НАДО? САМЫЙ УМНЫЙ ТУТ??? РЕАКЦИИ МОИ ЧЕКАТЬ РЕШИЛ!**")
	elif message.content == "б":
		await message.channel.send ("**БУБУН ЁБАНЫЙ ЧО НАДО? САМЫЙ УМНЫЙ ТУТ??? РЕАКЦИИ МОИ ЧЕКАТЬ РЕШИЛ!**")
	elif message.content == 'э':
		await message.channel.send ('**Чo ЭКoИШ ТЫ ТУПОИ ЗОТКНИС И ДАЙ САЛА ЦЕ ДЛЯ МЕНЯ!**')
	elif message.content == "😭":
		await message.channel.send ('**Чo ГРУСТИШ?! ПАШОЛ ТЫ НАФЕК ТАКОИ ГРУСНЫЙ!**')
	elif message.content == 'ля':
		await message.channel.send ('**ЧО ЛЯКАЕЩЬ?! ПОЕХОВШЫЙ ШТОЛЕ?!??!?!?! ИДЕОД МОЛЧИ ТУД У ТИБЯ МАТЕРЬ В КАНАВИ!**')
	elif message.content == 'блин':
		await message.channel.send ('**БЛИНЫ МНЕ ТВАЙА МАМА ГОТОВИЦ БУДЕД! ИДИ НАФЕК!**')
	elif message.content == 'м':
		await message.channel.send ('**ПОШЕЛ ТЫ КОРОВА ТУПАЙА ЙА ИЗ ТИБЯ САЛА СДЕЛАЙУ И БОГУ ПРОДАМ ЛОХ ТЫ ТУПОИ**')
	elif any(word in message.content for word in tochki):
		await message.channel.send ("**ПОШЕЛ НАФИГ ЧМО ТЫ ВАЩЭ! ЦЕ НЕКУЛЬТУРНО МНОГА ТОЧИК СТАВИТЬ ТЫ ЗНАЕШ ЭТО А Я ДА!**")
	elif any(word in message.content for word in funy):
		await message.channel.send ("**ЧO ТЫ ТУТ РЖOШ!?!?!?!?!? ВАЩЭ ШТОЛЕ СТРАХ ПАТИРЯЛ! Я ТИБЯ СИЙЧАС УЗНАЮ ПО ОЙПИ!!!!!**")

	elif any(word in message.content for word in cho):
		if message.author != "1312386610909937735":
			await message.channel.send("**НИЧO!**")
	elif message.content == "да":
		await message.channel.send("**Нет**")
	elif message.content == "ДА":
		await message.channel.send("**Нет**")
	elif message.content == "Да":
		await message.channel.send("**Нет**")
	elif any(word in message.content for word in votkomy):
		await message.channel.send("https://cdn.discordapp.com/attachments/1199215458973401111/1204717909906165770/animation.gif.gif?ex=65d5bffc&is=65c34afc&hm=03020ea8998dc24db9f0f32fd9dc9e7d6e1eee3635135bee59276204dbe03d66&")

	elif re.findall("класс", message.content):	
		await message.channel.send("**ТЫ В 1 КЛАССЕ ЯСНА**")
	elif re.findall("ля", message.content):
		await message.channel.send("**ЧО ЛЯКАЕШЬ?! ПОЕХАВШЫЙ ШТОЛИ?!??!?!?! ИДИОТ МОЛЧИ**")
	elif any(word in message.content for word in xoxol):
		await message.channel.send(f"**ЧО , {author.mention} , ВАЩЕ ПАЕХАВШЫЙ ШТОЛЕ?!?!?! ПАШОЛ АТСЮДА! ТЕБЕ ТУД НИ РАДЫ!!!**")
	elif message.content == "<@1312386610909937735>":
		if message.author != "1312386610909937735":
			await message.channel.send(f"**__Э ТЫ ЧО , {author.mention} АФИГЕЛ??? ЩА САЛОМ КИДАЦА БУДУ!!!__**")
	elif message.content == "г":
		await message.channel.send("**__ГОВНО СТАРОЕ! МОЛЧИ В УГОЛОЧКЕ ЕБЛАН ТЫ ТУПОЙ! РЕАКЦИИ ПРОДОЛЖАЕШЬ МОИ ИСКАТЬ???!__**")
	elif re.findall("ыыы", message.content):	
		await message.channel.send("**ЫЫЫЫЫ**")

	await bot.process_commands(message)



bot.run(token) 
