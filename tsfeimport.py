#%% [markdown]
# # TSFE Analysis
#%% [markdown]
# Some great folks in the JM sub on Reddit cataloged all songs played during The Search For Everything tour in '17. This is a csv version of that Google Sheet. The origional can be found here: https://docs.google.com/spreadsheets/d/1DeS4XIgtaw4LVuUXX3LLTStRbiaU_RDBy_RqJBXQ6JY/edit#gid=0
# 
# I've added a column the represents the album the song was from.
# 
#%% [markdown]
# ### Load and check out the first 5 rows

#%%
import pandas as pd

df = pd.read_csv('tsfe17.csv')
print(df.head(5))

#%% [markdown]
# #### Do some album counts for all the shows
# Interesting columns: id, Song, Album
# 

#%%
# df.loc[df['A'] == 'foo']
tsfe = df.loc[df['Album'] == 'TSFE']
print("TSFE: ", tsfe.shape[0])

cont = df.loc[df['Album'] == 'C']
print("Continuum: ", cont.shape[0])


#%%


