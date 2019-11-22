# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import matplotlib.pyplot as plt
import numpy as np

data = []
class LantouziPipeline(object):
    def process_item(self, item, spider):
        temp = item['year'] + ',' + item['month'] + ',' + item['day'] + ',' + item['count'] + ',' + item['money']
        #print("pipeline")
        print(temp)
        d = temp.split(',')
        #print(d)
        data.append(d)
        sort_data = sorted(data, key=lambda tm:(tm[0], tm[1], tm[2]), reverse=False)
        sort_data = np.array(sort_data)
        #print(sort_data)
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
        #print(y1)

        plt.cla()
        plt.plot(x, y1, 'r', x, y2, 'b')
        plt.legend(['count', 'money'])
        plt.pause(0.01)
        #print(temp)
        with open('lantouzi.csv', 'a') as fp:
            fp.write(temp)
            fp.write('\n')
        return item
