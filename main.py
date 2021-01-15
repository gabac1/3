import pandas as pd
import numpy as np

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for county, vote in counties_dict.items():
        print(f"{county} county has {vote} registered votes")

for dicti in voting_data:
        print(dicti["county"],dicti["registered_voters"])