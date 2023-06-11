import discord,asyncio
import random,math,time
default=["마지막에 말씀을 잘 못 이해 한것 같아요.","방금 하신 말씀을 잘 못 알아들었어요.","죄송해요. 다시 들려 주실래요?","제가 제대로 이해하고 있는지 잘 모르겠어요.","조금 헷갈리는데요.","제가 제대로 이해하지 못한것 같아요. 죄송해요."]
welcome=['오랜만이야','안녕','저기','잘 있었어','고마워','잘있었어','반가워','오랜만','어떻게 지냈어','잘 지냈니','오늘 어때']
welcome_response=['안녕하세요','안녕','오랜만이야 못 본 사이 그댄 얼굴이 좋아보여']
carrer_response=["웹 개발자가 꿈이에요","앱 개발자가 꿈이에요",'개발자가 꿈이에요']
carrer=["꿈",'진로','직업']
study=['교과','과목']
study_response=['화학','프로그래밍']
major=['전공','대학','과','대입']
major_response=['컴공과가 꿈이에요','컴퓨터 공학과에 진학하고 싶어요','저는 컴퓨터 공학을 전공하고 소프트웨어 개발자로 성장하고 싶어요.','전기전자공학과에 진학하고 싶어요.']
project=['걸린 시간','걸린시간','진행시간','프로젝트 진행','챗봇 작업','작업 시간','작업']
project_response=['작업 시간은 30시간정도 같습니다.','2023-5-27 ~ 2023-6-12 from Shin CY']
client = discord.Client(intents=discord.Intents.default())
prefix ='!'
@client.event
async def on_ready(): #Once the bot runs, the message runs
    print("봇이 실행중입니다.")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("작동되는 코드는 !help 를 쳐보세요"))
@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Ignore messages sent by the bot itself

    cmd = message.content
    for i in project:
        if i in cmd:
            await message.channel.send(random.choice(project_response))
            return
    for i in welcome:
        if i in cmd:
            await message.channel.send(random.choice(welcome_response))
            return
    for i in carrer:
        if i in cmd:
            await message.channel.send(random.choice(carrer_response))
            return
    for i in study:
        if i in cmd:
            await message.channel.send(f"과목은 {random.choice(study_response)}을 좋아해요")
            return
    for i in major:
        if i in cmd:
            await message.channel.send(random.choice(major_response))
            return
    if "테스트" in cmd:
        await message.channel.send("{} | {}, Hello".format(message.author, message.author.mention))
    elif "이름" in cmd:
        await message.channel.send("2학년 3반 13번 신찬영 입니다.")
    elif "!정보" in cmd:
        await message.channel.send("챗봇을 만들고 싶어서 만들기 시작한 프로젝트가 완성이 되었습니다.")
    elif "!랜덤" in cmd:
        await message.channel.send(random.randint(0,100))
    elif cmd=='!help':
        await message.channel.send("테스트, 이름, !정보 ,!랜덤")
    else:
        # Send a random pre-prepared response for undefined input
        response = random.choice(default)
        await message.channel.send(response)
