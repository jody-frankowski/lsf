# Langue des Signes

LSF ? DSGS ? lsf suisse ?

Python > access

why signsuisse? because it's the website with the best quality.

Variantes de "Maman":
- http://lsf.wikisign.org/wiki/Maman
- https://signsuisse.sgb-fss.ch/fr/lexikon/g/maman/
- https://dico.elix-lsf.fr/dictionnaire/maman/n.f.-185867

## Learning Order

Words only first > words + sentences with all words known > words + more sentences ?
since the 2 second case seems to have only a few candidates, it might work for
only a little while, and we should jump on the other technique after.
Words only first > words + sentences with words unknown > words + more sentences ?

One full deck + one deck by week? TODO Test full deck order.
/!\ How to change learning path while not breaking existing ones on Anki?

Grammar >> Practice/examples should be best. Examples imply knowing all the
words in the phrase?
The following might depend entirely on the available examples on signsuisse!
Rationale: From most to least useful
Missing: Common rules, like negation/questions...
Order:
Week 1:
- Salutations
- Alphabet (the sooner, the more links the student can do with other signs eg.
  soeur/bleu)
- Name Yourself
- Who am I? Who are you?
- Pronoms
- Mal/Entendant/Sourd/LSF
- Be aware of where your hands and fingers are, and where they come from and go
  to. (BP)
- Interrogative (can be learned from the examples? are there any questions on
  signsuisse?)

Week X;
- Formules Politesses
- Oui/Non
- Describe objects ? No cards for those yet!
- Quantities (Un peu/Beaucoup)
- Numbers >> Age

Week X:
- Expressions interrogatives ?
- Sentiments
- Parce que/pour/afin que/peut etre/Ou
- Vouloir/Avoir/Savoir/Ne pas avoir
- Bien/Bon/Mal/Mauvais

Week X:
- Expressions interrogatives
- Adjectifs Possessifs
- Family
- Describe family link

Week X:
- Where I live. (before what i do because the vocabulary is much more common for
  everyone)
- Buildings/Places
- Movements
- Transports

Week X:
- Weather
- Temps/Jours

Week X:
- Jobs
- What I do
- What my family does

Week X:
- Other activities: Eating/Sleeping/Playing/Partying/Evening Activities

Goal at that point: Being able to describe a typical day of your life

Week X:
- Colors
- Animals >> Colors ? (not that useful)
- Nature
- Where animals live?

LAST: How to learn an unknown sign?

Vocab target: 600 Words?
Examples: Less than 600 because not all words have examples!

Source:
What about the alphabet?
The numbers >> signsuisse has some!

Learning path >> json ?
```
day 1:
    word* to learn. link to data json? if yes how?
    example* to learn. link to data json? if yes how?
    best practice* ?
    explanation*
    exercise*

day X:
    word*
    examples*


[
    {
        day: 0,
        [
            word1,
            ...
        ],
        [
            example1,
            ...
        ]
    },
    ...
]
```

## Website scrap

signsuisse:
urls examples:
- https://signsuisse.sgb-fss.ch/fr/lexikon/g/test-1/ (it)
- https://signsuisse.sgb-fss.ch/fr/lexikon/g/test-2/ (blank)
- https://signsuisse.sgb-fss.ch/fr/lexikon/g/test-3/ (fr)
Errors:
- https://signsuisse.sgb-fss.ch/fr/lexikon/g/test-3/ : `Catégorie: ,En général`
- https://signsuisse.sgb-fss.ch/fr/lexikon/g/ancien-testament/ : `Catégorie: ,Religion`
- https://signsuisse.sgb-fss.ch/index.php\?id\=32\&tx_issignsuisselexikon_anzeige\[action\]\=ajaxsearch\&tx_issignsuisselexikon_anzeige\[controller\]\=Gebaerden\&type\=6666\&tx_issignsuisselexikon_anzeige\[stufe\]\=1\&tx_issignsuisselexikon_anzeige\[categories\]\=10000\&L\=1 SQL error

Two ways to crawl:
- `https://signsuisse.sgb-fss.ch/index.php?id=32&tx_issignsuisselexikon_anzeige[action]=ajaxsearch&tx_issignsuisselexikon_anzeige[controller]=Gebaerden&type=6666&tx_issignsuisselexikon_anzeige[stufe]=2&tx_issignsuisselexikon_anzeige[categories]=6876&L=1`
- `https://signsuisse.sgb-fss.ch/index.php?id=32&tx_issignsuisselexikon_anzeige[action]=ajaxsearch&tx_issignsuisselexikon_anzeige[controller]=Gebaerden&type=6666&tx_issignsuisselexikon_anzeige[stufe]=2&tx_issignsuisselexikon_anzeige[categories]=[00000-10000|6000-7000]&L=1` >> text/plain >> r.html.links works
- `https://signsuisse.sgb-fss.ch/fr/index.php?eID=signsuisse_search&sword=[aa-zz]&lang=[fr|de|it]&curlang=fr` >> application/json >> r.html.links doesn't work

```
for url in seed_urls:
    crawl(url)

# global? eww?
seen_urls = []

crawl(url):
    content = fetch(url)
    crawl_result[url] = {data...}
    for url in content.urls:
        if url not in seen_urls:
            seen_urls += url
            if base_domain(url) in allowed_domains:
                crawl(url)
```



## Steps

Crawl json:
```
{
ID:
    START_DATE:
    END_DATE:
    COMPLETED_DATE: NEVER|DATE
    URL:
    {
        START_DATE: NEVER|DATE ?
        END_DATE: TIMEOUT|DATE ?
        ERROR:
        HTTP_CODE:
        HTTP_HEADERS:
        EXTERNAL_URLS:
        INTERNAL_URLS:
    }
}
```

```
# Ugly ?
def extract_urls(response):
    if r.headers['Content-Type'] == "application/json":
        if signsuisse:
            extract(keys=link)
    else:
        r.html.absolute_links
    return []
```

Crawl
- Use the index and the two ajax calls as seed calls
- Store urls in big json
- Archive all urls on archive.org and archive.is

- Get as much of the old words in the db as possible
- Check that all fields are working and fix them if needed
- Fill the remaining ones manually
- Create a "learning" json which links to the real one? link to words and examples?
- Link both words and examples

## TODO

Show illustration or photo when video offline? (signsuisse doesn't always have one)
Add fetch/scrap date, maybe even video/text hash?
Add archive.is
Add https://signsuisse.sgb-fss.ch/fr/lexikon/g/alphabet/
Add turtle mode

Test extract_urls(response)

What about homonymes:
- https://signsuisse.sgb-fss.ch/fr/lexikon/g/frais-1/
- https://signsuisse.sgb-fss.ch/fr/lexikon/g/frais-2/
- https://signsuisse.sgb-fss.ch/fr/lexikon/g/frais-3/

What about hints? (eg. soeur > S)

Choose a license. One that forbids commercial use?

LSF Video explaining
Donate button
Contributions welcome for other sign languages

Disclaimer: Not a teacher. Open to suggestions. Open an issue to tell me if bad
or good, what worked or what didn't.

Delete wip branch on gh/gl

Global cards viewer? Useful when you are searching a particular sign video.

Check https://blog.fluent-forever.com/base-vocabulary-list/

## Old Words

```
@
A (alpha.)
Abeille
Absent (n.m.)
Accord (n.m.)
Adolescent (n.m.)
Adorer (v.)
Adulte 1
Âge
Aimer (v.)
Aller (n.m.)
Allumer (v.)
Animal - bête
Animaux
Application
Apprendre
Après-demain
Après-midi (n.m.)
Arbre
Arc-en-ciel
Argenté (adj.)
Arrêter (v.)
Arrière-grand-mère (n.f.)
Arrière-grand-père (n.m.)
Artiste (n.m.)
Attendre (v.)
Aujourd’hui (adv.)
Au revoir
Autobus -trolleybus - bus
Automobile - voiture
Avant-hier
Avion (n.m.)
Avoir (v.)
Baleine
B (alpha.)
Bateau (n.m.)
Beaucoup
Beau-fils (n.m.)
Beau-frère (n.m.)
Beau-père (n.m.)
Bébé (n.m.)
Beige (n.m.)
Belle-fille (n.f.)
belle-mère
Bien
Bière (n.f.)
Blanc (adj.)
Bleu
Boeuf
Boire 1
Bonjour (n.m.)
Bon (n.m.)
Bonsoir
Branche (substantif)
Briquet (n.m.)
Café (n.m.)
C (alpha.)
Camion
Campagne 1
Canard
Carré (n.m.)
cent
Cercle
Chance (substantif)
Chat
Chercher (v.)
Chien
Ciel
cinquante
Clair (adj.)
Cochon
Colère (n.f.)
Colline
Combien (adv.)
Comment
Commerçant (n.m.)
Comprendre (v.)
Content (adj.)
Couleur (n.f.)
Couleurs
Courir (v.)
Cousin (n.m.)
Cube (n.m.)
D (alpha.)
Dauphin
Demain
Demi-frère (n.m.)
De rien
Descendre (v.)
Désert
Dessiner (v.)
Détester (v.)
deux
deux cents
Dimanche (n.m.)
dix
Dommage (adj.)
Dormir (v.)
Dossier
Dur
E (alpha.)
éclair (n.m.)
Éléphant
email
énerver (v.)
Enfant (n.)
Enfin (adv.)
En forme (adj.)
Entendant
Épouse
Escargot
Éteindre (v.)
étonner (v.)
Étudier
Eux
Expressions interrogatives
Faire
Falaise
F (alpha.)
Famille
Famille
Fatiguer (v.)
Femme 1
Feuille d'arbre
Feuille (n.f.)
Fille 1
Fils (n.m.)
Fleur
Forêt
Formules de politesses
Frère (n.m.)
Froid (adj.)
Fusée (n.f.)
G (alpha.)
Garçon (n.m.)
Gare
Gentil
Girafe
Gorille
Grand-mère (n.f.)
Grand-père (n.m.)
Grenouille
Gris (n.m.)
Gronder (v.)
Guêpe
Habiter (v.)
H (alpha.)
Hélicoptère (n.m.)
Herbe
Heureux
Hier
Homme
I (alpha.)
Ici (adv.)
Île (substantif)
Informatique
Informatique
Internet
Interprète (n.)
J (alpha.)
Jaune (n.m.)
Jeudi (n.m.)
Jouer
Jour (n.m.)
K (alpha.)
Là-bas (adv.)
L (alpha.)
Lapin
Lieux
Ligne
Linux (n.)
Lion
Lire (v.)
Livre
Loup
LSF
Lui
Lundi (n.m.)
Lyon
Maison (n.f.)
Mal
Malade (adj.)
Malentendant
Malheureux (adj.)
Malin
M (alpha.)
Manger (v.)
Marcher 1
Mardi (n.m.)
Mari
Marron
Matin (n.m.)
médecin généraliste
Mer
Merci ! (int.)
Mercredi (substantif)
Mère (n.f.)
Météo
Métro
Midi
mille
Moi
Mon (dét.)
Montagne
Monter (v.)
Moto (n.f.)
Moustique (n.m.)
mouton
Naître
N (alpha.)
Nature
Nature
Neige
Neiger
Ne pas avoir
Ne pas savoir
Neveu (n.m.)
Noir (n.m.)
Nombres
Non (adv.)
Nous
Nuage (n.m.)
Nuit (n.f.)
O (alpha.)
Oiseau
Oncle (n.m.)
onze
Orangé (adj.)
Ordinateur
Ordinateur portable - laptop
Orthophoniste (n.m.)
Où
Ou (cnj.)
Oui (adv.)
Ours
P (alpha.)
Parce que (cnj.)
Pardon (n.m.)
Pareil (adv.)
Parents (substantif)
Paris
Parler
Pause (n.f.)
Père (substantif)
Peur (substantif)
Peut-être (adv.)
Pluie (substantif)
Plume
Poisson
Port
Portable (substantif)
Poubelle (n.f.)
Pour/afin que
Pourquoi
Pour quoi faire
Problème 1
Professeur
programmation informatique
Pronoms
Pyramide (n.f.)
Q (alpha.)
Quand
quarante
quatre-vingt
quatre-vingt-dix
Que faire
Qui
Quoi
R (alpha.)
Réfléchir (v.)
Regarder 1
Rejoindre
requin
Rêver (v.)
Rivière
Rocher (n.m.)
Rose 1
Rouge (n.m.)
Sable
S (alpha.)
Salut
Samedi (n.m.)
Sapin (n.m.)
S’appeler (v.)
Savoir 2
seize
Semaine (n.f.)
S’ennuyer (v.)
Sentiment (n.m.)
Sérieux
Signer [lsf] (verbe)
S'il vous plaît - s'il te plaît - svp - stp
Singe
six
Skateboard (n.m.)
Soeur (n.)
Soirée (n.f.)
soixante
soixante-dix
Soleil (n.prop.)
Sombre (adj.)
Son (dét.)
Sortir
Sourd
Sphère (n.f.)
T (alpha.)
Tante (n.f.)
Taxi (n.m.)
Temps/Jours
TGV (n.m.)
Thé (n.m.)
Toi
Ton (adj.)
Train (n.m.)
Tramway (n.m.)
Transport
Transports
Travail (n.m.)
trente
Triangle (n.m.)
Tricher
Triste
Trottinette (n.f.)
Trouver (verbe)
Tube (n.m.)
U (alpha.)
un
Un peu
Vache
Vallée
V (alpha.)
Vélo (n.m.)
Vendredi (n.m.)
Vert (n.m.)
Vexer
Vif (adj.)
Ville
Villes
Vin
vingt
vingt-et-un
Violet (n.m.)
Voir (v.)
Vouloir (v.)
Vous 1
Vous 2
X (alpha.)
Y (alpha.)
Z (alpha.)
```
