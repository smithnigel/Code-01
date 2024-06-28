import typer
import subprocess
from PyInquirer import prompt, print_json, Separator
from rich import print as rprint
from art import *
from rich.console import Console
from rich.panel import Panel


app = typer.Typer()
console = Console()

mih = text2art("\n\n\n\nWEATHER.io", font="alligator3")
console.print(mih, style="blue")
rprint(Panel.fit("[bold yellow]Creator: Nigel Smith                             ", style="bold yellow"))


@app.command("tools")
def sample_func():
    module_list_question = questions = [
        {
            'type': 'list',
            'name': 'username',
            'message': 'Select any one operation: ',
            'choices': [
                        {
                            'name': 'Weather',
                        },
                        {
                            'name': 'Hurricanes',
                        },
                        {
                            'name': 'Ask questions >>>',
                        },
                        {
                            'name': 'Exit',
                        },
            ],
        }
    ]


    username = prompt(module_list_question)

    if username['username'].__eq__("Weather"):
        city = input()
        print(city)
    
    if username['username'].__eq__("Hurricanes"):
        return

    if username['username'].__eq__("Ask questions >>>"):
        return

    if username['username'].__eq__("Exit"):
        exit()
        

    rprint("[yellow]=============================================[yello]")
    rprint("[green bold]Enter folder name :[green bold]")
    folder_name = input()


    subprocess.run(f"mkdir {folder_name}_created_by_{username['username']}", shell=True)

@app.command("test")
def sample_func():
    rprint("[red bold]Hello[/red bold] [yellow]World[yello]")



if __name__ == "__main__":
    app()  
    
    