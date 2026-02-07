from typing import TextIO

def main():
    # Recharger les mots et descriptions après réinitialisation de l'état

    mots = [
        "banane", "haricots verts", "courgette", "chou-fleur", "carotte", "pâtes",
        "pelmeni", "viande haché", "boulette de viande", "pain", "jus vert", "pizza", "patates",
        "frites", "chips", "soupe", "champignon", "citrouille", "sarrasin", "semoule de blé",
        "riz", "maïs", "lardon", "jambon", "poisson blanc", "poisson rouge", "poisson pané",
        "nuggets", "filet de poulet", "croque monsieur", "fromage",
        "pomme","jus de pomme","biscuit","cookie chocolat","polenta","petit pois","jus jaune",
        "kiwi","verre d’eau","melon","pastèque"
    ]

    descriptions = {
        "banane": "a ripe yellow banana, slightly curved, with smooth skin and a few brown speckles",
        "haricots verts": "a small bunch of long, slender green beans, fresh and shiny, laid together",
        "courgette": "a dark green zucchini, elongated, with smooth glossy skin and a small stem",
        "chou-fleur": "a large, compact head of ivory-white cauliflower with pale green leaves at the base",
        "carotte": "a bright orange carrot, conical and slightly dirty, with fresh green tops still attached",
        "pâtes": "a small pile of dry pasta (penne, spaghetti, or farfalle), slightly dusty with flour",
        "pelmeni": "small raw Russian dumplings in hexagonal shapes, lightly floured and arranged in a circle",
        "viande hachée": "a portion of raw ground meat, bright red, with tangled strands and a moist texture",
        "boulette de viande": "several cooked meatballs, browned on the outside, resting on a plate",
        "pain": "a rustic loaf of bread with a golden, cracked crust and a soft interior showing",
        "jus vert": "a glass of thick green juice",
        "pizza": "a slice of thin-crust pizza with tomato sauce, melted cheese, and mushroom slices",
        "patates": "whole raw potatoes, earthy and unpeeled, medium-sized with light brown skin",
        "frites": "a handful of crispy golden fries, lightly salted, stacked on a napkin",
        "chips": "thin, rippled potato chips, golden and slightly oily, stacked loosely",
        "soupe": "a steaming bowl of soup with visible vegetables and a wooden spoon beside it",
        "champignon": "a whole white button mushroom with a short stem and round cap",
        "citrouille": "a round orange pumpkin with ribbed skin and a greenish stem",
        "sarrasin": "a small bowl of raw buckwheat grains, small triangular in shape, brown/light brown in color",
        "semoule de blé": "a small bowl of golden-beige fine semolina, resembling coarse sugar",
        "riz": "a small bowl of uncooked white rice grains, long and dry, spilling slightly",
        "maïs": "a fresh corn cob with bright yellow kernels and some green husk partially peeled back",
        "lardon": "small diced pieces of bacon, pink with white fat, slightly crispy",
        "jambon": "a thin slice of ham, light pink, either flat or rolled on a wooden board",
        "poisson blanc": "a raw white fish fillet (like cod), slightly translucent, resting on crushed ice",
        "poisson rouge": "a live goldfish swimming in a small glass bowl or aquarium",
        "poisson pané": "a golden, crispy breaded fish stick, hot and freshly cooked",
        "nuggets": "several golden chicken nuggets, crunchy, arranged in a semicircle with dipping sauce",
        "filet de poulet": "a grilled chicken breast fillet with visible grill marks and juicy texture",
        "croque monsieur": "a toasted sandwich with melted cheese oozing, slightly crisp and layered",
        "fromage": "a wedge of hard cheese (like Comté), with a natural rind and a clean cut face",
        "pomme" : "a shiny red apple with a smooth surface, a small green leaf attached to the stem, sitting on a flat surface",
        "jus de pomme" : "a clear glass of golden apple juice with a few bubbles at the top, next to a sliced apple",
        "biscuit" : "a round, golden-brown biscuit or shortbread cookie with a simple, slightly crumbly texture",
        "cookie chocolat" : "a thick chocolate chip cookie with visible chunks of chocolate, slightly cracked on top",
        "polenta" : "a small bowl of yellow cooked polenta, smooth and slightly creamy, possibly served on a plate",
        "petit pois" : "a small pile of bright green peas, either loose or in a partially opened pod",
        "jus jaune" : "a clear glass of yellow juice",
        "kiwi" : "a halved kiwi fruit showing its bright green flesh and small black seeds, next to an uncut fuzzy brown kiwi",
        "verre d’eau" : "a clear glass filled with very light blue water, placed on a table with light reflections on the surface",
        "melon" : "a round cantaloupe with a rough, netted rind, shown whole and sliced to reveal its orange flesh and seeds",
        "pastèque" : "a large watermelon, green-striped on the outside, with a bright red interior and black seeds, shown whole and in triangular slices"
    }

    # Générer les prompts personnalisés
    custom_prompts = []
    for mot in mots:
        desc = descriptions.get(mot, f"a symbolic representation of the word '{mot}'")
        prompt = (
            f'A hand-drawn illustration on off-white textured paper. '
#            f'At the top, the word "{mot}" is written in lowercase bold black letters. '
            f'A detailed ink-style drawing shows {desc}. '
            f'The drawing features cross-hatching shadows and a sketchy, ink-pen rendering with color in square form paper. '
            f'The illustration is centered and clear. The background has the texture of slightly aged, off-white paper, '
            f'enhancing the traditional drawing effect. The overall style is reminiscent of naturalist or dictionary illustrations.'
        )
        custom_prompts.append((mot, prompt))

    # Écriture dans le fichier
    with open('repas.txt', 'w', encoding='utf-8') as kFile:
        for kprompt in custom_prompts:
            kFile.write(str(kprompt[0])+':\n')
            kFile.write(str(kprompt[1])+'\n\n')


if __name__ == "__main__":
    main()
    print("Fin du programme.")
    input("Appuyez sur Entrée pour quitter...")