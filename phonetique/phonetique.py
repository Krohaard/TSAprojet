from ..kScribus import *

lenght_card=200
height_card=145
syllabes_colorees = load_syllabes_as_tuples(r'phonetique.json')

xml_content = firstlines_header(total_pages=len(syllabes_colorees),page_width=lenght_card,page_height=height_card) + "\n"
xml_content += checkprofile_pdf()
xml_content += colors_document()
xml_content += style_master_page()
xml_content += init_document(lenght_card,height_card)
xml_content += generate_xml_from_syllables(syllabes_colorees,start_x=1000,start_y=500,step_y=205,page_width=lenght_card,page_height=height_card) + "\n"
xml_content += generate_footer()

# Export en TXT
with open("phonetique.sla", "w", encoding="utf-8") as f:
    f.write(xml_content)

print("Fichier 'phonetique.sla' généré avec couleurs par segment.")