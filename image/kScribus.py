import pathlib
import json
import math
from PIL import Image
from typing import List

def trouver_fichiers_json_recursif(dossier_racine: str) -> List[str]:
    """
    Recherche tous les fichiers .json dans le dossier racine et ses sous-dossiers.

    Args:
        dossier_racine: Le chemin du dossier à partir duquel commencer la recherche.

    Returns:
        Une liste d'objets pathlib.Path représentant les fichiers JSON trouvés.
    """
    # Crée un objet Path pour le dossier racine
    chemin_racine = pathlib.Path(dossier_racine)
    liste_fichier=[]
    # Utilise la méthode .rglob() pour une recherche récursive
    # '**/*.json' signifie :
    # - '**': chercher dans tous les répertoires, y compris les sous-répertoires (récursif)
    # - '*.json': correspondre à tous les fichiers se terminant par .json
    fichiers_json = list(chemin_racine.rglob('**/*.json'))
    for chemin in fichiers_json:
        liste_fichier.append(str(chemin.resolve()))

    return liste_fichier

def load_syllabes_as_tuples(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    # Convertir chaque sous-liste en tuples
    return [ [tuple(item) for item in group] for group in data ]

def load_pictures_name(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
        lol = []
    # Convertir chaque sous-liste en tuples
    return [ [group['name'],group['file'],group['display']] for group in data ]

def firstlines_header(total_pages, page_width, page_height):
    if total_pages==0:
        total_pages=1
    header = []
    header.append('<?xml version="1.0" encoding="UTF-8"?>')
    header.append('<SCRIBUSUTF8NEW Version="1.7.0.svn">')
    header.append(
        f'    <DOCUMENT ANZPAGES="{total_pages*2}" PAGEWIDTH="{page_width}" PAGEHEIGHT="{page_height}" '
        f'BORDERLEFT="{9}" BORDERRIGHT="{9}" BORDERTOP="{9}" BORDERBOTTOM="{9}" PRESET="0" BleedTop="6" BleedLeft="6" '
        f'BleedRight="6" BleedBottom="6" ORIENTATION="1" PAGESIZE="Custom" FIRSTNUM="1" BOOK="1" AUTOSPALTEN="1" '
        f'ABSTSPALTEN="31.1811023622047" UNITS="0" DFONT="Arial Regular" DSIZE="12" DCOL="1" DGAP="0" TabFill="" '
        f'TabWidth="36" TextDistLeft="0" TextDistRight="0" TextDistBottom="0" TextDistTop="0" FirstLineOffset="1" '
        f'AUTHOR="" COMMENTS="" KEYWORDS="" PUBLISHER="" DOCDATE="" DOCTYPE="" DOCFORMAT="" DOCIDENT="" DOCSOURCE="" '
        f'DOCLANGINFO="" DOCRELATION="" DOCCOVER="" DOCRIGHTS="" DOCCONTRIB="" TITLE="" SUBJECT="" VHOCH="33" '
        f'VHOCHSC="66" VTIEF="33" VTIEFSC="66" VKAPIT="75" BASEGRID="14.4" BASEO="0" AUTOL="100" UnderlinePos="-1" '
        f'UnderlineWidth="-1" StrikeThruPos="-1" StrikeThruWidth="-1" GROUPC="1" HCMS="1" DPSo="1" DPSFo="1" DPuse="1" '
        f'DPgam="0" DPbla="1" DPPr="ISO Coated v2 300% (basICColor)" DPIn="sRGB v3.0 (Canon)" DPInCMYK="ISO Coated v2 300% (basICColor)" '
        f'DPIn2="sRGB v3.0 (Canon)" DPIn3="ISO Coated v2 300% (basICColor)" DISc="1" DIIm="0" ALAYER="0" LANGUAGE="fr" '
        f'AUTOMATIC="1" AUTOCHECK="0" GUIDELOCK="0" SnapToGuides="0" SnapToGrid="0" SnapToElement="0" MINGRID="20" '
        f'MAJGRID="100" SHOWGRID="0" SHOWGUIDES="1" showcolborders="1" SHOWFRAME="1" SHOWControl="1" SHOWLAYERM="1" '
        f'SHOWMARGIN="1" SHOWBASE="0" SHOWPICT="1" SHOWLINK="1" rulerMode="1" showrulers="1" showBleed="1" rulerXoffset="0" '
        f'rulerYoffset="0" GuideRad="10" GRAB="4" POLYC="4" POLYF="0.502045814642449" POLYR="0" POLYIR="0" POLYCUR="0" '
        f'POLYOCUR="0" POLYS="0" arcStartAngle="30" arcSweepAngle="300" spiralStartAngle="0" spiralEndAngle="1080" '
        f'spiralFactor="1.2" AutoSave="0" AutoSaveTime="600000" AutoSaveCount="1" AutoSaveKeep="0" AUtoSaveInDocDir="1" '
        f'AutoSaveDir="" ScratchBottom="500" ScratchLeft="1000" ScratchRight="1000" ScratchTop="500" GapHorizontal="40" '
        f'GapVertical="60" StartArrow="0" EndArrow="0" PEN="Black" BRUSH="None" PENLINE="Black" PENTEXT="Black" '
        f'StrokeText="Black" TextBackGround="None" TextLineColor="None" TextBackGroundShade="100" TextLineShade="100" '
        f'TextPenShade="100" TextStrokeShade="100" STIL="1" STILLINE="1" WIDTH="1" WIDTHLINE="1" PENSHADE="100" '
        f'LINESHADE="100" BRUSHSHADE="100" CPICT="None" PICTSHADE="100" CSPICT="None" PICTSSHADE="100" PICTSCX="1" '
        f'PICTSCY="1" PSCALE="1" PASPECT="1" EmbeddedPath="0" HalfRes="1" dispX="10" dispY="10" constrain="15" '
        f'MINORC="#00ff00" MAJORC="#00ff00" GuidesColor="#000080" BaselineGridColor="#c0c0c0" renderStack="0 1 2 3 4" '
        f'GridType="0" PAGEC="#ffffff" MARGC="#0000ff" RANDF="1" currentProfile="PDF/X-4" '
        f'calligraphicPenFillColor="Black" calligraphicPenLineColor="Black" calligraphicPenFillColorShade="100" '
        f'calligraphicPenLineColorShade="100" calligraphicPenLineWidth="1" calligraphicPenAngle="0" '
        f'calligraphicPenWidth="10" calligraphicPenStyle="1">'
    )
    return "\n".join(header)

def checkprofile_pdf():
    # Ajout des CheckProfile
    profiles_code=[]
    check_profiles = [
        'PDF 1.3', 'PDF 1.4', 'PDF 1.5', 'PDF 1.6', 'PDF/X-1a', 'PDF/X-3', 'PDF/X-4', 'PostScript'
    ]
    for profile in check_profiles:
        profiles_code.append(f'        <CheckProfile Name="'+profile+'" ignoreErrors="0" '
                             f'autoCheck="1" '
                             f'checkGlyphs="1" '
                             f'checkOrphans="1" '
                             f'checkOverflow="1" '
                             f'checkPictures="1" '
                             f'checkPartFilledImageFrames="0" '
                             f'checkResolution="1" '
                             f'checkTransparency="1" '
                             f'minResolution="144" '
                             f'maxResolution="2400" '
                             f'checkAnnotations="0" '
                             f'checkRasterPDF="1" '
                             f'checkForGIF="1" '
                             f'ignoreOffLayers="0" '
                             f'checkNotCMYKOrSpot="0" '
                             f'checkDeviceColorsAndOutputIntent="1" '
                             f'checkFontNotEmbedded="1" '
                             f'checkFontIsOpenType="1" '
                             f'checkAppliedMasterDifferentSide="1" '
                             f'checkEmptyTextFrames="1"/>')

    return "\n".join(profiles_code)

def colors_document():
        # Ajout des couleurs et HYPHEN
    colors = [
        '        <COLOR NAME="Black" SPACE="CMYK" C="0" M="0" Y="0" K="100"/>',
        '        <COLOR NAME="Bleu" SPACE="CMYK" C="100" M="100" Y="0" K="0" Spot="1"/>',
        '        <COLOR NAME="Cyan" SPACE="CMYK" C="100" M="0" Y="0" K="0"/>',
        '        <COLOR NAME="Indigo" SPACE="CMYK" C="42" M="100" Y="0" K="49" Spot="1"/>',
        '        <COLOR NAME="Jaune or" SPACE="CMYK" C="0" M="16" Y="100" K="0" Spot="1"/>',
        '        <COLOR NAME="Jaune pale" SPACE="CMYK" C="0" M="0" Y="60" K="0" Spot="1"/>',
        '        <COLOR NAME="Magenta" SPACE="CMYK" C="0" M="80" Y="0" K="0" Spot="1"/>',
        '        <COLOR NAME="Marron" SPACE="CMYK" C="0" M="50" Y="100" K="41" Spot="1"/>',
        '        <COLOR NAME="Marron chocolat" SPACE="CMYK" C="0" M="61" Y="100" K="36" Spot="1"/>',
        '        <COLOR NAME="Marron rouge" SPACE="CMYK" C="0" M="75" Y="75" K="35" Spot="1"/>',
        '        <COLOR NAME="Marron-marron" SPACE="CMYK" C="0" M="100" Y="100" K="50" Spot="1"/>',
        '        <COLOR NAME="Orange Clair" SPACE="CMYK" C="0" M="40" Y="100" K="0" Spot="1"/>',
        '        <COLOR NAME="Orange foncé" SPACE="CMYK" C="0" M="60" Y="100" K="0" Spot="1"/>',
        '        <COLOR NAME="Registration" SPACE="CMYK" C="100" M="100" Y="100" K="100" Register="1"/>',
        '        <COLOR NAME="Rouge" SPACE="CMYK" C="0" M="100" Y="100" K="20" Spot="1"/>',
        '        <COLOR NAME="Vert" SPACE="CMYK" C="100" M="0" Y="100" K="0" Spot="1"/>',
        '        <COLOR NAME="Vert olive" SPACE="CMYK" C="0" M="0" Y="100" K="50" Spot="1"/>',
        '        <COLOR NAME="Violet" SPACE="CMYK" C="50" M="100" Y="0" K="0" Spot="1"/>',
        '        <COLOR NAME="Violet orchidée" SPACE="CMYK" C="12" M="59" Y="0" K="17" Spot="1"/>',
        '        <COLOR NAME="White" SPACE="CMYK" C="0" M="0" Y="0" K="0"/>',
        '        <HYPHEN/>'
    ]
    return "\n".join(colors)

def style_master_page():
        # Ajout Styles et autres éléments
    style = [
        '        <CHARSTYLE CNAME="Default Character Style" DefaultStyle="1" FONT="Arial Regular" FONTSIZE="12" FONTFEATURES="" FEATURES="inherit" FCOLOR="Black" FSHADE="100" HyphenWordMin="3" SCOLOR="Black" BGCOLOR="None" BGSHADE="100" SSHADE="100" TXTSHX="5" TXTSHY="-5" TXTOUT="1" TXTULP="-0.1" TXTULW="-0.1" TXTSTP="-0.1" TXTSTW="-0.1" SCALEH="100" SCALEV="100" BASEO="0" KERN="0" LANGUAGE="fr"/>',
        '        <STYLE NAME="Default Paragraph Style" DefaultStyle="1" ALIGN="0" DIRECTION="0" LINESPMode="0" LINESP="15" INDENT="0" RMARGIN="0" FIRST="0" VOR="0" NACH="0" ParagraphEffectOffset="0" DROP="0" DROPLIN="2" Bullet="0" Numeration="0" HyphenConsecutiveLines="2" BCOLOR="None" BSHADE="100"/>',
        '        <TableStyle NAME="Default Table Style" DefaultStyle="1" FillColor="None" FillShade="100">',
        '            <TableBorderLeft>',
        '                <TableBorderLine Width="1" PenStyle="1" Color="Black" Shade="100"/>',
        '            </TableBorderLeft>',
        '            <TableBorderRight>',
        '                <TableBorderLine Width="1" PenStyle="1" Color="Black" Shade="100"/>',
        '            </TableBorderRight>',
        '            <TableBorderTop>',
        '                <TableBorderLine Width="1" PenStyle="1" Color="Black" Shade="100"/>',
        '            </TableBorderTop>',
        '            <TableBorderBottom>',
        '                <TableBorderLine Width="1" PenStyle="1" Color="Black" Shade="100"/>',
        '            </TableBorderBottom>',
        '        </TableStyle>',
        '        <CellStyle NAME="Default Cell Style" DefaultStyle="1" FillColor="None" FillShade="100" LeftPadding="1" RightPadding="1" TopPadding="1" BottomPadding="1"/>',
        '        <LAYERS NUMMER="0" LEVEL="0" NAME="Fond de page" SICHTBAR="1" DRUCKEN="1" EDIT="1" SELECT="0" FLOW="1" TRANS="1" BLEND="0" OUTL="1" LAYERC="#000000"/>',
        '        <LAYERS NUMMER="1" LEVEL="1" NAME="CutContour" SICHTBAR="1" DRUCKEN="1" EDIT="1" SELECT="0" FLOW="1" TRANS="1" BLEND="0" OUTL="1" LAYERC="#ff0000"/>',
        '        <Printer firstUse="1" toFile="0" useAltPrintCommand="0" outputSeparations="0" useSpotColors="1" useColor="0" mirrorH="0" mirrorV="0" useICC="1" doGCR="0" doClip="0" setDevParam="0" useDocBleeds="1" cropMarks="1" bleedMarks="1" registrationMarks="0" colorMarks="0" includePDFMarks="1" PSLevel="3" PrintEngine="4" markLength="1" markOffset="0" BleedTop="6" BleedLeft="6" BleedRight="6" BleedBottom="6" printer="Canon TS9500 series" filename="" separationName="All" printerCommand=""/>',
        '        <PDF firstUse="1" Thumbnails="0" Articles="0" Bookmarks="0" Compress="1" CMethod="3" Quality="0" EmbedPDF="0" MirrorH="0" MirrorV="0" Clip="0" rangeSel="0" rangeTxt="" RotateDeg="0" PresentMode="0" RecalcPic="0" FontEmbedding="0" Grayscale="0" RGBMode="0" UseProfiles="0" UseProfiles2="1" Binding="0" PicRes="300" Resolution="300" Version="10" Intent="1" Intent2="0" SolidP="sRGB v3.0 (Canon)" ImageP="sRGB v3.0 (Canon)" PrintP="ISO Coated v2 300% (basICColor)" InfoString="" BTop="0" BLeft="0" BRight="0" BBottom="0" useDocBleeds="0" cropMarks="0" bleedMarks="0" registrationMarks="0" colorMarks="0" docInfoMarks="0" markLength="20" markOffset="0" ImagePr="0" PassOwner="" PassUser="" Permissions="-4" Encrypt="0" UseLayers="1" UseLpi="0" UseSpotColors="1" doMultiFile="0" displayBookmarks="0" displayFullscreen="0" displayLayers="0" displayThumbs="0" hideMenuBar="0" hideToolBar="0" fitWindow="0" openAfterExport="0" PageLayout="2" openAction="">',
        '            <Subset Name="Arial Bold"/>',
        '            <LPI Color="" Frequency="10" Angle="0" SpotFunction="0"/>',
        '            <LPI Color="Black" Frequency="133" Angle="45" SpotFunction="3"/>',
        '            <LPI Color="Cyan" Frequency="133" Angle="105" SpotFunction="3"/>',
        '            <LPI Color="Magenta" Frequency="133" Angle="75" SpotFunction="3"/>',
        '            <LPI Color="Yellow" Frequency="133" Angle="90" SpotFunction="3"/>',
        '        </PDF>'
    ]
    return "\n".join(style)

def init_document(page_width,page_height):
        # Ajout des blocs supplémentaires
    initdocument = [
        '        <DocItemAttributes/>',
        '        <Indexes/>',
        '        <TablesOfContents/>',
        '        <NotesStyles>',
        '            <notesStyle Name="Default" Start="1" Endnotes="0" Type="Type_1_2_3" Range="0" Prefix="" Suffix=")" AutoHeight="1" AutoWidth="1" AutoRemove="1" AutoWeld="1" SuperNote="1" SuperMaster="1" MarksStyle="" NotesStyle=""/>',
        '        </NotesStyles>',
        '        <OpticalMarginSets>',
        '            <Set Id="preset_0" Type="preset" Name="Default">',
        '                <Rules>',
        '                    <Rule Left="0" Right="0.5" Unit="7" Characters="U+003A,U+003B,U+2013,U+2033"/>',
        '                    <Rule Left="0" Right="0.75" Unit="7" Characters="U+002C,U+002D,U+002E,U+2010,U+2032"/>',
        '                    <Rule Left="0.25" Right="0.25" Unit="7" Characters="U+2014"/>',
        '                    <Rule Left="0.5" Right="0" Unit="7" Characters="U+2036"/>',
        '                    <Rule Left="0.5" Right="0.5" Unit="7" Characters="U+0022,U+0028,U+0029,U+005B,U+005D,U+00AB,U+00BB,U+201C,U+201D,U+201E,U+201F"/>',
        '                    <Rule Left="0.75" Right="0" Unit="7" Characters="U+2035"/>',
        '                    <Rule Left="0.75" Right="0.75" Unit="7" Characters="U+0027,U+002A,U+0060,U+007E,U+00B4,U+2018,U+2019,U+201A,U+201B,U+2039,U+203A"/>',
        '                </Rules>',
        '            </Set>',
        '        </OpticalMarginSets>',
        '        <PageSets>',
        '            <Set Name="Single Page" FirstPage="0" Rows="1" Columns="1"/>',
        '            <Set Name="Double Sided" FirstPage="0" Rows="1" Columns="2">',
        '                <PageNames Name="Left Page"/>',
        '                <PageNames Name="Right Page"/>',
        '            </Set>',
        '            <Set Name="3-Fold" FirstPage="0" Rows="1" Columns="3">',
        '                <PageNames Name="Left Page"/>',
        '                <PageNames Name="Middle"/>',
        '                <PageNames Name="Right Page"/>',
        '            </Set>',
        '            <Set Name="4-Fold" FirstPage="0" Rows="1" Columns="4">',
        '                <PageNames Name="Left Page"/>',
        '                <PageNames Name="Middle Left"/>',
        '                <PageNames Name="Middle Right"/>',
        '                <PageNames Name="Right Page"/>',
        '            </Set>',
        '        </PageSets>',
        '        <Sections>',
        '            <Section Number="0" Name="Section 1" From="0" To="5" Type="Type_1_2_3" Start="1" Reversed="0" Active="1" FillChar="0" FieldWidth="0"/>',
        '        </Sections>',
        '        <MASTERPAGE PAGEXPOS="1000" PAGEYPOS="500" PAGEWIDTH="'+f'{page_width}'+'" PAGEHEIGHT="'+f'{page_height}'+'" BORDERLEFT="9" BORDERRIGHT="9" BORDERTOP="9" BORDERBOTTOM="9" NUM="0" NAM="Normal gauche" MNAM="" Size="Custom" Orientation="1" LEFT="1" PRESET="0" VerticalGuides="" HorizontalGuides="" AGhorizontalAutoGap="0" AGverticalAutoGap="0" AGhorizontalAutoCount="0" AGverticalAutoCount="0" AGhorizontalAutoRefer="0" AGverticalAutoRefer="0" AGSelection="0 0 0 0" pageEffectDuration="1" pageViewDuration="1" effectType="0" Dm="0" M="0" Di="0"/>',
        '        <MASTERPAGE PAGEXPOS="1000" PAGEYPOS="500" PAGEWIDTH="'+f'{page_width}'+'" PAGEHEIGHT="'+f'{page_height}'+'" BORDERLEFT="9" BORDERRIGHT="9" BORDERTOP="9" BORDERBOTTOM="9" NUM="1" NAM="Normal droite" MNAM="" Size="Custom" Orientation="1" LEFT="0" PRESET="0" VerticalGuides="" HorizontalGuides="" AGhorizontalAutoGap="0" AGverticalAutoGap="0" AGhorizontalAutoCount="0" AGverticalAutoCount="0" AGhorizontalAutoRefer="0" AGverticalAutoRefer="0" AGSelection="0 0 0 0" pageEffectDuration="1" pageViewDuration="1" effectType="0" Dm="0" M="0" Di="0"/>'
    ]

    return "\n".join(initdocument)

def generate_footer():
    return "    </DOCUMENT>\n</SCRIBUSUTF8NEW>"

def generate_xml_from_syllables(syllables_with_colors, start_x, start_y, step_y, page_width, page_height):
    """
    syllables_with_colors : liste de syllabes où chaque syllabe est une liste de tuples (texte, couleur)
    Exemple :
    [
        [("AB", "Rouge"), ("I", "Magenta")],
        [("BO", "Bleu"), ("U", "Vert")]
    ]
    """
    xml_lines = []
    num = 0
    ypos = start_y

    # Génération des balises PAGE
    if len(syllables_with_colors)==0:
        nb_pages = 2
    else:
        nb_pages=len(syllables_with_colors)*2
    for i in range(0,nb_pages):
        xpos = start_x if i % 2 == 0 else start_x + 240
        mnam = "Normal gauche" if i % 2 == 0 else "Normal droite"

        xml_lines.append(
            f'        <PAGE PAGEXPOS="{xpos}" PAGEYPOS="{ypos}" PAGEWIDTH="{page_width}" PAGEHEIGHT="{page_height}" '
            f'BORDERLEFT="9" BORDERRIGHT="9" BORDERTOP="9" BORDERBOTTOM="9" NUM="{num}" NAM="" MNAM="{mnam}" '
            f'Size="Custom" Orientation="1" LEFT="0" PRESET="0" VerticalGuides="" HorizontalGuides="" '
            f'AGhorizontalAutoGap="0" AGverticalAutoGap="0" AGhorizontalAutoCount="0" AGverticalAutoCount="0" '
            f'AGhorizontalAutoRefer="0" AGverticalAutoRefer="0" AGSelection="0 0 0 0" pageEffectDuration="1" '
            f'pageViewDuration="1" effectType="0" Dm="0" M="0" Di="0"/>'
        )

        num += 1
        if i % 2 == 1:
            ypos += step_y

    # Réinitialisation pour PAGEOBJECT
    img = Image.open(r'TSAproject/verso.png')
    kwidth, kheight = img.size
    kdpi = img.info.get("dpi")
    kwidth=kwidth*72/kdpi[0]
    kheight=kheight*72/kdpi[1]
    kwidth=min(page_width/kwidth,page_height/kheight)
    num = 0
    ypos = start_y
    page_width = page_width-2
    page_height = page_height-2
    kheight=(page_height-kheight*kwidth)/2*28.44
    k_rayon = 15
    k_value=4/3*(math.sqrt(2)-1)
    k_arc = k_rayon*k_value
    xml_lines.append(f'        <MASTEROBJECT '
                     f'XPOS="{start_x+1}" '
                     f'YPOS="{start_y+1}" '
                     f'OwnPage="1" ItemID="1000" PTYPE="6" '
                     f'WIDTH="{page_width}" '
                     f'HEIGHT="{page_height}" '
                     f'RADRECT="14" FRTYPE="2" CLIPEDIT="0" PWIDTH="2" PCOLOR2="Black" PLINEART="1" ANNAME="CutContourVerso" '
                     f'path="M0 {k_rayon:.6g} '
                     f'C0 {k_rayon-k_arc:.6g} {k_rayon-k_arc:.6g} 0 {k_rayon:.6g} 0 '
                     f'L{page_width-k_rayon:.6g} 0 '
                     f'C{page_width-k_rayon+k_arc:.6g} 0 {page_width:.6g} {k_rayon-k_arc:.6g} {page_width:.6g} {k_rayon:.6g} '
                     f'L{page_width:.6g} {page_height-k_rayon:.6g} '
                     f'C{page_width:.6g} {page_height-k_rayon+k_arc:.6g} {page_width-k_rayon+k_arc:.6g} {page_height:.6g} {page_width-k_rayon:.6g} {page_height:.6g} '
                     f'L{k_rayon} {page_height:.6g} '
                     f'C{k_rayon-k_arc:.6g} {page_height:.6g} 0 {page_height-k_rayon+k_arc:.6g} 0 {page_height-k_rayon:.6g} '
                     f'L0 {k_rayon:.6g} Z" '
                     f'copath="M0 {k_rayon} '
                     f'C0 {k_rayon-k_arc:.6g} {k_rayon-k_arc:.6g} 0 {k_rayon:.6g} 0 '
                     f'L{page_width-k_rayon:.6g} 0 '
                     f'C{page_width-k_rayon+k_arc:.6g} 0 {page_width:.6g} {k_rayon-k_arc:.6g} {page_width:.6g} {k_rayon:.6g} '
                     f'L{page_width:.6g} {page_height-k_rayon:.6g} '
                     f'C{page_width:.6g} {page_height-k_rayon+k_arc:.6g} {page_width-k_rayon+k_arc:.6g} {page_height:.6g} {page_width-k_rayon:.6g} {page_height:.6g} '
                     f'L{k_rayon} {page_height:.6g} '
                     f'C{k_rayon-k_arc:.6g} {page_height:.6g} 0 {page_height-k_rayon+k_arc:.6g} 0 {page_height-k_rayon:.6g} '
                     f'L0 {k_rayon:.6g} Z" '
                     f'OnMasterPage="Normal droite" gXpos="34841" gYpos="501" gWidth="0" gHeight="0" LAYER="1"/>')
    xml_lines.append(f'        <MASTEROBJECT '
                     f'XPOS="{start_x}" '
                     f'YPOS="{start_y}" '
                     f'OwnPage="1" ItemID="1001" PTYPE="2" '
                     f'WIDTH="{page_width+2}" '
                     f'HEIGHT="{page_height+2}" '
                     f'FRTYPE="0" CLIPEDIT="0" PWIDTH="1" PLINEART="1" ANNAME="Verso" '
                     f'LOCALSCX="{kwidth:.6g}" LOCALSCY="{kwidth:.6g}" LOCALX="0" LOCALY="{kheight:.6g}" LOCALROT="0" PICART="1" SCALETYPE="0" RATIO="1" '
                     f'Pagenumber="0" PFILE="verso.png" PRFILE="sRGB v3.0 (Canon)" IRENDER="0" EMBEDDED="0" '
                     f'path="M0 0 '
                     f'L{page_width+2:.6g} 0 '
                     f'L{page_width+2:.6g} {page_height+2:.6g} '
                     f'L0 {page_height+2:.6g} '
                     f'L0 0 Z" '
                     f'copath="M0 0 '
                     f'L{page_width+2:.6g} 0 '
                     f'L{page_width+2:.6g} {page_height+2:.6g} '
                     f'L0 {page_height+2:.6g} '
                     f'L0 0 Z" '
                     f'OnMasterPage="Normal droite" ImageRes="2" gXpos="215080" gYpos="72250" gWidth="0" gHeight="0" LAYER="0" NEXTITEM="-1" BACKITEM="-1"/>')
    xml_lines.append(f'        <MASTEROBJECT '
                     f'XPOS="{start_x+1}" '
                     f'YPOS="{start_y+1}" '
                     f'OwnPage="0" ItemID="1002" PTYPE="6" '
                     f'WIDTH="{page_width}" '
                     f'HEIGHT="{page_height}" '
                     f'RADRECT="15" '
                     f'FRTYPE="2" CLIPEDIT="0" PWIDTH="2" PCOLOR2="Black" PLINEART="1" ANNAME="CutContourRecto" '
                     f'path="M0 {k_rayon:.6g} '
                     f'C0 {k_rayon-k_arc:.6g} {k_rayon-k_arc:.6g} 0 {k_rayon:.6g} 0 '
                     f'L{page_width-k_rayon:.6g} 0 '
                     f'C{page_width-k_rayon+k_arc:.6g} 0 {page_width:.6g} {k_rayon-k_arc:.6g} {page_width:.6g} {k_rayon:.6g} '
                     f'L{page_width:.6g} {page_height-k_rayon:.6g} '
                     f'C{page_width:.6g} {page_height-k_rayon+k_arc:.6g} {page_width-k_rayon+k_arc:.6g} {page_height:.6g} {page_width-k_rayon:.6g} {page_height:.6g} '
                     f'L{k_rayon} {page_height:.6g} '
                     f'C{k_rayon-k_arc:.6g} {page_height:.6g} 0 {page_height-k_rayon+k_arc:.6g} 0 {page_height-k_rayon:.6g} '
                     f'L0 {k_rayon:.6g} Z" '
                     f'copath="M0 {k_rayon} '
                     f'C0 {k_rayon-k_arc:.6g} {k_rayon-k_arc:.6g} 0 {k_rayon:.6g} 0 '
                     f'L{page_width-k_rayon:.6g} 0 '
                     f'C{page_width-k_rayon+k_arc:.6g} 0 {page_width:.6g} {k_rayon-k_arc:.6g} {page_width:.6g} {k_rayon:.6g} '
                     f'L{page_width:.6g} {page_height-k_rayon:.6g} '
                     f'C{page_width:.6g} {page_height-k_rayon+k_arc:.6g} {page_width-k_rayon+k_arc:.6g} {page_height:.6g} {page_width-k_rayon:.6g} {page_height:.6g} '
                     f'L{k_rayon} {page_height:.6g} '
                     f'C{k_rayon-k_arc:.6g} {page_height:.6g} 0 {page_height-k_rayon+k_arc:.6g} 0 {page_height-k_rayon:.6g} '
                     f'L0 {k_rayon:.6g} Z" '
                     f'OnMasterPage="Normal gauche" gXpos="1001" gYpos="501" gWidth="0" gHeight="0" LAYER="1"/>')
    # Génération des balises PAGEOBJECT avec texte coloré
    for i, segments in enumerate(syllables_with_colors):
        xpos = start_x
        syllable_text = "".join([seg[0] for seg in segments])  # concaténation des segments

        xml_lines.append(
            f'        <PAGEOBJECT XPOS="{xpos}" YPOS="{ypos}" OwnPage="{i*2}" ItemID="{10000000 + i}" PTYPE="4" WIDTH="{page_width}" HEIGHT="{page_height}" '
            f'FRTYPE="0" CLIPEDIT="0" PWIDTH="1" PLINEART="1" ANNAME="{syllable_text}" LOCALSCX="1" LOCALSCY="1" LOCALX="0" LOCALY="0" LOCALROT="0" '
            f'PICART="1" SCALETYPE="1" RATIO="1" COLUMNS="1" COLGAP="0" AUTOTEXT="0" EXTRA="0" TEXTRA="0" BEXTRA="0" REXTRA="0" VAlign="1" FLOP="1" '
            f'PLTSHOW="0" BASEOF="0" textPathType="0" textPathFlipped="0" path="M0 0 L{page_width} 0 L{page_width} {page_height} L0 {page_height} L0 0 Z" '
            f'copath="M0 0 L{page_width} 0 L{page_width} {page_height} L0 {page_height} L0 0 Z" gXpos="{xpos}" gYpos="{ypos}" gWidth="0" gHeight="0" '
            f'LAYER="0" NEXTITEM="-1" BACKITEM="-1">'
        )
        xml_lines.append('            <StoryText>')
        xml_lines.append('                <DefaultStyle FONT="Arial Bold" FCOLOR="Registration" FSHADE="100"/>')

        # Ajout des segments colorés
        for text, color in segments:
            xml_lines.append(f'                <ITEXT FONT="Arial Bold" FONTSIZE="48" FCOLOR="{color}" FSHADE="100" CH="{text}"/>')

        xml_lines.append('                <trail ALIGN="1" LINESPMode="1" LINESP="1"/>')
        xml_lines.append('            </StoryText>')
        xml_lines.append('        </PAGEOBJECT>')

        num += 1
        ypos += step_y

    return "\n".join(xml_lines)