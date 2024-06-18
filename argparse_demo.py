#
# https://docs.python.org/3/library/argparse.html
#

import argparse

APP_NAME = "ArgParse Demo app"
APP_VER = "v1.0"


# args
parser = argparse.ArgumentParser(
    prog=APP_NAME,
    description=APP_NAME + " " + APP_VER,
    epilog='End of help section')
parser.add_argument('filename')                                # positional argument
parser.add_argument('-c', '--count', nargs='?', type=int, required=True)      # option that takes a value
parser.add_argument('-v', '--verbose',
    action='store_true')                                       # on/off flag
args = parser.parse_args()



### ************** MAIN ********************
print( APP_NAME )
if __name__ == '__main__':
    if args.filename:
        print( f"Args: {args.filename}" )
    if args.count:
        print( f"Count: {args.count}" )
    else:
        print("------------------------ HELP ---------------------------")
        parser.print_help()
