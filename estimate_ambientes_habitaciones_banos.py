import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#df = pd.read_csv('/Users/ezequieldjemdjemian/Documents/TP_FIUBA_Regresion/ventas.csv')
df = pd.read_csv('ventas.csv')

print(df.info())

import statsmodels.api as sm
import statsmodels.formula.api as smf

df = df[df['lat'].isnull==False]
model = smf.ols("ambientes ~ lat + lon + L1 + L2 + operacion + tipo + ambientes ", data = df).fit()
print(model.summary())

