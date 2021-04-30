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
    await ctx.send('3MEサーバーへようこそ！まずは「/tutorial」と入力して、サーバーについて学びましょう！')


@bot.command()
async def tutorial(ctx):
    await ctx.send('チュートリアルを開始します。')
    await ctx.send('知りたい内容があれば以下のコマンドを入力してください！')
    
@bot.command()
async def server(ctx):
    await ctx.send('このサーバーは有志によって作られたクラスサーバーです。ここでは課題や予定の管理をはじめとし、様々なコミュニケーションを図れます。')
     

bot.run(token)

    
    


