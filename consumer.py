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
import strategy as strat

class Consumer:
    def __init__(self):
        self.strategy = strat.Strategy()
    def __str__(self):
        return f"Consumer(strategy={self.strategy})"
    def __repr__(self):
        return f"consumer.consumer(strategy={self.strategy})"
