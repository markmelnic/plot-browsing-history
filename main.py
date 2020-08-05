
import sys
from chart_utils import chart_json, generate_chart
from histogram_utils import hist_json, generate_hist
from argparse import ArgumentParser, RawTextHelpFormatter


if __name__ == '__main__':
    
    parser = ArgumentParser(formatter_class=RawTextHelpFormatter)

    parser.add_argument("file", metavar="file", type=str, help="JSON file.")
    parser.add_argument("type", metavar="type", type=str, help="Output type.")
    parser.add_argument("-s", "--size", dest="size", type=int, required=False,
    help="Number of top sites to be displayed.", default=20)
    parser.add_argument("-d", "--days", dest="days", type=int, required=False,
    help="Number of x last days of data to be displayed.", default=365)

    args = parser.parse_args()

    if args.type.lower() == 'chart':
        print("(1/2): Processing data")
        data = chart_json(args.file, args.days)

        print("(2/2): Generating graph")
        generate_chart(data, args.size, args.days)

    elif args.type.lower() == 'hist':
        print("(1/2): Processing data")
        
        print("(2/2): Generating histogram")
