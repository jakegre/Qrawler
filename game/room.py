from random import randint as r
from matplotlib import animation, pyplot as plt
from matplotlib.axes import Axes
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.figure import Figure
import numpy as np
import numpy.typing as npt
LIMITS = (-1, 1)
class makeRoom:

    def __init__(self):
        #self.size = r(6, 12)
        #self.xWall = "*\t"*self.size
        #self.yWall = ("*\n\n")*self.size
        #print(self.xWall, self.yWall)
        self.fig:Figure=plt.figure(figsize=(20,6))
        self.ax=self.fig.add_subplot(111,projection=Axes3D.name)
        self.fig.subplots_adjust(top=1.1, bottom=-0.1)
        self.func_ = lambda x, y: np.cos(10*x)

if __name__ == "__main__":
    makeRoom()
    plt.show
