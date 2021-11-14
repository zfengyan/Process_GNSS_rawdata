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
    x_set, y_set = get_long_lat("new_gpgga.txt")
    result = covariance(x_set, y_set)
    print(result)
    print(np.mean(x_set),np.mean(y_set))
    
    plt.figure()
    plt.xlabel('Longitude')
    plt.ylabel('Latitude') 

    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')

    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', np.mean(y_set)))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', np.mean(x_set)))

    #plt.xlim(min(x_set), max(x_set))
    #plt.ylim(min(y_set), max(y_set)) 

    plt.xticks([])
    plt.yticks([])

    #plt.text(np.mean(x_set),np.mean(y_set),(round(np.mean(x_set),2),round(np.mean(y_set)),2),color='r')
    
    plt.scatter(x_set,y_set,marker='.')
    plt.scatter(np.mean(x_set),np.mean(y_set),marker = '*')
    plt.show()

    #x = np.linspace(-5, 5, 100)
    #y1 = 0.5 * x
    #y2 = x * x
 
    #plt.figure()
    #plt.xlabel('Longitude')
    #plt.ylabel('Latitude')
 
    #ax = plt.gca()
 
    #ax.spines['right'].set_color('none')
    #ax.spines['top'].set_color('none')
 
    #ax.xaxis.set_ticks_position('bottom')
    #ax.yaxis.set_ticks_position('left')
 
    #ax.spines['bottom'].set_position(('data', 0))
    #ax.spines['left'].set_position(('data', 20)) 
    
    #plt.xlim(-50, 50)  # 设定绘图范围
    #plt.ylim(-10, 10) 
    
    #plt.plot(x, y1, linestyle='--')
    #plt.plot(x, y2)
 
    #plt.show()


if __name__ == "__main__":
    main()
