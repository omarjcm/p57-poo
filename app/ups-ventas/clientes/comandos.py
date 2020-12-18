import click

from clientes.servicios import ClienteServicios
from clientes.servicios import Cliente


@click.group()
def clientes():
    """
    Administra a los clientes.
    """
    pass


@clientes.command()
@click.option('-n', '--nombre',
                type=str, 
                prompt=True,
                help='El nombre del cliente es ')
@click.option('-e', '--empresa',
                type=str, 
                prompt=True,
                help='La empresa del cliente es ')
@click.option('-c', '--correo',
                type=str, 
                prompt=True,
                help='El correo del cliente es ')
@click.option('-p', '--posicion',
                type=str, 
                prompt=True,
                help='La posición del cliente es ')
@click.pass_context
def crear(ctx, nombre, empresa, correo, posicion):
    """
    Crea un nuevo cliente.
    """
    cliente = Cliente(nombre, empresa, correo, posicion)
    cliente_servicio = ClienteServicios( ctx.obj['cliente_tabla'] )
    cliente_servicio.cliente_crear( cliente )


@clientes.command()
@click.pass_context
def listar(ctx):
    """
    Lista a todos los clientes
    """
    pass


@clientes.command()
@click.pass_context
def actualizar(ctx, id_cliente):
    """
    Actualiza a un cliente
    """
    pass


@clientes.command()
@click.pass_context
def eliminar(ctx, id_cliente):
    """
    Elimina un cliente
    """
    pass


all = clientes