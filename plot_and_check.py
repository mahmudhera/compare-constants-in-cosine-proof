from matplotlib import pyplot as plt
import numpy as np

def f1(epsilon):
    return np.sqrt( (1+epsilon)/(1-epsilon) )

def f2(epsilon):
    return (1-epsilon)/(1+epsilon)

if __name__ == '__main__':
    epsilons = np.linspace( 0.0001, 0.5, 200 )
    f1_vectorized = np.vectorize(f1)
    f1_values = f1_vectorized(epsilons)
    f2_vectorized = np.vectorize(f2)
    f2_values = f2_vectorized(epsilons)

    plt.plot(epsilons, f1_values, label='sqrt( (1+epsilon)/(1-epsilon)')
    plt.plot(epsilons, f2_values, label='(1-epsilon)/(1+epsilon)')
    plt.legend()

    plt.show()
