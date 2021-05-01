# NicoNico

import discord
from niconico_dl_async import NicoNico

client = discord.Client()

# 起動したらメッセージ。
@client.event
async def on_ready():
    print("起動しました。")

@client.event
async def on_message(message):
    # もしBotだったら反応しない。
    if message.author.bot:
        return

    # メッセージの内容の最初が!playなら。
    if message.content.startswith("!play"):
        # チャンネルに入力中を送信する。
        await message.channel.trigger_typing()
        # もしボイスチャンネルに接続していないなら、コマンド実行者のボイスチャンネルに接続する。
        if not message.guild.voice_client:
            await message.author.voice.channel.connect()
        # メッセージの内容を/で分けてできたリストの最後を取得する。
        # urlの最後にニコニコ動画のIDがあるはずだからそれをniconico_dlに渡す。
        nico_id = message.content.split("/")[-1]
        niconico = NicoNico(nico_id)
        # 動画のURLを取得する。
        url = await niconico.get_download_link()
        # 動画のURLからオーディオソースを作る。(ffmpegが必要)
        player = discord.FFmpegPCMAudio(url)
        # 再生する。 
        # playのafterという引数に終了時に実行してほしいものを入れた関数を入れることができる。
        # niconico_dlはurlの使用が終わった後にclose()しなければいけない。
        # なのでclose()をしてくれる関数をafterに入れる。
        # 入れる関数にはエラー時のエラーメッセージをとる。
        # 今回はlambdaを使って関数を作る。(lambdaについてはここを参考にしよう: https://qiita.com/nagataaaas/items/531b1fc5ce42a791c7df)
        after = lambda e: niconico.close()
        message.guild.voice_client.play(player, after=after)
        # 通知メッセージ。
        await message.channel.send("再生します。")

# 接続する。
client.run("TOKEN")
