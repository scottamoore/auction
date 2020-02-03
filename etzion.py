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

import utilities as util


def expected_profit(auct,
                    env,
                    lower_val: float,
                    upper_val: float,
                    lowest_winning_bid: float) -> float:
    """
    Summary line.

    Extended description of function.

    Parameters
    ----------
    auct: description
    env: description
    lower_val: description
    upper_val: description
    lowest_winning_bid: description

    Returns
    -------
    The appropriate integer for that selection.

    """
    (q, t, p) = auct
    (lmbda, w) = env
    prob_above = (upper_val - p)/(upper_val - lower_val)
    prob_below = (p - lower_val)/(upper_val - lower_val)
    if (p > lower_val) and (p < upper_val):
        s = calculate_threshold_value(q, t, p, lmbda, w,
                                      lower_val, upper_val, lowest_winning_bid)
        lmbda1 = lmbda * t * prob_below
        lmbda2 = lmbda * min(t, s) * prob_above
        prob1 = [poisson(lmbda1, x) for x in range(0, q+1)]
        prob2 = [poisson(lmbda2, x) for x in range(0, q+1)]
        sum1 = sum([math.pow(lmbda2, x) * (q - x + 1.0)/math.factorial(x) for x in range(0, q+1)])
        sum2 = sum([(lower_val + (p - lower_val) * (y - (q-x))/(y+1)) * prob1[y] * prob2[x]
                    for x in range(0, q+1) for y in range(0, q - x + 1)])
        sum3 = sum([prob2[x] for x in range(0, q+1)])
        sum4 = lower_val
        f = (q * (lower_val + (p - lower_val) *
                  (lmbda1 - math.exp(-lmbda2) *
                   (1.0 - math.exp(-lmbda1)) *
                   sum1)/lmbda1 - sum2) +
             sum4 +
             p * (lmbda * t * prob_above - lmbda2) +
             p * (lmbda2 - q) * (1 - sum3) +
             p * lmbda2 * prob2[q])
    elif p == upper_val:
        tempx = lmbda * t
        prob3 = [poisson(tempx, x) for x in range(0, q+1)]
        sum6 = sum([(lower_val + (n-q)/(n + 1)) * prob3[n+1] for n in range(0, q+1)])
        sum5 = sum([n * prob3[n+1] for n in range(0, q+1)])
        sum5 = sum5 * lower_val
        f = (q * (lower_val +
                  (upper_val - lower_val) *
                  (1 - ((q + 1) * math.exp(-tempx) * (math.exp(tempx) - 1.0))/tempx) - sum6) + sum5)
    else: # p == lower_val
        f = lmbda * t * lower_val
    return f

def test_function(w: float,
                  s: float,
                  beta: float,
                  alpha: float,
                  p: float,
                  b: float,
                  U: float,
                  q: int,
                  high_val_consumers_up: float,
                  L: float,
                  high_val_consumers_down: float) -> bool:
    """
    Summary line.

    Extended description of function.

    Parameters
    ----------
    w: description
    s: description
    beta: description
    alpha: description
    p: description
    b: description
    U: description
    q: description
    high_val_consumers_up: description
    L: description
    high_val_consumers_down: description

    Returns
    -------
    The appropriate integer for that selection.

    """
    return (((w * s) + 0.0000000000001) <
            (beta * alpha *
             (p - max(b,
                      min(p,
                          b + (p - b) *
                          (U - (q - high_val_consumers_up - 1))/(U + 1)))) +
             (beta * (1 - alpha) *
              (p - max(b,
                       min(p,
                           b + (p - b) * (U - (q - high_val_consumers_down - 1))/(U + 1))))) +
             ((1 - beta) *
              (1 - alpha) * (p - max(b,
                                     min(p,
                                         b + (p - b) *
                                         (L - (q - high_val_consumers_down - 1))/(L + 1))))) +
             ((1 - beta) *
              alpha * (p - max(b, min(p,
                                      b + (p - b) *
                                      (L - (q - high_val_consumers_up - 1))/(L + 1)))))))

def calculate_threshold_value(q: int,
                              t: int,
                              p: int,
                              lmbda: int,
                              w: float,
                              lower_val: float,
                              upper_val: float,
                              lowest_winning_bid: float) -> float:
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
    s = 0.0
    prob_above = (upper_val - p)/(upper_val - lower_val)
    prob_below = (p - lowest_winning_bid)/(upper_val - lower_val)
    t_estimate = lmbda * t * prob_below
    beta = fractional_part(t_estimate)
    lower_bound = math.floor(t_estimate)
    upper_bound = calculate_upper(beta, t_estimate)
    temp_num = (p - lowest_winning_bid -
                beta * (p - lowest_winning_bid) * (upper_bound - q + 1.0)/(upper_bound + 1.0) -
                (1 - beta) * (p - lowest_winning_bid) * (lower_bound - q + 1.0)/(lower_bound + 1.0))
    temp_denom = (w +
                  beta * (p - lowest_winning_bid) * lmbda * prob_above/(upper_bound + 1.0) +
                  (1.0 - beta) * (p - lowest_winning_bid) * lmbda * prob_above/(lower_bound + 1.0))
    s = min(temp_num/temp_denom, t)
    t_estimate = lmbda * s * prob_above
    alpha = fractional_part(t_estimate)
    if alpha == 0.0:
        high_val_consumers_up = t_estimate
        high_val_consumers_down = t_estimate
    else:
        high_val_consumers_up = math.ceil(t_estimate)
        high_val_consumers_down = math.floor(t_estimate)
    if (high_val_consumers_up >= q) or ((1.0 + high_val_consumers_down + lower_bound) <= q):
        s = calculate_s(w, 0.0, beta, 0.0, p, lowest_winning_bid, upper_bound,
                        q, 0.0, lower_bound, 0.0, lmbda, t, prob_above, 1.0, True)
        s = (s - 1) * 60  # convert to minutes
        t_estimate = lmbda * s * prob_above/60.0
        alpha = fractional_part(t_estimate)
        s = calculate_s(w, s, beta, alpha, p, lowest_winning_bid, upper_bound, q,
                        calculate_upper(alpha, t_estimate), lower_bound,
                        math.floor(t_estimate), lmbda, t, prob_above, 1.0, False)
        s = (s - 1.0)/60
    return s

def calculate_s(w: float,
                s: float,
                beta: float,
                alpha: float,
                p: float,
                the_low_value: float,
                U: float, q: int,
                high_val_consumers_up: float,
                L: float,
                high_val_consumers_down: float,
                lmbda: float,
                t: int,
                prob_above: float,
                i: float,
                is_hours: bool) -> float:
    """
    Summary line.

    Extended description of function.

    Parameters
    ----------
    w: description
    s: description
    beta: description
    alpha: description
    p: description
    the_low_value: description
    U: description
    high_val_consumers_up: description
    L: description
    high_val_consumers_down: description
    lmbda: description
    t: description
    prob_above: description
    i: description
    is_hours: description

    Returns
    -------
    The appropriate integer for that selection.

    """
    if is_hours:
        adjust = 1.0
    else:
        adjust = 1.0/60.0
    continue_computing = True
    while (continue_computing and
           test_function(adjust * w, s, beta, alpha, p, the_low_value,
                         U, q, high_val_consumers_up, L, high_val_consumers_down)):
        s += i
        t_estimate = lmbda * s * adjust * prob_above
        alpha = fractional_part(t_estimate)
        high_val_consumers_up = calculate_upper(alpha, t_estimate)
        high_val_consumers_down = math.floor(t_estimate)
        s_upper = calculate_s_upper(t, q, lmbda, prob_above)
        if s * adjust >= s_upper:
            s = s_upper/adjust
            continue_computing = False
    return s

def fractional_part(x: float) -> float:
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
    return x - math.floor(x)

def round_towards_zero(x: float) -> float:
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
    if x < 0:
        ret_val = math.ceil(x)
    else:
        ret_val = math.floor(x)
    return ret_val

def round_away_from_zero(x: float) -> float:
    """
    Rounds floating point numbers away from zero.
    """
    ret_val: float
    if x > 0:
        ret_val = math.ceil(x)
    else:
        ret_val = math.floor(x)
    return ret_val

def calculate_upper(x: float,
                    y: float) -> float:
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
    return y if (x == 0.0) else math.ceil(y)

def calculate_s_upper(len_of_auction: float,
                      quantity_auctioned: int,
                      l: float,
                      pa: float) -> float:
    """
    Summary line.

    Extended description of function.

    Parameters
    ----------
    len_of_auction: description
    quantity_auctioned: description
    l: description
    pa: description

    Returns
    -------
    The appropriate integer for that selection.

    """
    return min(len_of_auction, quantity_auctioned/l/pa)

def poisson(lmbda: float,
            x: int) -> float:
    """
    Calculates the Poisson pdf.

    Extended description of function.

    Parameters
    ----------
    lmbda: description
    x: description

    Returns
    -------
    The appropriate integer for that selection.

    """
    return math.exp(-1 * lmbda) * math.pow(lmbda, x)/math.factorial(x)

