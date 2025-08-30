import numpy as np
from typing import Callable

def mesh_function(f: Callable[[float], float], t: np.ndarray) -> np.ndarray:
    t = np.asarray(t, dtype=float)
    vals = [f(float(ti)) for ti in t]
    return np.asarray(vals, dtype=float)

def func(t: float) -> float:
    return np.exp(-t) if t < 4.0 else np.exp(-12.0)

def test_mesh_function():
    t = np.array([1, 2, 3, 4], dtype=float)
    f = np.array([np.exp(-1), np.exp(-2), np.exp(-3), np.exp(-12)], dtype=float)
    fun = mesh_function(func, t)
    assert np.allclose(fun, f)


if __name__ == "__main__":
    test_mesh_function()




