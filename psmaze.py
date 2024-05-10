# vim: ts=2 sw=2 expandtab
from pyscript import document
import numpy as np

a = np.zeros((3,4,5),dtype=int)
document.body.append(str(a))
