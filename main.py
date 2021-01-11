import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")


def Import_data(path):
    '''Importe la donnée.
    
    Keyword arguments:
    path - path du jeu de données
    '''
    
    pd.read_csv(path)
   
   
def CleanFilter_data():
    '''Nettoye les données et ne conserve que les observations et variables souhaitées.'''
    
    
def ScoresNZipcode():
    '''Calcule le score et merge avec le code postal.'''
    
    
def Convert_to_heatmap():
    '''Convertit le jeu de données en carte de chaleur géographique.
    
    Source: https://medium.com/@m_vemuri/create-a-geographic-heat-map-of-the-city-of-toronto-in-python-cd2ae0f8be55
    
    Commencer par Toronto pour le tutoriel'''
    
    shape files
    

if __name__ == "__main__":

    Import_data('data.csv')
    
    CleanFilter_data()
    
    ScoresNZipcode()
    
    Convert_to_heatmap()
