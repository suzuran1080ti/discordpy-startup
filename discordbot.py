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
    await ctx.send('チュートリアルを開始します。')
    await ctx.send('知りたい内容があれば以下のコマンドを入力してください！')
    
    await ctx.send('/server')
    await ctx.send('サーバーの概要')



@bot.command()
async def server1(ctx):
    await ctx.send('このサーバーは有志によって作られたクラスサーバーです。')
    await ctx.send('ここでは課題や予定の管理をはじめとし、様々なコミュニケーションを図れます。')


class PagerWithEmojis:
    """
    受け取った絵文字によってページを移動するためのクラス
    """
    LEFT_ARROW: str = "\N{LEFTWARDS BLACK ARROW}\N{VARIATION SELECTOR-16}"
    RIGHT_ARROW: str = "\N{BLACK RIGHTWARDS ARROW}\N{VARIATION SELECTOR-16}"
    STOP: str = "\N{CROSS MARK}"
    # 処理に必要な絵文字を変数として持っておく

    def __init__(self, pages:list[discord.Embed]):
        self.page_index: int = 0
        self.pages: list[discord.Embed] = pages

    @property
    def now_page(self) -> discord.Embed:
        return self.pages[self.page_index]

    @property
    def max_page_index(self) -> int:
        return len(self.pages) - 1

    @property
    def page_emojis(self) -> list[str]:
        """
        現在ページを出力する際に追加する必要のある絵文字のリストを返します。
        """
        emojis: list[str] = [self.LEFT_ARROW,self.RIGHT_ARROW,self.STOP]
        if self.page_index == 0:
            # もし、今最初のページにいるなら左へ移動する絵文字を除外する
            emojis.remove(self.LEFT_ARROW)
        if self.page_index == self.max_page_index:
            # もし、今最後のページにいるなら右へ移動する絵文字を除外する
            emojis.remove(self.RIGHT_ARROW)
        return emojis

    def move_page_by_emoji(self, emoji: str):
        """
        絵文字を受け取って、参照するページを変更します。
        """
        if emoji == self.LEFT_ARROW:
            self.page_index -= 1
        elif emoji == self.RIGHT_ARROW:
            self.page_index += 1

    async def discord_pager(self, ctx: commands.Context):
        """
        コマンドのContextを受け取って、Discord上でページ移動の受付・処理を行います。
        """
        now_page = self.now_page
        emojis = self.page_emojis
        # 現在ページ内容と、出力に必要な絵文字を取得
        msg: discord.Message = await ctx.send(embed=now_page)

        for emoji in emojis:
            await msg.add_reaction(emoji)

        def check(reaction: discord.Reaction, user: discord.User) -> bool:
            # リアクション先のメッセージや追加された絵文字が適切かどうか判断する。
            return str(reaction.emoji) in emojis and reaction.message == msg and user == ctx.author

        while True:
            reaction, _ = await ctx.bot.wait_for("reaction_add",check=check)
            await msg.clear_reactions()  # 事前に全てのリアクションを削除しておく。
            if str(reaction.emoji) == self.STOP:
                # 停止用の絵文字が追加された場合、リアクションを新たに付与することなく終了する。
                break
            self.move_page_by_emoji(str(reaction.emoji))
            now_page = self.now_page
            emojis = self.page_emojis
            await msg.edit(embed=now_page)

            for emoji in emojis:
                await msg.add_reaction(emoji)


@bot.command()
async def server(ctx: commands.Context):
    pages: list[discord.Embed] = [
        discord.Embed(
            title="1ページ目です。",
            description="最初のページなので、右矢印とバツマークのリアクションが追加されます。",
            color=discord.Color.random()
        ),
        discord.Embed(
            title="2ページ目です。",
            description="左矢印と右矢印に、バツマークのリアクションも追加されます。",
            color=discord.Color.random()
        ),
        discord.Embed(
            title="最後のページです。",
            description="最後のページなので、左矢印とバツマークのリアクションが追加されます。",
            color=discord.Color.random()
        )
    ]
    pager = PagerWithEmojis(pages)
    await pager.discord_pager(ctx)

bot.run("TOKEN")

    
    


