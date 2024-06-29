import time
import typer
import subprocess
from PyInquirer import prompt, print_json, Separator
from rich import print as rprint
from art import *
from rich.console import Console
from rich.panel import Panel
from Weather import *
from Hurricanes import hurricaneRun

exitApp = False


app = typer.Typer()
console = Console()

mih = text2art("\n\n\n\nWEATHER.io", font="alligator3")


def Menu(city):
    if city.lower() == "menu":                     ### Line 21 when executed, checks to see if user typed 'back'. If true then the app goes back to the main menu
        app()

#hi = rprint("[green bold]Select any one operation:[green bold]")

@app.command("tools")
def sample_func():
    console.print(mih, style="blue")
    rprint(Panel.fit("[bold yellow]Creator: Nigel Smith                             ", style="bold yellow"))
    rprint("[green bold]Select any one operation:[green bold]")
    dots = rprint("[yellow]====================================================[yello]")

    module_list_question = questions = [
        {
            'type': 'list',
            'name': 'username',
            'message': '            ',
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

    #This section evalutes the option that the user chose

    city = ""
    if username['username'].__eq__("Weather"):
        rprint("[yellow bold]Enter city[yellow bold]" + "[red](Type \"MENU\" to return home[red]): ", end='')
        city = input()
        if city == "":
            return print(f"{ValueError} Somethings wrong... try again"), time.sleep(3), app()
        url_Func(city)

        #Back to the main menu
        Menu(city)
        
        ##weatherRun()
    
    if username['username'].__eq__("Hurricanes"):
        hurricaneRun()

    if username['username'].__eq__("Ask questions >>>"):
        chatRun()

    if username['username'].__eq__("Exit"):
        exit()

        

#rprint("[green bold]Enter folder name :[green bold]")
    #folder_name = input()


    #subprocess.run(f"mkdir {folder_name}_created_by_{username['username']}", shell=True)

@app.command("test")
def sample_func():
    rprint("[red bold]Hello[/red bold] [yellow]World[yello]")


#while exitApp != True:
if __name__ == "__main__":
    app()
    
    