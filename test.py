import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

@click.command()
@click.option('--csv', default=1, help='Comma seperated values')
@click.option('--term', default=8, help='Value to count')
def count_val(csv, term):
    sum = 0
    for x in csv:
        sum += 1
    print(sum)

if __name__ == '__main__':
    hello()
    count_val()
