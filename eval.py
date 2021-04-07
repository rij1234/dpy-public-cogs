'''
This is modified from https://gist.github.com/nitros12/2c3c265813121492655bc95aa54da6b9
Includes evals for syntax highlighted codeblocks
'''

def insert_returns(body):
    # insert return stmt if the last expression is a expression statement
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    # for if statements, we insert returns into the body and the orelse
    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    # for with blocks, again we insert returns into the body
    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)


@bot.command(aliases=["eval","e"])
@commands.is_owner()
async def evaluate(ctx,*,cmd):
  if ctx.author.id in bot.admin_id:
    fn_name = "_eval_expr"
#    return await ctx.send(cmd)
    cmd.replace("```py", "")
    if cmd.endswith('```'):
        cmd = cmd[:-3]
    if cmd.startswith('```py'):
        cmd = cmd[5:]
    if cmd.startswith('```'):
        cmd = cmd[3:]

    # add a layer of indentation
    cmd = "\n".join(f"    {i}" for i in cmd.splitlines())

    # wrap in async def body
    body = f"async def {fn_name}():\n{cmd}"

    parsed = ast.parse(body)
    body = parsed.body[0].body
    insert_returns(body)

    env = {
        'bot': ctx.bot,
        'discord': discord,
        'commands': commands,
        'ctx': ctx,
        '__import__': __import__
    }
    exec(compile(parsed, filename="<ast>", mode="exec"), env)

    result = (await eval(f"{fn_name}()", env))
    try:
        await ctx.send(f"```{result}```")
    except:
        return
