"""Script to generate a pie chart graph from a Pylint report."""

import argparse
import re
from collections import Counter

import matplotlib.pyplot as plt


def process(line):
    """Process a line from the pylint report, returning just the code & message."""
    match = re.match(r"^.*.*:\d+: \[(?P<code>.*)\((?P<message>.*)\),", line)
    if match:
        return f"{match.group('code')} - {match.group('message')}"


def get_data(filename):
    """Parse the warning data from a pylint report."""
    with open(filename, "r") as fobj:
        tokens = [token for token in (process(line) for line in fobj) if token]

    counts = Counter(tokens)
    return counts.most_common(10)


def generate_plot(data, outfile):
    """Generate the pie chart & saves to outfile."""
    # Data to plot
    labels = [label[0] for label in data]
    sizes = [label[1] for label in data]
    colors = [
        "#ff6666",
        "#ffcc99",
        "#99ff99",
        "#66b3ff",
        "#c2c2f0",
        "#ffb3e6",
        "#B2912F",
        "#5DA5DA",
        "#F17CB0",
        "#4D4D4D",
    ]
    # explode 1st slice
    explode = [0.1] + ([0] * (len(data) - 1))

    plt.pie(
        sizes,
        explode=explode,
        labels=sizes,
        autopct="%1.1f%%",
        shadow=True,
        colors=colors,
        wedgeprops={"linewidth": 1, "edgecolor": "black"},
    )

    plt.legend(labels, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    plt.title("Pylint Violations by Count")
    plt.axis("equal")
    plt.savefig(outfile, bbox_inches="tight")


def parse_args():
    """Parse out the command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n",
        action="store",
        dest="slices",
        default=5,
        help="Number of slices",
        type=int,
    )
    parser.add_argument(
        "-f",
        action="store",
        dest="filename",
        default="/tmp/pylint-report.txt",
        help="Name of pylint report",
    )
    parser.add_argument(
        "-o",
        action="store",
        dest="outfilename",
        default="/tmp/pylint.png",
        help="Name of output file",
    )
    return parser.parse_args()


def main():
    """Enter main entry point."""
    args = parse_args()
    data = get_data(args.filename)[: args.slices]

    generate_plot(data, args.outfilename)


if __name__ == "__main__":
    main()
