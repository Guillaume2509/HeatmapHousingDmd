import pandas as pd


def Import_data():
    '''Importer la donnée'''
    
    pd.read_csv('data.csv')
   
   
def CleanFilter_data():
    '''Nettoyer les données et ne conserver que les observations et variables souhaitées'''
    
    
def ScoresNZipcode():
    '''Calculer le score et merger avec le code postal'''
    
def Convert_to_heatmap():
    '''Convertir le jeu de données en carte de chaleur géographique'''
    

if __name__ == "__main__":

    Import_data()
    
    CleanFilter_data()
    
    ScoresNZipcode()
    
    Convert_to_heatmap()
