# TAROT
##  Silly web service for Tarot readings


The title says all.

Based on the Rider-Waite-Smith framework, but includes information related to the Ordo Templi Orientis framework as well.

Information extracted from various books and resources found online .

With basic web templates that include images of either fantastic decks : [Anima Mundi](https://www.kickstarter.com/projects/128820172/the-anima-mundi-tarot-deck) _(for RWS)_ or [Tabula Mundi](http://www.tabulamundi.com/home/) _for OTO_ .

*Available in English and Spanish (Castellano)*

*Translation of Spanish:*

```
Pentacles   -> Oros
Swords      -> Espadas
Wands       -> Bastos
Cups        -> Copas
Knight      -> Caballo
Page        -> Sota
Queen       -> Reina
King        -> Rey

0 The Fool      -> El Loco
1 The Magician  -> El Mago
2 The High Priestess -> La Sacerdotisa
3 The Empress   -> La Emperatriz
3 The Emperor   -> El Emperador
5 The Hierophant -> El Sumo Sarcedote
6 The Lovers    -> Los Enamorados
7 The Chariot   -> El Carro
8 Justice       -> La Justicia
9 The Hermit    -> El Hermitaño
10 The Wheel of Fortune -> La Rueda de la Fortuna
11 Strength     -> La Fuerza
12 The Hanged Man -> El Colgado
13 Death        -> La Muerte
14 Temperance   -> La Templanza
15 The Devil    -> El Diablo
16 The Tower    -> La Torre
17 The Star     -> La Estrella
18 The Moon     -> La Luna
19 The Sun      -> El Sol
20 Judgement    -> El Juicio
21 The World    -> El Mundo
```

### REST Endpoints

_For the Spanish version, just add the prefix "es" after the "/"_

_Return the details of the specified symbol including its picture_

```
GET /{:symbol}/{:name|:number}
```

_Cast a reading where spread (integer) is some of my favourite spreads._
```
GET /{:spread_id}
```

### Tech stack

- [Sinatra](https://sinatrarb.com/intro.html)
- [MongoDB](https://www.mongodb.com)