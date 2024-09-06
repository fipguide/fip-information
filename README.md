# FIP Information

(Logo hier einfügen)

## Table of Contents

- [English](#english)
- [Deutsch](#deutsch)

## English

This repository provides the data foundation for the [FIPGuide](INSERT LINK HERE). Everyone is welcome to help make the information clearer, update it, or add new information.
An overview of the repository’s data structure and how information can be contributed can be found in the [Wiki](INSERT LINK HERE).

## Deutsch

Dieses Repository bildet die Datengrundlage für den [FIPGuide](LINK HIER EINFÜGEN). Jeder ist willkommen Informationen besser verständlich zu machen, zu aktualisieren oder neue hinzuzufügen.
Ein Überblick über die Datenstruktur des Repositorys und wie Informationen beigetragen werden können ist im [Wiki](LINK HIER EINFÜGEN) zu finden.

#######################################
Abschitt für spätere Wikiseiten
#######################################

Deutsch

# Datenstruktur

## Ordnerstruktur

Die Dateien sind nach folgender Ordnerstruktur aufgebaut

```bash
information
├── companies [^1]
│   └── <company X> [^2]
│       ├── <company X>.png [^3]
│       ├── <company X>_<lang>.md [^4]
│       ├── <company X>_<lang>.json [^5]
│       └── images [^6]
│           ├── <image 1>
│           └── <image 2>
├── countries [^7]
│   ├── index_<lang>.json [^8]
│   └── <country A> [^9]
│       ├── <country A>.png [^10]
│       ├── <country A>.json [^11]
│       ├── information_<lang>.md [^12]
│       └── images [^13]
│           ├── <image 3>
│           └── <image 4>
└── general [^14]
    ├── generalFipGuides_<lang>.md [^15]
    └── generalTravelGuides_<lang>.md [^16]
```

[^1]: Ordner für Informationen über Bahngesellschaften
[^2]: Eine bestimmte Bahngesellschaft z.B. DB, SNCF oder PKP
[^3]: Das Logo der Bahngesellschaft als PNG Datei
[^4]: Der Informationstext über die Bahngesellschaft pro Sprache. Infos zur Datei unter [Dateiformate](#bahngesellschaft-informationen)
[^5]: Metadaten für die Bahngesellschaft pro Sprache. Infos zur Datei unter [Dateiformate](#bahngesellschaft-metadaten)
[^6]: Ordner für Bilder die auf der Seite der Bahngesellschaft angezeigt werden soll
[^7]: Ordner für Informationen über Länder.
[^8]: Metadaten über die Länder pro Sprache. Notwendig zur Generierung des Menüs im FIPGuide. Infos zur Datei unter [Dateiformate](#länder-index)
[^9]: Ein bestimmtes Land z.B. Deutschland, Frankreich oder Polen.
[^10]: Die Flagge des Landes in 72x72 Pixel PNG Datei. Zur Zeit wird [twemoji](https://github.com/twitter/twemoji) genutzt.
[^11]: Metadaten für das Land. Notwendig zum Anzeigen der dazugehörigen Bahngesellschaften. Infos zur Datei unter [Dateiformate](#land-metadaten)
[^12]: Der Informationstext über das Land pro Sprache. Infos zur Datei unter [Dateiformate](#land-informationen)
[^13]: Ordner für Bilder die auf der Seite des Landes angezeigt werden sollen
[^14]: Ordner für allgemeine Informationen auf der Seite des FIPGuides
[^15]: Allgemeine Informationen über das Reisen mit FIP
[^16]: Allgemeine Informationen zum Zugfahren in Europa

## Dateiformate

Genaue technische Schemas der JSON Dateien sind [im Frontend Repository](https://github.com/fipguide/frontend/tree/main/src/assets/json/schemas) zu finden.

### Bahngesellschaft Informationen

Die Datei `information/companies/<company>/<company>_<lang>.md` enthält Informationen zur jeweiligen Bahngesellschaft.

Folgende Überschriften erkannt und mit dem passenden Text pro Sprache dargestellt:

- `generellInformation`
- `reservations`
- `validityOfFipTickets`
- `summaryOfParticularities`
- `trainCategories`
- `ticketPurchase`
- `arrivals`
- `borders`
- `reducedTickets`
- `specialTariffRules`

Angegebene Informationen sollten soweit möglich mit Quellen hinterlegt werden. Dazu kann eine Fußnote erstellt werden.

```bash
Information.[^1]

[^1]: Quelle
```

### Bahngesellschaft Metadaten

Die Datei `information/companies/<company>/<company>_<lang>.json` enthält Metadaten die zum Anzeigen der Bahngesellschaft des Landes angegeben werden.

- `name: string` der geläufigste Name der Bahngesellschaft in der jeweiligen Sprache
- `abbreviation: string` die Abkürzung der Bahngesellschaft
- `authors: string[]` eine Liste der Autoren der Informationen der Bahngesellschaft
- `created: "YYYY-MM-DD"` Datum der Erstellung
- `edited: "YYYY-MM-DD"` Datum der letzten Aktualisierung

### Länder Index

Die Datei `information/countries/index_<lang>.json` enthält Metadaten die zum Anzeigen der Länder im Menü in der jeweiligen Sprache notwendig sind.
Eine Liste aus Objekten die jeweils besteht aus:

- `name: string` der Name des Landes in der jeweiligen Sprache
- `path: string` der Pfad zu Informationen des Landes

### Land Metadaten

Die Datei `information/countries/<country>/<country>_<lang>.json` enthält Metadaten die zum Anzeigen der passenden Bahngesellschaften des Landes angegeben werden.
Sie besteht aus:

- `insideEu: boolean` gibt an, ob das Land Mitglied der europäischen Union ist
- `fipCompanys: string[]` eine Liste der Bahngesellschaften des Landes die FIP akzeptieren. In der Liste muss der Pfad der Bahngesellschaft angegeben werden.
- `nonFipCompanies: string[]` eine Liste der Unternehmen, die kein FIP akzeptieren.

### Land Informationen

TOBECREATED

#########################################

Englisch

# Data structure

## Folder structure

Die Dateien sind nach folgender Ordnerstruktur aufgebaut

```bash
information
├── companies [^1]
│   └── <company X> [^2]
│       ├── <company X>.png [^3]
│       ├── <company X>_<lang>.md [^4]
│       ├── <company X>_<lang>.json [^5]
│       └── images [^6]
│           ├── <image 1>
│           └── <image 2>
├── countries [^7]
│   ├── index_<lang>.json [^8]
│   └── <country A> [^9]
│       ├── <country A>.png [^10]
│       ├── <country A>.json [^11]
│       ├── information_<lang>.md [^12]
│       └── images [^13]
│           ├── <image 3>
│           └── <image 4>
└── general [^14]
    ├── generalFipGuides_<lang>.md [^15]
    └── generalTravelGuides_<lang>.md [^16]
```

[^1]: Folder for information about railway companies
[^2]: A specific railway company, e.g., DB, SNCF, or PKP
[^3]: The logo of the railway company as a PNG file
[^4]: The informational text about the railway company in each language. Info about the file can be found under [File formats](#railway-company-informationen)
[^5]: Metadata for the railway company in each language. Info about the file can be found under [File formats](#railway-company-metadata)
[^6]: Folder for images to be displayed on the railway company’s page
[^7]: Folder for information about countries
[^8]: Metadata about the countries in each language. Necessary for generating the menu in the FIPGuide. Info about the file can be found under [File formats](#countries-index)
[^9]: A specific country, e.g., Germany, France, or Poland
[^10]: The country’s flag in a 72x72 pixel PNG file. Currently [twemoji](https://github.com/twitter/twemoji) is being used
[^11]: Metadata for the country. Necessary for displaying the associated railway companies. Info about the file can be found unde [File formats](#country-metadata)
[^12]: The informational text about the country in each language. Info about the file can be found under [File formats](#country-information)
[^13]: Folder for images to be displayed on the country’s page
[^14]: Folder for general information on the FIPGuide page
[^15]: General information about traveling with FIP
[^16]: General information about train travel in Europe

## File formats

The detailed technical schemas of the JSON files can be found [in the frontend repository](https://github.com/fipguide/frontend/tree/main/src/assets/json/schemas).

### Railway company informationen

The file `information/companies/<company>/<company>_<lang>.md` contains information about the respective railway company.

The following headings are recognized and displayed with the appropriate text in each language:

- `generalInformation`
- `reservations`
- `validityOfFipTickets`
- `summaryOfParticularities`
- `trainCategories`
- `ticketPurchase`
- `arrivals`
- `borders`
- `reducedTickets`
- `specialTariffRules`

Information provided should be accompanied by sources where possible. A footnote can be created for this purpose.

```bash
Information.[^1]

[^1]: Source
```

### Railway company metadata

The file `information/companies/<company>/<company>_<lang>.json` contains metadata used to display the railway company for the country.

- `name: string` the most common name of the railway company in the respective language
- `abbreviation: string` the abbreviation of the railway company
- `authors: string[]` a list of the authors of the railway company information
- `created: "YYYY-MM-DD"` date of creation
- `edited: "YYYY-MM-DD"` date of last update

### Countries index

The file `information/countries/index_<lang>.json` contains metadata necessary for displaying countries in the menu in the respective language. It consists of a list of objects, each containing:

- `name: string` the name of the country in the respective language
- `path: string` the path to information about the country

### Country metadata

The file `information/countries/<country>/<country>_<lang>.json` contains metadata used to display the relevant railway companies for the country. It consists of:

- `insideEu: boolean` indicates whether the country is a member of the European Union
- `fipCompanies: string[]` a list of the country's railway companies that accept FIP. The list must include the path to the railway company.
- `nonFipCompanies: string[]` a list of companies that do not accept FIP.

### Country information

TOBECREATED
