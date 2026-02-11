# main.py

import argparse
from attention import list_papers, open_paper

def main():
    parser = argparse.ArgumentParser(
        prog="attention",
        description="CLI to list and open high-impact AI research papers.",
    )

    parser.add_argument(
        "-n", "--name",
        type=str,
        help="Name of the paper to open (e.g. 'Attention Is All You Need')"
    )

    parser.add_argument(
        "command",
        nargs="?",
        choices=["list"],
        help="Commands: `list` to list all papers"
    )

    args = parser.parse_args()

    if args.command == "list":
        list_papers()
    elif args.name:
        open_paper(args.name)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
