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
    await ctx.send('次へ')


@bot.command()
async def server(ctx):
    await ctx.send('このサーバーは有志によって作られたクラスサーバーです。')
    await ctx.send('ここでは課題や予定の管理をはじめとし、様々なコミュニケーションを図れます。')
    await ctx.send('また、サーバー内には、権限を管理する「笛」によって出現するチャンネルや「寮生専用チャット」「イブニングトーク」等の非公開チャンネルも存在します。')
   
    
@bot.command()
async def authority(ctx):
    await ctx.send('このサーバーでは笛によって階級が定められています。')
    await ctx.send('詳細は/whistleで確認できますが、通常の機能を使うのであれば「鈴付き」で申し分ありません。')
    
@bot.command()
async def whistle(ctx):
    await ctx.send('笛はサーバーでの活動の評価値に準じて付与され、階級が上がるごとに機能が解禁されていきます。')
    await channel.send(file=discord.File('840138425809895434'))
    await ctx.send('主に解禁される機能（頻繁に変更します')
    await ctx.send('青笛・上位ボイスチャンネルの使用/コマンド部屋の閲覧')
    await ctx.send('月笛・招待リンクの作成/サーバーミュート/コマンド部屋の使用')
    await ctx.send('黒笛・チャンネル改変/ユーザーのキック/ニックネーム変更')

@bot.command()
async def terms(ctx):
    await ctx.send('本サービスにおいては、利用希望者が「次へ」を押した時点で本規約に同意したとみなします。')
    await ctx.send('当運営は、ユーザーに事前に通知することなく本サービスの一部を停止または中断することができるものとします。')
    await ctx.send('当運営は、ユーザーに事前に通知することなく、投稿データの削除及びユーザー登録の抹消ができるものとします。')
    await ctx.send('当運営は、必要と判断した場合には、ユーザーに事前に通知することなく本規約を変更することができるものとします。')
    await ctx.send('当運営は、事実上または法律上の瑕疵が無いことを保証しておりません。本サービスにおいて、ユーザーと他ユーザーの間において生じたあらゆる損害について一切の責任を負いません')
    await ctx.send('当運営の判断において、ユーザーの登録を抹消した際に、該当ユーザーからの批判はご遠慮ください。')
    await ctx.send('本サービスにおいては、利用希望者が「次へ」を押した時点で本規約に同意したとみなします。')
    await ctx.send('ユーザーは、本サービスを利用するにあたって、以下の行為を禁じます。')
  　await ctx.send('・法令または公序良俗に違反する行為')
  　await ctx.send('・第三者になりすまし、サーバーへアクセスする行為')
    await ctx.send('・当運営のサービスに関する運営を妨害する行為')
    await ctx.send('・過度な暴力的な表現（判断は相対的に行う）')
    await ctx.send('・露骨な嫌がらせ、または性的表現')
    await ctx.send('以上の規約に反した場合、当運営は然るべき処置を検討いたします。')
    
bot.run(token)
