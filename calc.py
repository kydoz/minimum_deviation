import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
top_angle = float(input("Top angle: "))
#angle_of_incidence = float(input("Incidence angle: "))
refractive_index = float(input("Refractive index "))


fig, ax = plt.subplots()
x_list=[]
y_list = []
for x in range(0,90,1):
    try:
        dev = math.radians(x) + math.asin(refractive_index*math.sin(math.radians(top_angle)-math.asin(math.sin(math.radians(x))/refractive_index)))-math.radians(top_angle)
        x_list.append(x)
        y_list.append(math.degrees(dev))
    except ValueError:
        print("Value error")
        continue
if len(y_list) == 0:
    print("No angles of deviation found")
else:
    print(min(y_list))
    min_div = math.radians(min(y_list))
    n_result = math.sin((min_div+math.radians(top_angle))/2)/math.sin(math.radians(top_angle)/2)
    print(f"The refractive index: {n_result}")
    ax.plot(x_list, y_list)
    ax.set_xlabel('Angle of incidence')
    ax.set_ylabel('Angle of deviation')
    ax.set_title(f"Minimum deviation of the prism \n top angle: {int(top_angle)}, refractive index: {refractive_index}")
    ax.annotate(f'minimum of deviation: {round(min(y_list), 2)}', xy=(x_list[y_list.index(min(y_list))], min(y_list)), xytext=(x_list[y_list.index(min(y_list))], min(y_list)+max(y_list)*0.25),
                arrowprops=dict(facecolor='black', shrink=0.05))
    plt.show()


