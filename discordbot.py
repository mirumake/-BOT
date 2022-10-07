import discord
from discord.channel import VoiceChannel
from discord.player import FFmpegPCMAudio
import pydub
from tsukuyomichan_talksoft import TsukuyomichanTalksoft
tsukuyomichan_talksoft = TsukuyomichanTalksoft(model_version='v.1.2.0')
fs = 24000

TOKEN = 'MTAyNzc3MTc4NDUwNzk2NTQ4Mg.GqoVMF.P7-6j3pj-Ifahc4UjVXbfg8A14GpBaF6sOK12A'
client = discord.Client()

voiceChannel: VoiceChannel 

@client.event
async def on_ready():
    print('つくよみちゃんがサーバーにログインしました！')

@client.event
async def on_message(message):
    global voiceChannel
    channel_id = 01234567890123456789
    if message.channel.id != channel_id:
        return

    if message.author.bot:
        return
    if message.content == '!tukuyomi':
        voiceChannel = await VoiceChannel.connect(message.author.voice.channel)
        await message.channel.send('つくよみちゃんが参加したよ！')
        return
    elif message.content == '!dtukuyomi':
        voiceChannel.stop()
        await message.channel.send('つくよみちゃんが退出したよ！')
        await voiceChannel.disconnect()
        return

    play_voice(message.content)

def play_voice(text):
    wav = tsukuyomichan_talksoft.generate_voice(text, 0)
    sound = pydub.AudioSegment.from_wav("out.wav")
    sound.export("out.mp3", format="mp3")
    voiceChannel.play(FFmpegPCMAudio("out.mp3"))
