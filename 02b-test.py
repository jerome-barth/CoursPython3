## Test : affichage des résultats
from IPython.display import display, HTML
def affiche_tableau(data):
    tableau = "<center><table><tr>"
    for key, value in sorted(data.items()):tableau += "<th style='text-align:center'>"+key+"</th>\n"
    tableau += "</tr>"
    for index in range(len(list(data.items())[0][1])):
        tableau += "<tr>"
        for key, value in sorted(data.items()):tableau += "<td style='text-align:center'>"+str(value[index])+"</td>"
        tableau += "</tr>"
    tableau +="</table></center>"
    display(HTML(tableau))
donnees = {
    'a':[3, 3, 6, 2, 7, 8],
    'b':[3, 4, 6, 3, 2, 8],
    'c':[5, 5, 6, 4, 7, 1]}
resultats = {
    'isocèle':['?']*6, 'rectangle':['?']*6,
    'équilatéral':['?']*6, 'quelconque':['?']*6}
check = '✓'
for index in range(len(donnees['a'])):
    iso  = est_isocele(donnees['a'][index], donnees['b'][index], donnees['c'][index])
    equi = est_equilateral(donnees['a'][index], donnees['b'][index], donnees['c'][index])
    rect = est_rectangle(donnees['a'][index], donnees['b'][index], donnees['c'][index])
    qcq  = est_quelconque(donnees['a'][index], donnees['b'][index], donnees['c'][index])
    if iso  != None: resultats['isocèle'][index] = check if iso else " "
    if equi != None: resultats['équilatéral'][index] = check if equi else " "
    if rect != None: resultats['rectangle'][index] = check if rect else " "
    if qcq  != None: resultats['quelconque'][index] = check if qcq else " "
affiche_tableau({**donnees, **resultats})

## Test : validation des résultats
attendus = {
    'isocèle':[check, ' ', check, ' ', check, check],
    'rectangle':[' ', check, ' ', ' ', ' ', ' '],
    'équilatéral':[' ', ' ', check, ' ', ' ', ' '],
    'quelconque' :[' ', ' ', ' ', check, ' ', ' ']}
if resultats == attendus:
    print("OK c'est valide !")
else:
    print("Il y a au moins une erreur, les résultats attendus sont :")
    affiche_tableau({**donnees, **attendus})