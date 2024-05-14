import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


# clean data using pandas 
data=pd.read_excel("C:/Users/user/Desktop/py/MNG_bourse_data.xlsx")
#creation d'une dataFrame à partir des données du fichier 
dff=pd.DataFrame(data)
#suppression des doublons
dff=dff.drop_duplicates()
print("les doublons sont supprimées")

#gestion des données manquantes 
    #on va remplacer les valeurs manquantes par des 0
new_data=dff.fillna(0)
    #ecrire la nouvelle data dans le fichier
new_data.to_excel("C:/Users/user/Desktop/py/donnees_bourse6.xlsx", index=False)
print("new_data ecrite dans donnees_bourse6.xlsx")

#traitement des valeurs abberantes pour l'attribut "cumulVolumeEchange"
  #génération de la boite à moustache pour visualiser les valeurs abberantes 
sample= new_data["attributes.cumulVolumeEchange"].to_list()
plt.boxplot(sample, vert=False)
plt.title("detection des valeurs abberantes")
plt.xlabel('cumulVolumeEchange')
plt.show()

# pour detecter les valeurs abberantes 
   #méthode du score Z
outliers = []
def detect_outliers_zscore(data):
    thres = 3
    mean = np.mean(data)
    std = np.std(data)
    
    for i in data:
        z_score = (i-mean)/std
        if (np.abs(z_score) > thres):
            outliers.append(i)
    return outliers
sample_outliers = detect_outliers_zscore(sample)
print("valeurs abberantes detecté avec la methode Z-scores : ", sample_outliers) 
'''
noter qu'il est tres important de gérer les valeurs abberants soit en les supprimes ou bien
en les remplace par la moyenne , mais dans notre projet on manipule des données finnanciers qui sont 
assez sensibles, pour cette raison que j ai garder la valeur abberante detecté par 
la fonction detect_outliers_zscore. pour savoir plus voir LISEZMOI
'''