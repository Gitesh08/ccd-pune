#!/usr/bin/env python3
import argparse
import re
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init(autoreset=True)

def display_welcome():
    """Display an interactive welcome message."""
    print(Fore.CYAN + "=" * 50)
    print(Fore.YELLOW + "🌩️ Welcome to GCCD Pune 2025! 🌩️")
    print(Fore.GREEN + "Join the cloud community in Pune for an epic event!")
    print(Fore.MAGENTA + "Try these commands:")
    print(Fore.MAGENTA + "  - `gccd-pune --date` for a hint")
    print(Fore.MAGENTA + "  - `gccd-pune DD-MM-YY` to guess (e.g., 12-06-25)")
    print(Fore.MAGENTA + "  - `gccd-pune --venue` for venue info")
    print(Fore.MAGENTA + "  - `gccd-pune --help` for more details")
    print(Fore.CYAN + "=" * 50)

def validate_date_format(date_str):
    """Validate DD-MM-YY format."""
    pattern = r"^\d{2}-\d{2}-\d{2}$"
    return bool(re.match(pattern, date_str))

def main():
    parser = argparse.ArgumentParser(
        description="Google Cloud Community Day Pune 2025 Interactive CLI",
        epilog="Commands: `gccd-pune --date` for a hint, `gccd-pune DD-MM-YY` to guess the date, `gccd-pune --venue` for venue info."
    )
    parser.add_argument("--date", action="store_true", help="Get a hint for the event")
    parser.add_argument("--venue", action="store_true", help="Get venue information")
    parser.add_argument("guess", nargs="?", help="Guess the date in DD-MM-YY format (e.g., 12-06-25)")
    args = parser.parse_args()

    # Display welcome message on every command
    display_welcome()

    correct_date = "12-07-25"
    hints = [
        f"{Fore.YELLOW}Hint: Clouds part in Pune, day is a dozen!{Style.RESET_ALL}",
        f"{Fore.YELLOW}Hint: The month is a prime number!{Style.RESET_ALL}",
        f"{Fore.GREEN}Final reveal: The date is 12 July 2025!{Style.RESET_ALL}"
    ]

    # Track attempts in a file
    try:
        with open(".gccd_pune_guesses.txt", "r") as f:
            attempts = int(f.read())
    except FileNotFoundError:
        attempts = 0

    if args.date:
        print(hints[0])
        print(f"{Fore.CYAN}Guess the date with: `gccd-pune DD-MM-YY` (e.g., `gccd-pune 12-06-25`)")
    elif args.venue:
        print(f"{Fore.MAGENTA}Thoda sabar karo")
    elif args.guess:
        if not validate_date_format(args.guess):
            print(f"{Fore.RED}Invalid format! Use DD-MM-YY (e.g., 12-06-25)")
            return
        if args.guess == correct_date:
            print(f"{Fore.GREEN}Correct! Google Cloud Community Day Pune 2025 is on 12 July 2025!")
            with open(".gccd_pune_guesses.txt", "w") as f:
                f.write("0")  # Reset attempts
        else:
            attempts += 1
            with open(".gccd_pune_guesses.txt", "w") as f:
                f.write(str(attempts))
            if attempts == 1:
                print(f"{Fore.RED}Wrong guess! {hints[1]}")
                print(f"{Fore.CYAN}Try again with: `gccd-pune DD-MM-YY` (e.g., `gccd-pune 12-06-25`)")
            else:
                print(hints[2])
                with open(".gccd_pune_guesses.txt", "w") as f:
                    f.write("0")  # Reset attempts
    else:
        print(f"{Fore.CYAN}Get started with `gccd-pune --date`, `gccd-pune DD-MM-YY`, or `gccd-pune --venue`.")

if __name__ == "__main__":
    main()
