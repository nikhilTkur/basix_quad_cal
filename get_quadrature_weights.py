import numpy as np
import quadpy
import csv

orders = [10,11,12,13,14,15,16,17,18,19,20]

for i in orders:
    scheme_name = f'xiao_gimbutas_{i}'
    scheme = quadpy.t2.schemes[scheme_name]()
    scheme_x = scheme.points[0]
    scheme_y = scheme.points[1]
    scheme_w = scheme.weights

    with open(f'xiao_gimbutas_{i}_data.csv', mode='w') as file:
        writer = csv.writer(file, delimiter=',')
        for j in range(0, scheme_x.shape[0]):
            writer.writerow([scheme_x[j], scheme_y[j]])
        file.close()
    with open(f'xiao_gimbutas_{i}_weights.csv', mode='w') as file:
        writer = csv.writer(file, delimiter=',')
        for j in range(0, scheme_w.shape[0]):
            writer.writerow([scheme_w[j]])
        file.close()
