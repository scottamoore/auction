"""
Description.

Example
-------
asdf

Attributes
----------
asdf

Todo
----
asdf

"""
#!/usr/bin/python3

#import math
#import random
import sys

#import strategy as strat
import etzion as etz
import experiment_control as expctl
#import consumer as con
#import generate_consumers as gcon
import market as mkt
import utilities as util

#import timeit


def main():
    """
    Summary line.

    Extended description of function.

    Parameters
    ----------
    the_choice: Selected response of the user for this question

    Returns
    -------
    The appropriate integer for that selection.

    """
    assump = util.GLOBAL
    if len(sys.argv) == 1:
        expctl.control_experiment(assump)
    elif len(sys.argv) > 1:
        print("Command line arguments are not needed.")
    else:
        print("Is this even possible?")

if __name__ == "__main__":
    main()
