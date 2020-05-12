import argparse


from baseemoji import encode, decode


def main():
    """Base Emoji encode or decode FILE, or standard input, to standard output."""

    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument(
        "data", metavar="DATA", nargs="?", default="-", help="data to be encoded."
    )
    parser.add_argument("-d", "--decode", action="store_true", help="decode data.")

    args = parser.parse_args()
    func = {True: decode, False: encode}[args.decode]

    try:
        result = func(args.data)
    except Exception as e:
        sys.exit(e)

    print(result)


if __name__ == "__main__":
    main()
