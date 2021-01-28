import click


@click.command()
@click.option('--sum', help="Compute sum and return")
@click.option('--max')
def compute():
    pass