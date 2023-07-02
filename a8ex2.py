"""
Author: Oleh Karavskyi
Matr.Nr.: k12139895
Exercise: 2
"""

import os

class Reader:

    def __init__(self, path: str):

        self.fh = open(path, "rb")

    def close (self):
        self.th.close()

    def __len__(self):
        return self.fh.seek(0, os.SEEK_END)


    def __getitem__(self, key):

        if isinstance(key, int):
            if key <= self.fh.seek(0, os.SEEK_END):
                if key >= 0:
                    self.fh.seek(key)
                    return self.fh.read(1)
                else:
                    self.fh.seek(int(self.__len__())+key)
                    return self.fh.read(1)
            else:
                raise IndexError("Reader index out of range")
        else:
            raise TypeError("indexing expects 'int', not 'str'")
