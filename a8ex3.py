"""
Author: Oleh Karavskyi
Matr.Nr.: k12139895
Exercise: 3
"""


class Aggregator:

    def __init__(self, agg_type: type, ignore_errors: bool = True):
        self.param = None
        # self.sentence = None
        self.agg_type = agg_type
        self.ignore_errors = ignore_errors


    def __call__(self, *args):

        if self.agg_type == int:
            if  self.param == None and args:
                self.param = 0

            for i in args:
                if self.ignore_errors == True:

                    if isinstance(i, int):
                        self.param += i
                else:
                    if isinstance(i, int):
                        self.param += i
                    else:
                        raise TypeError("aggregation only works on type 'int', not 'str'")
            return self.param

        if self.agg_type == str:
            if  self.param == None and args:
                self.param = ''

            for s in args:
                if self.ignore_errors == True:
                    if isinstance(s, str):
                        self.param += s
                else:
                    if isinstance(s, str):
                        self.param += s
                    else:
                        raise TypeError("aggregation only works on type 'str', not 'int'")
            return self.param
