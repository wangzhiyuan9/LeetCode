
import numpy as np
def GM1n(x0,y0,z0):
    x0 = np.array([x0]).T
    y0 = np.array([y0]).T
    z0 = np.array([z0]).T

    n = x0.shape[0]
    m = n+6

    x1 = x0.cumsum(axis=0)
    y1 = y0.cumsum(axis=0)
    z1 = z0.cumsum(axis=0)

    Z1 = np.zeros(n-1)
    for i in range(1,n):
        Z1[i-1] = (0.5*x1[i]+(1-0.5)*x1[i-1])

    B = np.ones([n-1,3])
    Y = np.ones([n-1,1])

    for i in range(n-1):
        Y[i][0] = x0[i+1]
        B[i][0] = -Z1[i]
        B[i][1] = y1[i+1]
        B[i][2] = z1[i+1]

    u = np.dot((np.dot(np.linalg.inv(np.dot(B.T,B)),B.T)),Y)

    a=u[0][0]
    b=u[1][0]
    c=u[2][0]

    X1F = np.zeros(m)
    X1F[0] = x0[0][0]

    for i in range(1, m):
        X1F[i] = (x0[0][0] - b * y1[i][0] / a - c * z1[i][0] / a) * np.exp(
            -1 * a * i) + b * y1[i][0] / a + c * z1[i][0] / a

    X0F = np.zeros(m)
    X0F[0] = x0[0][0]

    for i in range(1,m):
        X0F[i] = X1F[i] - X1F[i-1]
    X0F = np.array([list(X0F)]).T
    return X0F



x0 = [221.3, 255.6, 308.3, 331.9, 366, 383.1, 418.1]
y0 = [
    130756, 131448, 132129, 132802, 133450, 134091, 134735, 135404, 136072,
    136782, 137462, 138271, 139008
]
z0 = [
    185998.9, 219028.5, 270704.0, 321229.5, 347934.9, 410354.1, 483392.8,
    537329.0, 588141.2, 644380.2, 686255.7, 743408.3, 831381.2
]


GM1n(x0,y0,z0)