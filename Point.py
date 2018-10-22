import numpy as numpy
from scipy.spatial import distance


class Point(object):
    def __init__(self, x=0, y=0, group=0):
        self._x = x
        self._y = y
        self._group = group
        self._ax = None
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, val):
        if val > 0:
            self._x = val
        else:
            raise Exception('asdasd')

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, val):
        self._y = val

    @property
    def group(self):
        return self._group
    
    @group.setter
    def group(self, val):
        self._group = val

    @property
    def ax(self):
        return self._ax
    
    @ax.setter
    def ax(self, val):
        self._ax = val