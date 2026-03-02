import pandas as pd

def unisex(allnames):
  indexedNames = allnames.set_index(['name', 'year'])

  boyNames = indexedNames.loc['M',:]
  girlNames = indexedNames.loc['F',:]

  unisexDF = pd.merge(boyNames,girlNames, on='name', suffixes=['_boys', '_girls'])
  unisexDF['sum'] = unisexDF.number_boys + unisexDF.number_girls
  unisexDF['ratio'] = unisexDF.number_boys / unisexDF.number_girls

  unisexDF = unisexDF[(0.5 < unisexDF.ratio) & (unisexDF.ratio < 2)]
  return unisexDF.sort_values('name', ascending=False).head(10).sum
