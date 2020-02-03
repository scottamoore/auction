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
import consumer as con

class Generate_Consumers:
    def __init__(self, how_many=5, consumer_type=None):
        self.how_many = how_many
        self.consumer_type = consumer_type
        self.all_consumers = self._all()
    def __str__(self):
        ret_val = []
        for con in self.all_consumers:
            ret_val.append(f"{con}")
        return ", ".join(ret_val)
    def __repr__(self):
        return (f"generate_consumers.Generate_Consumers(how_many={self.how_many}, " +
                ", ".join([f"{con}" for con in self.all_consumers]))
    def _all(self):
        return [con.Consumer() for _ in range(0, self.how_many)]
