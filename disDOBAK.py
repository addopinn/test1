import os
import csv
import Dtime
import random
import discord
import datetime
from discord.ext import commands
from discord.ext.commands import Bot
from Dtime import Uptime
import pymysql
conn = None
cur = None
data1 = ""
data2 = ""
data3 = ""

data9 = ""

sql = ""

client = discord.Client()
Uptime.uptimeset()
token = "your token"
######################################################################### former sys

@client.event
async def on_ready():
    print(client.user.name)
    print('로그인 완료')
    print("="*50)
    play = discord.Game("투자연습 준비 끝!")
    await client.change_presence(status=discord.Status.online, activity=play)

@client.event
async def on_message(message):
    if message.content.startswith("!리포트"):
        msg = message.content[28:]
        embed = discord.Embed(title=f"새 리포트!")
        embed.add_field(name="리포트", value=f"``{message.content}``", inline=True)
        await client.get_channel(828633748572471316).send(embed=embed)
        await message.channel.send("리포트가 성공적으로 전송되었습니당!")
 
    if message.content.startswith("!청소"):
        number = int(message.content.split(" ")[1])
        print(message.author, "님이 메세지", number, "개 삭제")
        await message.delete()  
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메세지가 삭제되었습니다.")

###########################################################New Sys
    if message.content.startswith("!도움말"):
        print(message.author,"님이 도움을 요청하셨습니다.")
        embed = discord.Embed(title="도움말!")
        embed.add_field(name="|  가격 살펴보기  |", value="!현재가격")
        embed.add_field(name="  자신의 정보 조회  |",value="!내정보")
        embed.add_field(name="  용어정리!  ", value= "\"매수\" ==> 구매!  |  \"매도\" ==> 판매!", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("!현재가격"):
        print(message.author,"님이 현재가격을 조회하셨습니다.")
        cost = random.randrange(1,100001)
        embed = discord.Embed(title="현재가격!")
        embed.add_field(name="두근두근! 가격은?", value=f"{cost}원입니다!")
        await message.channel.send(embed=embed)
        msg = await message.channel.send("이 가격에 매수는 🔼를, 매도는 🔽를 선택해주세요")
        await msg.add_reaction("🔼")
        await msg.add_reaction("🔽")

    if message.content.startswith("!내정보"):
        print(message.author,"님이 본인의 정보를 확인했습니다")
        conn = pymysql.connect(host='127.0.0.1', user='root', password='kkkk123', db='Pingu', charset='utf8') 
        cur = conn.cursor() 
        print("DB접속 성공!")
        cur.execute("SELECT discordID FROM userTable")
        while (True) :
            row = cur.fetchone()
            if #row2에 있는 정보 == message.author.id:
                await message.channel.send("|   ID   |    이름    |     보유 현금     | 보유 코인 |  직업  | 환전횟수 | 페널티 횟수 | 가입한 날짜 |")
                await message.channel.send(("%15s %5s %15s %15s %15s %15s %5s %15s %15s %15s" % ("    ",row[0], row[1],row[3],row[4],row[5],row[6],drow[7],"         ",row[8])))
                break
        conn.close()

    if message.content.startswith("!매수"):
        print(message.author, "님이 매수를 결정!")
        su = await message.channel.send("매수를 결정하셨습니다! 몇 개를 매수할까요?")
        print(author.id, "매수#직접")
        await su.add_reaction("1️⃣")
        await su.add_reaction("2️⃣")
        await su.add_reaction("3️⃣")
        await su.add_reaction("4️⃣")
        await su.add_reaction("5️⃣")
        await su.add_reaction("6️⃣")
        await su.add_reaction("7️⃣")
        await su.add_reaction("8️⃣")
        await su.add_reaction("9️⃣")

    if message.content.startswith("!매도"):
        print(message.author, "님이 매도를 결정!")
        do = await message.channel.send("매도를 결정하셨습니다! 몇 개를 매도할까요?")
        print("매도#직접")
        await do.add_reaction("1️⃣")
        await do.add_reaction("2️⃣")
        await do.add_reaction("3️⃣")
        await do.add_reaction("4️⃣")
        await do.add_reaction("5️⃣")
        await do.add_reaction("6️⃣")
        await do.add_reaction("7️⃣")
        await do.add_reaction("8️⃣")
        await do.add_reaction("9️⃣")  

    if message.content.startswith("!DB추가"):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='kkkk123', db='Pingu', charset='utf8') 
        cur = conn.cursor() 
        print("DB접속 성공")
        await message.channel.send("콘솔을 확인하세요")
        while (True):
            data1 = input("사용자 ID를 입력하세요(엔터 클릭 시 종료): ") 
            if data1 == "":
                break; 
            data2 = input("사용자 이름을 입력하세요: ") 
            data3 = input("사용자 디스코드 ID를 입력하세요: ")
            data4 = input("보유 돈을 입력하세요: ")
            data5 = input("보유 코인을 입력하세요: ")
            data6 = input("직업을 입력하세요: ")
            data7 = input("물건환전 횟수를 입력하세요: ")
            data8 = input("페널티 횟수를 입력하세요: ")
            data9 = input("가입일을 입력하세요: ")
            sql = "INSERT INTO userTable VALUES('" + data1 + "','" + data2 + "','" + data3 + "','" + data4 + "','" + data5 + "','" + data6 + "','" + data7 + "','" + data8 + "','" + data9 + "')" #sql변수에 INSERT SQL문 입력 
            cur.execute(sql)
        conn.commit()
        print("DB저장 성공!")
        DBOK = await message.channel.send(f"<@{message.author.id}> DB저장에 성공했습니다")
        await DBOK.add_reaction("✅")
        conn.close()
                
    


@client.event
async def on_reaction_add(reaction, user):
    if user.bot == 1: #봇이면 패스
        return None

    if str(reaction.emoji) == "🔼":
        print(user, "님이 매수를 결정했어요!")
        su = await reaction.message.channel.send(user.name + "님이 매수를 결정하셨습니다. 몇 개를 매수할까요?")
        print("매수2")
        await su.add_reaction("1️⃣")
        await su.add_reaction("2️⃣")
        await su.add_reaction("3️⃣")
        await su.add_reaction("4️⃣")
        await su.add_reaction("5️⃣")
        await su.add_reaction("6️⃣")
        await su.add_reaction("7️⃣")
        await su.add_reaction("8️⃣")
        await su.add_reaction("9️⃣")
        
    elif str(reaction.emoji) == "🔽":
        print(user, "님이 매도를 결정했어요!")
        do = await reaction.message.channel.send(user.name + "님이 매도를 결정하셨습니다. 몇 개를 매도할까요?")
        print("매도2")
        await do.add_reaction("1️⃣")
        await do.add_reaction("2️⃣")
        await do.add_reaction("3️⃣")
        await do.add_reaction("4️⃣")
        await do.add_reaction("5️⃣")
        await do.add_reaction("6️⃣")
        await do.add_reaction("7️⃣")
        await do.add_reaction("8️⃣")
        await do.add_reaction("9️⃣")
    if str(reaction.emoji) == "1️⃣":
        do = await reaction.message.channel.send(user.name + "1")
    if str(reaction.emoji) == "2️⃣":
        do = await reaction.message.channel.send(user.name + "2")
    if str(reaction.emoji) == "3️⃣":
        do = await reaction.message.channel.send(user.name + "3")
    if str(reaction.emoji) == "4️⃣":
        do = await reaction.message.channel.send(user.name + "4")
    if str(reaction.emoji) == "5️⃣":
        do = await reaction.message.channel.send(user.name + "5")
    if str(reaction.emoji) == "6️⃣":
        do = await reaction.message.channel.send(user.name + "6")
    if str(reaction.emoji) == "7️⃣":
        do = await reaction.message.channel.send(user.name + "7")
    if str(reaction.emoji) == "8️⃣":
        do = await reaction.message.channel.send(user.name + "8")
    if str(reaction.emoji) == "9️⃣":
        do = await reaction.message.channel.send(user.name + "9")
    

    

client.run(token) 
