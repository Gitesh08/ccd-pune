#!/usr/bin/env python3
import argparse
import re
import os
from pathlib import Path
from colorama import init, Fore, Style

# Version for setup.py
__version__ = "1.0.1"

# Initialize colorama for cross-platform colored output
init(autoreset=True)

def display_welcome():
    """Display an interactive welcome message."""
    print(Fore.CYAN + "=" * 50)
    print(Fore.YELLOW + "Welcome to GCCD Pune 2025!")
    print(Fore.GREEN + "Join the cloud community in Pune for an epic event!")
    print(Fore.MAGENTA + "Try these commands:")
    print(Fore.MAGENTA + "  - `gccdpune --date` for a hint")
    print(Fore.MAGENTA + "  - `gccdpune DD-MM-YY` to guess (e.g., 12-06-25)")
    print(Fore.MAGENTA + "  - `gccdpune --venue` for venue info")
    print(Fore.MAGENTA + "  - `gccdpune --help` for more details")
    print(Fore.CYAN + "=" * 50)

def should_show_welcome():
    """Check if welcome message should be shown."""
    # Explicitly use USERPROFILE on Windows
    home_dir = Path(os.environ.get("USERPROFILE", Path.home()))
    welcome_flag = home_dir / ".gccdpune_welcome"
    print(f"{Fore.CYAN}Checking welcome flag at: {welcome_flag}")  # Debug
    try:
        if not welcome_flag.exists():
            welcome_flag.touch()  # Create flag file
            print(f"{Fore.CYAN}Created welcome flag: {welcome_flag}")  # Debug
            return True
        print(f"{Fore.CYAN}Welcome flag exists, skipping welcome message")  # Debug
        return False
    except Exception as e:
        print(f"{Fore.RED}Error handling welcome flag: {e}")
        return True  # Show welcome if file access fails

def validate_date_format(date_str):
    """Validate DD-MM-YY format."""
    pattern = r"^\d{2}-\d{2}-\d{2}$"
    return bool(re.match(pattern, date_str))

def main():
    parser = argparse.ArgumentParser(
        description="Google Cloud Community Day Pune 2025 Interactive CLI",
        epilog="Commands: `gccdpune --date` for a hint, `gccdpune DD-MM-YY` to guess the date, `gccdpune --venue` for venue info."
    )
    parser.add_argument("--date", action="store_true", help="Get a hint for the event")
    parser.add_argument("--venue", action="store_true", help="Get venue information")
    parser.add_argument("guess", nargs="?", help="Guess the date in DD-MM-YY format (e.g., 12-06-25)")
    args = parser.parse_args()

    # Show welcome message only on first run
    if should_show_welcome():
        display_welcome()

    correct_date = "12-07-25"
    hints = [
        f"{Fore.YELLOW}Hint: Clouds part in Pune, day is a dozen!{Style.RESET_ALL}",
        f"{Fore.YELLOW}Hint: The month is a prime number!{Style.RESET_ALL}",
        f"{Fore.GREEN}Final reveal: The date is 12 July 2025!{Style.RESET_ALL}"
    ]

    # Track attempts in a file
    home_dir = Path(os.environ.get("USERPROFILE", Path.home()))
    guess_file = home_dir / ".gccdpune_guesses.txt"
    try:
        with open(guess_file, "r") as f:
            attempts = int(f.read())
    except (FileNotFoundError, ValueError):
        attempts = 0

    if args.date:
        print(hints[0])
        print(f"{Fore.CYAN}Guess the date with: `gccdpune DD-MM-YY` (e.g., `gccdpune 12-06-25`)")
    elif args.venue:
        print(f"{Fore.MAGENTA}Thoda sabar karo")
    elif args.guess:
        if not validate_date_format(args.guess):
            print(f"{Fore.RED}Invalid format! Use DD-MM-YY (e.g., 12-06-25)")
            return
        if args.guess == correct_date:
            print(f"{Fore.GREEN}Correct! Google Cloud Community Day Pune 2025 is on 12 July 2025!")
            with open(guess_file, "w") as f:
                f.write("0")  # Reset attempts
        else:
            attempts += 1
            with open(guess_file, "w") as f:
                f.write(str(attempts))
            if attempts == 1:
                print(f"{Fore.RED}Wrong guess! {hints[1]}")
                print(f"{Fore.CYAN}Try again with: `gccdpune DD-MM-YY` (e.g., `gccdpune 12-06-25`)")
            else:
                print(hints[2])
                with open(guess_file, "w") as f:
                    f.write("0")  # Reset attempts
    else:
        print(f"{Fore.CYAN}Get started with `gccdpune --date`, `gccdpune DD-MM-YY`, or `gccdpune --venue`.")

if __name__ == "__main__":
    main()
