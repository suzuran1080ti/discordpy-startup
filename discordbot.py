from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def begin(ctx):
    await ctx.send('3MEサーバーへようこそ！')
    await ctx.send('まずは「/tutorial」と入力して、サーバーについて学びましょう！')


@bot.command()
async def tutorial(ctx):
    await ctx.send('チュートリアルを開始します！')
    await ctx.send('知りたい内容があれば以下のコマンドを入力してください！')
 
    await ctx.send('/server')
    await ctx.send('サーバーの概要')

    await ctx.send('/authority')
    await ctx.send('サーバー権限')

    await ctx.send('/whistle')
    await ctx.send('笛の種類')

    await ctx.send('/terms')
    await ctx.send('利用規約')

    await ctx.send('/next')
    await ctx.send('次へ進む')


@bot.command()
async def server(ctx):
    await ctx.send('このサーバーは有志によって作られたクラスサーバーです。')
    await ctx.send('ここでは課題や予定の管理をはじめとし、様々なコミュニケーションを図れます。')
    await ctx.send('また、サーバー内には権限を管理する「笛」によって出現するチャンネルや「寮生専用チャット」「イブニングトーク」等の非公開チャンネルも存在します。')
    
    
@bot.command()
async def authority(ctx):
    await ctx.send('このサーバーでは笛によって階級が定められています。')
    await ctx.send('詳細は/whistleで確認できますが、通常の機能を使うのであれば「鈴付き」で申し分ありません。')


@bot.command()
async def whistle(ctx):
    await ctx.send('笛はサーバーでの活動の評価値に準じて付与され、階級が上がるごとに機能が解禁されていきます。')

    await ctx.send('主に解禁される機能（頻繁に変更します）')
    await ctx.send('青笛・上位ボイスチャンネルの使用/コマンド部屋の閲覧')
    await ctx.send('月笛・招待リンクの作成/サーバーミュート/コマンド部屋の使用')
    await ctx.send('黒笛・チャンネル改変/ユーザーのキック/ニックネーム変更') 
    
      


bot.run(token)
