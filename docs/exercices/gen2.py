import os, re
import sys

NB_DOSS = 40

lst = ['{:02d}'.format(k) for k in range(1, NB_DOSS+1)]

def create_doss():
    for nom in lst:
        os.makedirs(nom + '_1', exist_ok = True)
        os.makedirs(nom + '_2', exist_ok = True)

def fichier(nom_doss):
    nom_file = nom_doss + '/' + 'enonce.md'
    with open(nom_file, 'w') as f:
        f.write("")
        
    nom_file = nom_doss + '/' + 'correction.md'
    with open(nom_file, 'w') as f:
        f.write("")

def fichiers_1_2():
    for nom_doss in lst:
        n1 = nom_doss + '_1'
        n2 = nom_doss + '_2'
        fichier(n1)
        fichier(n2)


#create_doss()
#fichiers_1_2()




# contenu = """
# ### Exercice {0}.1 □
# !!! example "Exercice {0}.1"
#     === "Énoncé" 
#         --8<-- "docs/T6_6_Epreuve_pratique/files/{0}_1/enonce.md"
# 
#     === "Correction"
#         --8<-- "docs/T6_6_Epreuve_pratique/files/{0}_1/correction.md"
# 
#     === "Source Markdown"
#             --8<-- "docs/T6_6_Epreuve_pratique/files/{0}_1/enonce.md"
# 
# 
# ### Exercice {0}.2 □
# !!! example "Exercice {0}.2"
#     === "Énoncé" 
#         --8<-- "docs/T6_6_Epreuve_pratique/files/{0}_2/enonce.md"
# 
#     === "Correction"
#         --8<-- "docs/T6_6_Epreuve_pratique/files/{0}_2/correction.md"
# 
#     === "Sources Markdown"
#         ```md
#         --8<-- "docs/T6_6_Epreuve_pratique/files/{0}_2/enonce.md"
#         ```             
#         """

contenu = """
--8<-- "./docs/exercices/{0}/{1}/sujet_formate.md"

"""
ide = """
```python
    --8<-- "./docs/exercices/{0}/{1}/exo.py"
```
"""
exclude = """
search:
    - exclude: True"""
for root, dirs, lst_files in os.walk('.') :
    for file in lst_files :
        if file == 'sujet.md' :
            print('traitenent de {0}/{1}'.format(root, file))
            with open(os.path.join(root,file), 'r') as f:
                data = ''.join(f.readlines())
                
            titre = re.search('title: (?P<title>.*)', data).group('title')
            regex = re.compile(r'exclude: True', re.MULTILINE)
            if regex.search(data) == None :
                regex = re.compile(r'title:.*', re.MULTILINE)
                titre = regex.search(data).group()
                data2 = regex.sub(titre + exclude, data)
                with open(os.path.join(root,file), 'w') as f:
                    f.write(data2)
            titre = re.search('title: (?P<title>.*)', data).group('title')
            regex = re.compile(r'---(\n|.)*---$', re.MULTILINE)
            data = regex.sub('', data)
            regex = re.compile(r"{{ py_sujet.*}}", re.MULTILINE)
            data = regex.sub('', data)
            regex = re.compile(r"{{ IDE.*}}", re.MULTILINE)
            rep = root.split('/')
            data = regex.sub(ide.format(rep[-2], rep[-1]), data)
            regex = re.compile(r']\(images/', re.MULTILINE)
            data = regex.sub(']({0}/images/'.format(rep[-1]), data)  
            with open(os.path.join(root, 'sujet_formate.md'), 'w') as f :
                f.write("\n\n### {0} \n\n".format(titre))
                f.write(data)
            
                 
     
for rep in os.listdir() :    
    if os.path.isdir(rep) :
        with open('./{0}/exos.md'.format(rep), 'w') as f :
            for ss_rep in os.listdir('./'+rep) :
                f.write(contenu.format(rep, ss_rep))
           



# nom_dossier = 'listes_logins'
# nom_sources = "sources"
# os.makedirs(nom_dossier, exist_ok = True)
# os.makedirs(nom_sources, exist_ok = True)
# for file in os.scandir(nom_dossier):
#     os.remove(file.path)
# 
# 
# 
# 
# for classe in classes:
#     print(classe)
#     nomhtml = nom_sources + '/' + classe + '.html'
#     with open(nomhtml, 'w') as f:
#         f.write(html_start)
#         f.write('<h1> ' + classe + ' - logins Scribe </h1>')
#         f.write(tabdf[classe].to_html(index=False))
#         f.write(html_end)
#     nom_fichier = nom_dossier + '/' + classe + '.pdf'
#     pdf.from_file(nomhtml, nom_fichier)
#     os.remove(nomhtml)
# os.rmdir(nom_sources)
# print("Terminé")
