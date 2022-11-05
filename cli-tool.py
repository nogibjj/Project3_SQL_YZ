import typer
from userGender import userGender
from userAge import userAge
from userLanguage import userLanguage
from userDestination import userDestination

main = typer.Typer()

@main.command()
def getUserGender():
    result1, result2 = userGender()
    print("Plot of User Gender Distribution created!")
    typer.echo(result1)
    typer.echo(result2)

@main.command()
def getUserAge():
    result = userAge()
    print("Plot of User Age Distribution created!")
    typer.echo(result)

@main.command()
def getUserLanguage():
    result1, result2 = userLanguage()
    print("Plot of User Language Distribution created!")
    print("Plot of Non-English Speaking User Language Distribution created!")
    typer.echo(result1)
    typer.echo(result2)

@main.command()
def getUserDestination():
    result = userDestination()
    print("Plot of User Destination Distribution created!")
    typer.echo(result)

if __name__ == "__main__":
    main()