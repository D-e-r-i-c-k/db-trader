from cli import Parser


if __name__ == "__main__":
    parser = Parser()
    parser.__init__()
    print(parser.args)
    print(parser.get_command())