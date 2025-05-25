from rich.console import Console
from rich.panel import Panel
from rich.box import SQUARE
from rich.live import Live

import time

console = Console()


def scroll_text(sentence, width=50, delay=0.03, box=SQUARE):
    output = ""

    with Live(Panel(output, width=width, box=box), refresh_per_second=60) as live:
        for character in sentence:
            output += character
            live.update(Panel(output, width=width, box=box))
            time.sleep(delay)


# Example usage
scroll_text("Did you know that grass is green?")
input()