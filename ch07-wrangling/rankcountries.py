import pandas as pd

#Paramters:
# medals: a pandas df of event winners with columns Event, Medal, Athlete, Result, Country, Record

def rankcountries(medals):
  totals = medals.groupby('Medal').Country.value_count().unstack(level=0).fillna(0)

  totals['Total'] = totals.sum(axis=1)

  return totals.sort_values(['Totals', 'Gold', 'Silver', 'Bronze'], ascending=False).head(4)