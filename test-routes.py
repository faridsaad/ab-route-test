#!/usr/bin/env python
import string
import argparse
from prettytable import PrettyTable
import requests


def main(endpoint, req_attempts):

    results = dict()
    total_count = 0
    table = PrettyTable(["Version", "Count", "Percent"])

    for counter in range(req_attempts):
        total_count += 1
        request = requests.get(endpoint)
        result = request.headers['X-Hostname']
        if result in results:
            results[result] += 1
        else:
            results[result] = 1

    for result in results.keys():
        table.add_row([result, results[result], (results[result]/float(total_count)*100)])

    print table

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Request from URL and calculate result counts")
    parser.add_argument("url", help="URL to request")
    parser.add_argument("count", type=int,
                        help="number of requests to perform")
    args = parser.parse_args()

    main(args.url, args.count)
