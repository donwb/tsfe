
#%% [markdown]
# ## This is me testing the python interactive environment in VSCode
# ### This is a subhead



#%%
import pandas as pd
df = pd.read_csv("tsfe17.csv")
df.head(10)

#%%
tsfe = df.loc[df['Album'] == 'TSFE']
print("TSFE: ", tsfe.shape[0])

cont = df.loc[df['Album'] == 'C']
print("Continuum: ", cont.shape[0])


#%%
print('hey')


