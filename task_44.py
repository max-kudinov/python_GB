import pandas as pd
import random


lst = ["robot"] * 10
lst += ["human"] * 10

random.shuffle(lst)
data = pd.DataFrame({"whoAmI": lst})

print(data)
print()

one_hot_list = list()
for el in lst:
    one_hot_list.append([int(el == "robot"), int(el == "human")])


one_hot_data = pd.DataFrame(one_hot_list, columns=["robot", "human"])
print(one_hot_data)
