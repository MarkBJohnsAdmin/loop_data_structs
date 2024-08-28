import numpy as np
import pandas as pd

world_pop = {
    "afghanistan": 30.55,
    "albania": 2.77,
    "algeria": 39.21,
    "andorra": 0.08,
    "angola": 25.83,
    "argentina": 43.85,
    "armenia": 2.92,
    "australia": 24.13,
    "austria": 8.69,
    "azerbaijan": 9.65,
    "bangladesh": 161.20,
    "belarus": 9.50,
    "belgium": 11.31,
    "bhutan": 0.78,
    "bolivia": 11.05,
    "brazil": 207.65,
    "canada": 36.29,
    "chile": 17.91,
    "china": 1408.09,
    "colombia": 48.65,
    "cuba": 11.24,
    "denmark": 5.75,
    "egypt": 94.98,
    "ethiopia": 102.40,
    "france": 66.90,
    "germany": 82.79,
    "india": 1324.17,
    "indonesia": 260.58,
    "iran": 80.28,
    "iraq": 37.20,
    "italy": 60.60,
    "japan": 126.70,
    "kenya": 47.25,
    "mexico": 127.54,
    "nigeria": 186.99,
    "russia": 144.34,
    "south africa": 55.91,
    "spain": 46.56,
    "united kingdom": 65.64,
    "united states": 323.95,
    "vietnam": 92.70,
    "zimbabwe": 16.15
}

# for cntry, pop in world_pop.items():
#     print(f"{cntry} - population: {pop} million")
    
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])

np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

bmi = np_weight / np_height ** 2

np_data = np.array([np_height, np_weight])

# for val in np.nditer(np_data):
#     print(val)
    
brics = pd.read_csv("brics.csv", index_col=0)

for lbl, row in brics.iterrows():
    brics.loc[lbl, "name_length"] = len(row["country"])
    
# print(brics)

brics["cap_length"] = brics["capital"].apply(len)

print(brics)
