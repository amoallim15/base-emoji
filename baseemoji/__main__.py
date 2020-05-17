import argparse
import sys

from baseemoji import encode, decode


def main():
    """
    Base Emoji encode or decode FILE, or standard input,
    to standard output.
    """
    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument(
        "--version", "-v",
        action="version",
        version='%(prog)s {version}'.format(version=__version__)
    )
    parser.add_argument(
        "--input-file", "-i",
        type=argparse.FileType("r"),
        default=sys.stdin,
        help="Input file name to be encoded."
    )
    parser.add_argument(
        "text",
        nargs="?",
        type=str,
        help="Input string to be encoded."
    )
    parser.add_argument(
        "--output-file", "-o",
        type=argparse.FileType("w"),
        help="output file name.",
        default=sys.stdout
    )
    parser.add_argument("-d", "--decode", action="store_true", help="decode data.")

    args = parser.parse_args()
    func = {True: decode, False: encode}[args.decode]

    try:
        data = args.text or args.input_file.read()
        result = func(data)
        args.output_file.write(result)
    except Exception as e:
        sys.exit(e)


if __name__ == "__main__":
    main()
