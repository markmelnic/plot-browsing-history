
import sys
from processing import refine, generate_graph
from argparse import ArgumentParser, RawTextHelpFormatter


if __name__ == '__main__':

    parser = ArgumentParser(formatter_class=RawTextHelpFormatter)

    parser.add_argument("file", metavar="file", type=str, help="JSON file.")
    parser.add_argument("-s", "--size", dest="size", type=int, required=False,
    help="Number of top sites to be displayed.", default=20)
    parser.add_argument("-d", "--days", dest="days", type=int, required=False,
    help="Number of x last days of data to be displayed.", default=365)

    args = parser.parse_args()

    print(args.days)
    print("(1/2): Processing data")
    refined_data = refine(args.file, args.days)

    print("(2/2): Generating graph")
    generate_graph(refined_data, args.size)
