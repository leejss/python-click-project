import click


def compute_sum(ctx, param, value):
    if value:
        click.echo("Enter 0 to exit")
        total = 0
        while True:
            value = click.prompt("Enter Number: ", type=int)
            total += value
            if value == 0:
                if click.confirm("Do you want to exit? "):
                    click.echo(f'Sum: {total}')
                    ctx.exit()
                    break


def find_max(ctx, param, value):
    if value:
        click.echo("Enter 0 to exit")
        max_number = 0
        while True:
            value = click.prompt("Enter Number: ", type=int)
            max_number = max(max_number, value)
            if value == 0:
                if click.confirm("Do you want to exit? "):
                    click.echo(f'Max: {max_number}')
                    ctx.exit()
                    break


@click.command()
@click.option('--sum', help="Compute sum and return", is_flag=True, callback=compute_sum, expose_value=False)
@click.option('--max', help="Find max in given number", is_flag=True, callback=find_max, expose_value=False)
def compute():
    pass
