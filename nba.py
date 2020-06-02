#Create a dataset that explores the rise in points per game per team from
#2010 to 2018 and look at the trends, maybe focus on 1 team to start
#
#

import pandas as pd
import numpy as np
nba = pd.read_csv("/Users/kylekempt/Desktop/junkyard/nbaallelo.csv")
print(type(nba))




pd.set_option("display.precision", 2)

print(nba.info())

nba_set = pd.DataFrame({
        "team": nba["fran_id"].value_counts()
})

print(nba_set)