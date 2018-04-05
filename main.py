#!/usr/bin/env python

from os import listdir
from os.path import isfile,join
from shutil import move
import re
import argparse

def months_regex():
    return '(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)'

def convert_month(month):
    if month == 'Jan': return 1
    elif month == 'Feb': return 2
    elif month == 'Mar': return 3
    elif month == 'Apr': return 4
    elif month == 'May': return 5
    elif month == 'Jun': return 6
    elif month == 'Jul': return 7
    elif month == 'Aug': return 8
    elif month == 'Sep': return 9
    elif month == 'Oct': return 10
    elif month == 'Nov': return 11
    elif month == 'Dec': return 12
    else: raise

def convert_filename(groups):
    groups['hour']

    if groups['period'] == 'PM':
        groups['hour'] += 12

    filename = '{0:02}'.format(groups['month'])
    filename += '-'
    filename += '{0:02}'.format(groups['day'])
    filename += '_'
    filename += '{0:02}'.format(groups['hour'])
    filename += '-'
    filename += '{0:02}'.format(groups['minute'])
    filename += '-'
    filename += '{0:02}'.format(groups['second'])
    filename += '_'
    filename += '{0:02}'.format(groups['copy'])
    filename += '.jpg'

    return filename

def move_file(src, dest, live):
    print 'Moving {0} to {1}'.format(src, dest)
    if live:
        move(src, dest)

def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--live', dest='live', action='store_true',
                        default=False, help='Run in live mode')
    parser.add_argument('--directory', dest='directory', required=True,
                        help='Run in live mode')

    return parser.parse_args()

def try_rename_dupe_file(directory, f, live):
    dupe_regex_pattern = '^Photo {0} ([0-9]+), ([0-9]+) ([0-9]+) ([0-9]+) (AM|PM)( \([0-9]\)).jpg$'.format(months_regex())
    m = re.search(dupe_regex_pattern, f)
    if m is None:
        return False

    groups = {
        'month': convert_month(m.group(1)),
        'day': int(m.group(2)),
        'hour': int(m.group(3)),
        'minute': int(m.group(4)),
        'second': int(m.group(5)),
        'period': m.group(6),
        'copy': int(m.group(7).replace(' (', '').replace(')', ''))
    }

    filename = convert_filename(groups)
    move_file(join(directory, f), join(directory, filename), live)
    return True


def try_rename_file(directory, f, live):
    regex_pattern = '^Photo {0} ([0-9]+), ([0-9]+) ([0-9]+) ([0-9]+) (AM|PM).jpg$'.format(months_regex())
    m = re.search(regex_pattern, f)
    if m is None:
        return False

    groups = {
        'month': convert_month(m.group(1)),
        'day': int(m.group(2)),
        'hour': int(m.group(3)),
        'minute': int(m.group(4)),
        'second': int(m.group(5)),
        'period': m.group(6),
        'copy': 0
    }

    filename = convert_filename(groups)
    move_file(join(directory, f), join(directory, filename), live)
    return True


def main():
    args = parse_args()

    if args.live:
        print "Running in live mode"

    files = [f for f in listdir(args.directory) if isfile(join(args.directory, f))]

    for f in files:
        if try_rename_file(args.directory, f, args.live):
            continue

        if try_rename_dupe_file(args.directory, f, args.live):
            continue

if __name__ == "__main__":
    main()
