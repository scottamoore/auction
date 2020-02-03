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
from typing import List  # , TextIO, Optional, Set, Union, Dict, Tuple
import collections as coll
import math
import random

auction_settings = coll.namedtuple('auction_settings', ['q', 't', 'p'])
environment_settings = coll.namedtuple('environment_settings', ['lmbda', 'w'])
assumptions = coll.namedtuple('assumptions', ['R', 'h', 'min_val', 'max_val'])

GLOBAL = assumptions(R=0, h=1, min_val=0, max_val=100)

def get_environment_settings():
    """
    Summary line.

    Extended description of function.

    Returns
    -------
    The appropriate integer for that selection.

    """
    arrival_rate = [1, 5, 10, 20, 30, 40]
    waiting_cost = [0.5, 1, 2, 4, 1000]
    ar_counter = 0
    while ar_counter < len(arrival_rate):
        w_counter = 0
        while w_counter < len(waiting_cost):
            yield environment_settings(lmbda=arrival_rate[ar_counter],
                                       w=waiting_cost[w_counter])
            w_counter += 1
        ar_counter += 1

def get_auction_settings():
    """
    Generates the auction settings namedtuple that will be tested during
    a specific run of an auction.

    Extended description of function.

    Returns
    -------
    The appropriate integer for that selection.

    """
    quantity: List[int] = [1, 2, 3, 5, 7, 10]
    auction_length: List[float] = [1, 2, 4, 6, 8]
    posted_price: List[float] = [40, 43, 47, 50]
    #quantity: List[int] = [1, 2, 3, 5, 7, 10, 12, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100]
    #auction_length: List[float] = [1, 2, 4, 6, 8, 10, 12, 15, 18, 24, 30, 36, 42, 48, 54, 60, 72,
    #                              84, 96, 108, 120, 132, 144, 154, 160, 168]
    #posted_price: List[float] = [40, 43, 45, 47, 50, 53, 55, 57, 60, 63, 65, 67, 70, 73, 101]
    q_counter = 0
    while q_counter < len(quantity):
        t_counter = 0
        while t_counter < len(auction_length):
            p_counter = 0
            while p_counter < len(posted_price):
                yield auction_settings(q=quantity[q_counter],
                                       t=auction_length[t_counter],
                                       p=posted_price[p_counter])
                p_counter += 1
            t_counter += 1
        q_counter += 1

def random_list(the_min: int,
                the_max: int,
                the_len: int,
                dist_type: str = "uniform"):
    """
    Summary line.

    Extended description of function.

    Parameters
    ----------
    the_min: description
    the_max: description
    the_len: description
    dist_type: description

    Returns
    -------
    The appropriate integer for that selection.

    """
    if dist_type == "uniform":
        retval = [random.uniform(the_min, the_max) for _ in range(the_len)]
    elif dist_type == "triangular":
        retval = [random.triangular(the_min, the_max) for _ in range(the_len)]
    return retval

def get_all_arrival_times(lmbda: float,
                          max_time: int = 168) -> List[float]:
    """
    Summary line.

    Extended description of function.

    Parameters
    ----------
    lmbda: description
    max_time: description

    Returns
    -------
    The appropriate integer for that selection.

    """
    _num_arrivals: int = 0
    _arrival_time: float = 0
    arrival_times: List[float] = []
    continue_process: bool = True

    while continue_process:
        p: float = random.random()
        _inter_arrival_time: float = -math.log(1.0 - p)/lmbda
        _arrival_time += _inter_arrival_time
        if _arrival_time < max_time:
            arrival_times.append(_arrival_time)
            _num_arrivals += 1
        else:
            continue_process = False
    return arrival_times

def get_number_of_auctions_to_run(q: int,
                                  t: int,
                                  lmbda: int) -> int:
    """
    Summary line.

    Extended description of function.

    Parameters
    ----------
    q: description
    t: description
    lmbda: description

    Returns
    -------
    The appropriate integer for that selection.

    """
    retval: int = 0
    if t <= 2:
        retval = 2400
    elif t <= 8:
        retval = 1600
    elif t <= 18:
        retval = 1200
    elif t <= 60:
        retval = 800
    elif t <= 108:
        retval = 600
    elif t <= 144:
        retval = 500
    else:
        retval = 400
    if (q == 1) or (lmbda == 1):
        retval *= 2
    return retval
