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
    await ctx.send('まずは「/tutorial」と入力してユーザー登録を実行しましょう！')
    await ctx.send('※このチャンネルは他のユーザーに閲覧されません。')

@bot.command()
async def tutorial(ctx):
    await ctx.send('チュートリアルを開始します！')
    await ctx.send('知りたい内容があれば以下のコマンドを入力してください！')
    await ctx.send('━━━━━━━━━━━━━━━━')
    await ctx.send('/server')
    await ctx.send('「サーバーの概要」')
    await ctx.send('━━━━━━━━━━━━━━━━')
    await ctx.send('/authority')
    await ctx.send('「サーバー権限」')
    await ctx.send('━━━━━━━━━━━━━━━━')
    await ctx.send('/whistle')
    await ctx.send('「笛の詳細」')
    await ctx.send('━━━━━━━━━━━━━━━━')
    await ctx.send('/next')
    await ctx.send('「次へ進む」')
    await ctx.send('━━━━━━━━━━━━━━━━')
    await ctx.send('知りたい内容が無い場合は上記の利用規約をよく読んだうえで「/next」と入力してください！')

@bot.command()
async def server(ctx):
    await ctx.send('このサーバーは有志によって作られたクラスサーバーです。')
    await ctx.send('ここでは課題や予定の管理をはじめとし、様々なコミュケーションを図る事ができます。')
    await ctx.send('━━━━━━━余談━━━━━━━')
    await ctx.send('サーバー内には「笛」によって出現するチャンネルや「寮生専用チャット」「イブニングトーク」等の非公開チャンネルも多数存在します。')
    
    
@bot.command()
async def authority(ctx):
    await ctx.send('このサーバーでは笛によって階級が定められています。')
    await ctx.send('詳細は上記の表や/whistleで確認できますが、通常の機能を使うのであれば「鈴付き」で申し分ありません。')


@bot.command()
async def whistle(ctx):
    await ctx.send('笛はサーバーでの活動の評価値に応じて付与され、階級が上がるごとに機能が解禁されていきます。')
    await ctx.send('笛の種類と条件については上記の資料をご覧ください。')
    await ctx.send('【主に解禁される機能】')
    await ctx.send('━━━━━━━━━━━━━━━━')
    await ctx.send('青笛・上位ボイスチャンネルの使用/コマンド部屋の閲覧/ニックネーム変更')
    await ctx.send('━━━━━━━━━━━━━━━━')
    await ctx.send('月笛・招待リンクの作成/サーバーミュート/コマンド部屋の使用')
    await ctx.send('━━━━━━━━━━━━━━━━')
    await ctx.send('黒笛・チャンネル改変/ユーザーのキック/ニックネーム管理') 
    await ctx.send('━━━━━━━━━━━━━━━━')
    await ctx.send('※その他、各チャンネルにて権限が付与されます。')
    
      
@bot.command()
async def next(ctx):

    await ctx.send('━━━━━━━━━━━━━━━━')
    await ctx.send('利用規約に同意しました！')
    await ctx.send('━━━━━━━━━━━━━━━━')
    await ctx.send('管理者がニックネームとロールを付与致しますので、自分の氏名と出席番号を入力してお待ちください！')

bot.run(token)
