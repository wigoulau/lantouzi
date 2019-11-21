#--*-- coding: utf-8 --*--

import numpy as np
import matplotlib.pyplot as plt
import time

with open('lantouzi.csv', 'r') as fp:
    data = []
    content = fp.readlines()
    for line in content:
        #print(line)
        d = line.split(',')
        data.append(d)
        sort_data = sorted(data, key=lambda tm:(tm[0], tm[1], tm[2]), reverse=False)
        sort_data = np.array(sort_data)
        #sort_data = list(map(int, sort_data))
        x = range(len(sort_data))
        y1 = list(map(int, sort_data[:, 3]))
        y2 = list(map(int, sort_data[:, 4]))
        y1 = np.array(y1)
        y2 = np.array(y2)
        y1_min = min(y1)
        y1_max = max(y1)
        y2_min = min(y2)
        y2_max = max(y2)
        y2 = (y2 - y2_min) / (y2_max - y2_min) * (y1_max - y1_min) + y1_min
        plt.cla()
        plt.plot(x, y1, 'r', x, y2, 'b')
        plt.legend(['count', 'money'])
        plt.pause(0.01)
        #print(x)
        #print(y1)
        # print(y2)
        # plt.subplot(221)
        # plt.cla()
        # plt.plot(x, y1)
        # plt.subplot(222)
        # plt.cla()
        # plt.plot(x, y2)
        #plt.pause(0.01)
    plt.show()

