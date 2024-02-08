import click
from .line_helper import LineHelper


@click.command()
@click.argument("filepath")
def skillcorner_line_cleaner(filepath) -> None:

    to_parse_file = None
    try:
        to_parse_file = open(filepath, "r")
    except FileNotFoundError:
        raise click.FileError(filepath, "File not found.")

    count = 0
    while True:
        # Get next line from file
        line = to_parse_file.readline()

        # if line is empty
        # end of file is reached
        if not line:
            break

        try:
            line_helper = LineHelper(line_number=count, line=line)
            line_helper.calculate_line()
        except Exception as e:
            click.echo(f"Line {count}: Error {e}")
            continue

        click.echo(f"{count} : {line_helper.line.strip()}")

        count += 1

    to_parse_file.close()
