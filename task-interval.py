#!/usr/bin/env python3

import datetime
import tasklib
import sys

tag = 'taskinterval'
tw = tasklib.TaskWarrior()


def get_intervals():
    # Modified Paul Pimsleur's intervals for language learning
    days = (2, 6, 25, 90)
    for d in days:
        yield datetime.timedelta(d)


def add_tasks(desc):
    """ Add task multiple times with different intervals. """
    today = datetime.datetime.today()
    for interval in get_intervals():
        due = today + interval
        task = tasklib.Task(tw, description=desc, due=due, tags=[tag])
        task.save()


def main():
    if len(sys.argv) < 2:
        print('Usage: {} text...'.format(sys.argv[0]))
        sys.exit(1)

    desc = ' '.join(sys.argv[1:])
    add_tasks(desc)
    print('Created tasks.')


if __name__ == '__main__':
    main()
