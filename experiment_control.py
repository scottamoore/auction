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
import market as mkt
import etzion as etz
import utilities as util


def control_experiment(assump):
    num_of_simulations: int = 0
    num_of_simulation_sets: int = 1
    print("Beginning to run the simulation.")
    for env in util.get_environment_settings():
        print(f"Environment set for lambda={env.lmbda:.1f}, w={env.w:.1f}")
        for auct in util.get_auction_settings():
            num_of_simulations = run_set_of_simulations_for_settings(assump,
                                                                     env,
                                                                     auct,
                                                                     num_of_simulation_sets,
                                                                     num_of_simulations)
        num_of_simulation_sets += 1
    print(f"Done with all {num_of_simulation_sets - 1} simulation sets ({num_of_simulations} simulations).")


def run_set_of_simulations_for_settings(assump,
                                        env,
                                        auct,
                                        num_of_simulation_sets: int,
                                        num_of_simulations: int) -> int:
    print(f"Simulation set {num_of_simulation_sets} beginning with simulation #{num_of_simulations}: " +
          f"(q,t,p) = {auct.q}, {auct.t}, {auct.p:.1f}")
    auctions_to_run: int = util.get_number_of_auctions_to_run(auct.q, auct.t, env.lmbda)
    auctions_to_run = 3
    for auct_num in range(0, auctions_to_run):
        arrival_times: List[float] = util.get_all_arrival_times(env.lmbda, max_time=auct.t)
        num_of_consumers: int = len(arrival_times)
        valuations: List[float] = util.random_list(assump.min_val, assump.max_val, num_of_consumers)
        for the_market in [mkt.JustPosted(env, auct, arrival_times, valuations),
                           mkt.JustSealed(env, auct, arrival_times, valuations),
                           mkt.JustOpen(env, auct, arrival_times, valuations),
                           mkt.DualSealed(env, auct, arrival_times, valuations),
                           mkt.DualOpen(env, auct, arrival_times, valuations)]:
            num_of_simulations += 1
            expected_profit: float = etz.expected_profit(auct,
                                                         env,
                                                         assump.min_val,
                                                         assump.max_val,
                                                         1)
            print(f"Expected Profit/Hour (for {auct.t} hours)={expected_profit/auct.t:.2f}" +
                  f" & Profit/Item (for {auct.q} items)={expected_profit/auct.q:.2f}")
            the_market.setup(auctions_to_run)
            the_market.run()
            mkt_stats = the_market.statistics() # TODO: how to record the statistics?
            #print(f"mkt_stats={mkt_stats}")
    return num_of_simulations
