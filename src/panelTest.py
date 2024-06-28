from art import *
from rich.console import Console
from rich.panel import Panel
from rich.spinner import Spinner
from rich import print
from rich.layout import Layout


layout = Layout()
console = Console()
spinner = Spinner('bouncingBall')

mih = text2art("\n\n\n\nWEATHER.io", font="alligator3")
console.print(mih, style="blue")
print(Panel.fit("[bold yellow]Creator: Nigel Smith                             ", style="bold yellow"))


layout.split_column(
    Layout(name="upper"),
    Layout(name="lower")
)

layout["upper"].split_row(
    Layout(name="left"),
    Layout(name="center"),
    Layout(name="right"),
)

layout["lower"].split_row(
    Layout(name="left"),
    Layout(name="right"),
)
print(layout)