import numpy as np
import matplotlib.pyplot as plt


def get_long_lat(file_nm):
    """
    get longtitude and latitud
    for plot: longtitude -- x
              latitude -- y
    """
    records = []
    with open(file_nm,'r') as fh:
        records = fh.readlines()
    x_set = []
    y_set = []
    for r in records:
        r = r.split(',')
        x_set.append(float(r[4])*0.01) # longtitude to x_set
        y_set.append(float(r[2])*0.01) # latitude to y_set
    return x_set, y_set


def covariance(x_set, y_set):
    """
    calculate the covariance of x and y
    """
    return np.cov(x_set, y_set)
        

def main():
    x_set, y_set = get_long_lat("blocked_gpgga.txt")
    result = covariance(x_set, y_set)
    print(result)
    plt.scatter(x_set,y_set)
    plt.scatter(np.mean(x_set),np.mean(y_set),marker = '*')
    plt.show()


if __name__ == "__main__":
    main()
