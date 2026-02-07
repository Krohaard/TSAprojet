from kScribus import *
import pandas as pd

def update_json_file():
    json_file_path = trouver_fichiers_json_recursif('.')
    csv_file_path = './definition.csv'
    df = pd.read_csv(csv_file_path,sep='\t')
    modification = False
    for kindex,kelement in df.iterrows():
        for kfile in json_file_path:
            with open(kfile, "r", encoding="utf-8") as f:
                data = json.load(f)
            for kobjet in data:
                if kobjet.get('file') == kelement['file']:
                    prompt = (
                        f'A hand-drawn illustration on white textured paper. A detailed ink-color-style drawing shows '
                        f'{kelement['description']} '
                        f'The drawing features in colors ink with minimal shading, ink-pen rendering in square form paper. '
                        f'The illustration is centered and clear. The background is white paper, enhancing the traditional drawing effect.'
#                        f'The overall style is reminiscent of naturalist or dictionary illustrations.'
                    )

                    kobjet['prompt'] = kelement['description']
                    modification = True
            if modification == True:
                with open(kfile, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
                    modification = False

def update_excel_file():
    excel_file_path = './bdd_images.xlsx'
    csv_file_path = './definition.csv'

    # Charger les DataFrames
    xlsdf = pd.read_excel(excel_file_path, sheet_name='liste')
    csvdf = pd.read_csv(csv_file_path, sep='\t')
    
    # Vérification des colonnes pour s'assurer qu'elles existent
    if 'name' not in xlsdf.columns or 'theme' not in xlsdf.columns or 'prompt' not in xlsdf.columns:
        print("Erreur: Le DataFrame Excel doit contenir les colonnes 'name', 'theme' et 'prompt'.")
        return
    
    # Itérer sur les données du CSV (source des mises à jour)
    for index_csv, kelement in csvdf.iterrows():
        # Itérer sur le DataFrame Excel (cible des mises à jour)
        # On utilise iterrows() pour avoir un accès direct à l'index (index_excel)
        for index_excel, krow in xlsdf.iterrows():
            
            # Vérifier la condition de correspondance (les clés de jointure)
            if (krow['name'] == kelement['name']) and (krow['theme'] == kelement['theme']):
                
                # Mettre à jour le DataFrame xlsdf en utilisant .loc[index, colonne]
                # Cette ligne est la correction critique :
                xlsdf.loc[index_excel, 'prompt'] = kelement['prompt']
                
                # Optionnel : Sortir de la boucle interne une fois la correspondance trouvée
                break 

    # Écrire le DataFrame mis à jour dans le fichier Excel
    xlsdf.to_excel(
        excel_writer=excel_file_path,
        sheet_name='liste',
        index=False,
        header=True
    )
    print(f"Mise à jour terminée. Le fichier '{excel_file_path}' a été réécrit.")

if __name__ == "__main__":
#    update_json_file()
    update_excel_file()