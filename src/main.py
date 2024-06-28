import time
import typer
import subprocess
from PyInquirer import prompt, print_json, Separator
from rich import print as rprint
from art import *
from rich.console import Console
from rich.panel import Panel
from Weather import weatherRun
from Hurricanes import hurricaneRun
from ChatGPT import chatRun

exitApp = False


app = typer.Typer()
console = Console()

mih = text2art("\n\n\n\nWEATHER.io", font="alligator3")
console.print(mih, style="blue")
rprint(Panel.fit("[bold yellow]Creator: Nigel Smith                             ", style="bold yellow"))


def Menu(city):
    if city.lower() == "back":                     ### Line 21 when executed, goes back to the main menu
        app()


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


    city = ""
    if username['username'].__eq__("Weather"):
        print("Enter city: ", end='')
        city = input()
        if city == "":
            return print(f"{ValueError} Somethings wrong... try again"), time.sleep(3), app()

        Menu(city)                                                      #Back to the main menu
        print(city)
        weatherRun(city)
    
    if username['username'].__eq__("Hurricanes"):
        hurricaneRun()

    if username['username'].__eq__("Ask questions >>>"):
        chatRun()

    if username['username'].__eq__("Exit"):
        exit()

        

rprint("[yellow]=============================================[yello]")
rprint("[green bold]Enter folder name :[green bold]")
    #folder_name = input()


    #subprocess.run(f"mkdir {folder_name}_created_by_{username['username']}", shell=True)

@app.command("test")
def sample_func():
    rprint("[red bold]Hello[/red bold] [yellow]World[yello]")


#while exitApp != True:
if __name__ == "__main__":
    app()
    
    