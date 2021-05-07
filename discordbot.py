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


bot.run(token)
