from kScribus import *
import pandas as pd

def image_prompt_generation():
    excel_file_path = './bdd_images.xlsx'
    # Charger les DataFrames
    xlsdf = pd.read_excel(excel_file_path, sheet_name='liste')
    ktext = ''
    for kelement in xlsdf.itertuples():
        ktext += f'{kelement.name} : ' 
        ktext += f'A hand-drawn illustration on white textured paper. '
        ktext += f'A detailed ink-color-style drawing shows {kelement.prompt}. '
        ktext += f'The drawing features in colors ink with minimal shading, ink-pen rendering in square form paper. '
        ktext += f'The illustration is centered and clear. The background is white paper, '
        ktext += f'enhancing the traditional drawing effect.'
        ktext += '\n'
    with open('generation_image.txt', 'w', encoding='utf-8') as f:
        f.write(ktext)

if __name__ == "__main__":
    image_prompt_generation()