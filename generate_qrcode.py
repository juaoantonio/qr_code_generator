import qrcode
from qrcode.constants import ERROR_CORRECT_H
import argparse
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

console = Console()

def generate_qrcode(content, output_file="qrcode.png"):
    """
    Generates a QR Code with the specified content and saves it as a PNG file.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(content)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)  # type: ignore
    console.print(f"✅ [bold green]QR Code saved as '{output_file}'[/]")

def options_menu():
    table = Table(title="Options Menu")
    table.add_column("Number", justify="center", style="cyan", no_wrap=True)
    table.add_column("QR Code Type", style="magenta")

    table.add_row("1", "Text or URL")
    table.add_row("2", "Wi-Fi")

    console.print(table)

    while True:
        choice = Prompt.ask("[bold blue]Select an option[/]", choices=["1", "2"])
        return choice

def generate_text_qrcode():
    content = Prompt.ask("Enter the text or URL to encode")
    output_file = Prompt.ask(
        "Output file name",
        default="qrcode.png"
    )
    generate_qrcode(content, output_file)

def generate_wifi_qrcode():
    ssid = Prompt.ask("📶 Wi-Fi Network Name (SSID)")
    password = Prompt.ask("🔑 Wi-Fi Password (leave empty for open network)", default="")
    security = Prompt.ask(
        "🔒 Security Type",
        choices=["WPA", "WEP", "nopass"],
        default="WPA"
    )

    if security == "nopass":
        password = ""

    wifi_content = f"WIFI:T:{security};S:{ssid};P:{password};;"

    output_file = Prompt.ask(
        "Output file name",
        default="wifi_qrcode.png"
    )
    generate_qrcode(wifi_content, output_file)

def main():
    console.print("[bold yellow]🚀 Interactive QR Code Generator[/]\n")

    option = options_menu()

    if option == "1":
        generate_text_qrcode()
    elif option == "2":
        generate_wifi_qrcode()
    else:
        console.print("[bold red]Invalid option.[/]")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="QR Code Generator")
    parser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help="Run in interactive mode with menu"
    )
    args = parser.parse_args()

    if args.interactive:
        main()
    else:
        console.print("[bold green]To use interactive mode, run:[/]")
        console.print("  python qrcode_generator.py -i")
