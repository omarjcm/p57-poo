import click

@click.group()
def clientes():
    """
    Administra a los clientes.
    """
    pass

@clientes.command()
@click.pass_context
def crear(ctx, nombre, empresa, correo, posicion):
    """
    Crea un nuevo cliente.
    """
    pass

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