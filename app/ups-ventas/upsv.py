import click

from clientes import comandos as clientes_comandos

CLIENTES_TABLA = '.clientes.csv'


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}
    ctx.obj['cliente_tabla'] = CLIENTES_TABLA


cli.add_command( clientes_comandos.all )