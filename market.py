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
import generate_consumers as gcon

class Market:
    def __init__(self, env, auct, arrival_times, valuations):
        self.how_many = len(arrival_times)
        self.lmbda = env.lmbda
        self.w = env.w
        self.q = auct.q
        self.t = auct.t
        self.p = auct.p
        #TODO: define all of the consumers here
        pass
    def __str__(self):
        if self.consumers:
            the_text = ", ".join([f"{con}" for con in self.consumers])
        else:
            the_text = "none"
        return f"Market(how_many={self.how_many}, consumers=[{the_text}])"
    def __repr__(self):
        if self.consumers:
            the_text = ", ".join([f"{con}" for con in self.consumers])
        else:
            the_text = "none"
        return f"market.Market(how_many={self.how_many}, consumers=[{the_text}])"
    def add_consumers(self, list_of_consumers):
        self.consumers = list_of_consumers
    def setup(self, auctions_to_run):
        self.auctions_to_run = auctions_to_run
    def run(self):
        pass
    def statistics(self):
        pass


class JustPosted(Market):
    pass


class JustSealed(Market):
    pass


class JustOpen(Market):
    pass


class DualOpen(Market):
    pass


class DualSealed(Market):
    pass


