from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Displays "Hello world" on the screen',
    # type=str, # Argument type
    metavar='STRING',
    # default='Hello world', # Default value
    required=False,
    action='append',  # Accepts the argument more than once
    # nargs='+', # Accepts more than one value
)
parser.add_argument(
    '-v', '--verbose',
    help='Displays logs',
    action='store_true'
)
args = parser.parse_args()

if args.basic is None:
    print('You did not provide the value for b.')
    print(args.basic)
else:
    print('The value of basic:', args.basic)

print(args.verbose)


