"""CLI menu for RPL Toolkit."""


def run_menu() -> None:
    """Run the main interactive menu."""
    while True:
        print("\n╔══════════════════════════════════╗")
        print("║          RPL TOOLKIT             ║")
        print("║     Student Developer Tools      ║")
        print("╚══════════════════════════════════╝")
        print("\n[1] Calculator")
        print("[2] Converter")
        print("[3] Encoder / Decoder")
        print("[4] JSON Formatter")
        print("[5] UUID Generator")
        print("[6] Timestamp")
        print("[7] QR Generator")
        print("[8] File Utilities")
        print("[0] Exit")

        choice = input("\nSelect tool > ").strip()

        if choice == "0":
            print("Goodbye! 👋")
            break
        print("This tool is not implemented yet.")
