import click

from clientes import comandos as clientes_comandos

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}

cli.add_command( clientes_comandos.all )