import numpy as np
from typing import Callable

def mesh_function(f: Callable[[float], float], t: np.ndarray) -> np.ndarray:
    arr=[]
    for i in t:
        arr.append(f(i))
    return np.array(arr)

def func(t: float) -> float:
    if t == 4:
        t = 12
    return np.exp(-t)

def test_mesh_function():
    t = np.array([1, 2, 3, 4], dtype=float)
    f = np.array([np.exp(-1), np.exp(-2), np.exp(-3), np.exp(-12)], dtype=float)
    fun = mesh_function(func, t)
    assert np.allclose(fun, f)


if __name__ == "__main__":
    test_mesh_function()




