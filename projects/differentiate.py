import numpy as np


def differentiate(u: np.ndarray, dt: float) -> np.ndarray:
    du=[]
    for i in range(0,len(u)-1):
        du.append((u[i + 1] - u[i]) / ( dt))
    du.append((u[-1] - u[-2]) / ( dt))
    return np.array(du)

def differentiate_vector(u: np.ndarray, dt: float) -> np.ndarray:
    du = np.empty_like(u, dtype=float)
    du[:-1] = (u[1:] - u[:-1]) / dt      
    du[-1]  = (u[-1] - u[-2]) / dt       
    return du

def test_differentiate():
    t = np.linspace(0, 1, 10)
    dt = t[1] - t[0]
    u = t**2
    du1 = differentiate(u, dt)
    du2 = differentiate_vector(u, dt)
    assert np.allclose(du1, du2)

if __name__ == '__main__':
    test_differentiate()
    
