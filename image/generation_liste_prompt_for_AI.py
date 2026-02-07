from kScribus import *
import pandas as pd

def liste_image_from_json():
    xml_content=""
    ktest = trouver_fichiers_json_recursif('.')
    syllabes_colorees = []
    for pathfile in ktest:
        syllabes_colorees.extend(load_pictures_name(pathfile))

    for kelem in syllabes_colorees:
        xml_content += kelem[1] + "\t" + kelem[0] + "\n"

    # Export en TXT
    with open("liste.csv", "w", encoding="utf-8") as f:
        f.write(xml_content)

    print(f'fichier générer')
def liste_image_from_xls():
    xml_content = ''
    file_xls = 'bdd_images.xlsx'
    df = pd.read_excel(file_xls,sheet_name='liste')
    for krow in df.itertuples(index=True):
        xml_content += krow.theme + '\t' + krow.name + '\n'
    # Export en TXT
    with open("liste.csv", "w", encoding="utf-8") as f:
        f.write(xml_content)
    print(f'fichier lisete.csv générer.')

if __name__ == "__main__":
#    liste_image_from_json()
    liste_image_from_xls()