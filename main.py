
from utils import generate_plot, chart_json, hist_json
from argparse import ArgumentParser, RawTextHelpFormatter


if __name__ == '__main__':

    parser = ArgumentParser(formatter_class=RawTextHelpFormatter)

    parser.add_argument("file", metavar="file", type=str, help="Google takeout JSON file.")
    parser.add_argument("-s", "--size", dest="size", type=int, required=False,
    help="Number of top sites to be displayed.", default=20)
    parser.add_argument("-d", "--days", dest="days", type=int, required=False,
    help="Number of x last days of data to be displayed.", default=60)

    args = parser.parse_args()

    print("(1/2): Processing data")
    data = []
    data.append(chart_json(args.file, args.days))
    data.append(hist_json(args.file, args.days))

    print("(2/2): Generating graph")
    generate_plot(data, args.size, args.days)
