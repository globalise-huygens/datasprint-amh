# GLOBALISE AMH Datasprint

Materials for the GLOBALISE datasprint on places in the Indian Ocean world.

| :warning: | A more recent version of the 4.VEL map data can be found in this GLOBALISE [`maps`](https://github.com/globalise-huygens/maps) repository. |
| :-------: | :----------------------------------------------------------------------------------------------------------------------------------------- |

- [GLOBALISE AMH Datasprint](#globalise-amh-datasprint)
  - [Introduction](#introduction)
  - [Collections](#collections)
  - [Aggregations](#aggregations)
  - [Scripts](#scripts)
  - [About](#about)

## Introduction

Historical places are important building blocks for the reconstruction of historical events. The GLOBALISE corpus of about 5 million pages from the VOC archives describes hundreds of thousands of events that took place over a period of two centuries in a large number of locations spread over a huge area around the Indian Ocean and Indonesian archipelago. Thanks to initiatives like the [_Atlas of Mutual Heritage_](https://www.atlasofmutualheritage.nl/) and the [_World Historical Gazetteer_](https://whgazetteer.org/), we can locate some of the places mentioned, but by no means all of them. Within GLOBALISE, we would like to bring as much of these locations to light as possible by creating a dataset that identifies and geolocates historical places mentioned in our texts. This is challenging, as disambiguation of spelling variations is not always easy, place names appear in different languages, change over time, and sources present ambiguous references to locations.

This datasprint aims to foster collaboration between historians, heritage professionals and data scientists for better availability of data on historical places. It intends to curate, publish, and link data on historical places collected by researchers within their own projects, as well as test and improve digital techniques to extract, structure, and share data on places. In addition to data creation, curation, and linking, this datasprint will offer a space to exchange knowledge and expertise on historical places and contexts, and digital techniques. We hope that by the end of the datasprint, all participants will have learned something, and that we will have generated valuable data on historical locations with which to improve our understanding of the early modern Indian Ocean and Indonesian archipelago worlds.

## Collections

These IIIF Collections can be found in the [`manifests`](manifests) folder. The URLs below point to a [Mirador3 viewer](https://globalise-huygens.github.io/datasprint-amh/) with the respective collection loaded.

- [4.VEL Entire collection](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests/B.3.1.json)
  - B Zee-, kust- en rivierkaarten
    - [B.3 Azië](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests/B.3.json)
      - [B.3.1 Roode Zee en Perzische Golf](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests/B.3.1.json)
      - [B.3.2 Decan, Kanara](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests/B.3.2.json)
      - [B.3.3 Malabar](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests/B.3.3.json)
      - [B.3.4 Ceylon](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests/B.3.4.json)
      - [B.3.5 Coromandel](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests/B.3.5.json)
      - [B.3.6 Bengalen](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests/B.3.6.json)
      - [B.3.7 Schiereiland Malakka](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests/B.3.7.json)
      - [B.3.8 Siam, Cambodja](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests/B.3.8.json)
      - [B.3.9 Quinam, Tonquin, Cochin-China](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests/B.3.9.json)
      - [B.3.10 China, Japan](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests/B.3.10.json)
      - [B.3.11 Chineesche Zee](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests/B.3.11.json)
      - [B.3.12 Eilanden in de Chineesche Zee](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests/B.3.12.json)
      - [B.3.13 Philippijnsche Eilanden](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests/B.3.13.json)
      - [B.3.14 Mindanao](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests/B.3.14.json)
      - [B.3.15 Pescadores](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests/B.3.15.json)
      - [B.3.16 Formosa](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests/B.3.16.json)
      - [B.3.17 Prata Shoal](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests/B.3.17.json)
      - [B.3.18 Indische Oceaan](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests/B.3.18.json)
      - [B.3.19 Eilanden in de Indische Oceaan](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests/B.3.19.json)
      - [B.3.20 Indische Archipel](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests/B.3.20.json)
  - C Landkaarten, plans, enz.
    - [C.2 Azië](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests/B.2.json)
      - [C.2.1 Algemeen](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests//C.2.1.json)
      - [C.2.2 Perzische Golf](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests//C.2.2.json)
      - [C.2.3 Gujarat](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests//C.2.3.json)
      - [C.2.4 Malabar](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests//C.2.4.json)
      - [C.2.5 Ceylon](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests//C.2.5.json)
      - [C.2.6 Coromandel](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests//C.2.6.json)
      - [C.2.7 Bengalen](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests//C.2.7.json)
      - [C.2.8 Malakka](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests//C.2.8.json)
      - [C.2.9 China](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests//C.2.9.json)
      - [C.2.10 Japan](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests//C.2.10.json)
      - [C.2.11 Formosa](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests//C.2.11.json)
      - [C.2.12 Indische Zee](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests//C.2.12.json)
      - [C.2.13 Indische Archipel](https://globalise-huygens.github.io/datasprint-amh/#data:text/x-url,https://globalise-huygens.github.io/datasprint-amh/manifests//C.2.13.json)

## Aggregations

To bridge between the image itself, the IIIF Collections and Manifests, and the structured metdata of the Atlas of Mutual Heritage, the Atlas's data is modelled in the Europeana Data Model as RDF. The Manifests then link to the structured RDF data using the `rdfs:seeAlso` property, and the map links to the Manifest using the `dcterms:isReferencedBy` property. An example of this data (coming from [aggregations/4.VEL/297.json](aggregations/4.VEL/297.json)):

```json
{
  "@context": "https://globalise-huygens.github.io/datasprint-amh/context.json",
  "id": "https://globalise-huygens.github.io/datasprint-amh/aggregations/4.VEL/297.json",
  "type": "ore:Aggregation",
  "edm:aggregatedCHO": {
    "id": "http://hdl.handle.net/10648/ad12d7d6-3531-4cb7-8a24-50d3e0b41633",
    "type": ["edm:ProvidedCHO", "schema:Map"],
    "image": "https://www.atlasofmutualheritage.nl/image/2022/4/21/vel0297.jpg%28mediaclass-meta-tag-image.4b190bfcc55e159332679890b17bd2261ced7954%29.jpg",
    "dc:title": "Plattegrond van het kasteel St.Jago te Manilha",
    "dc:description": "Titel in catalogus Leupe (Nationaal Archief): Platte grond van het Kasteel St.Jago en de Stadt Manilha.\nNotities verso: Behoort by de overgekomen brieven en papieren van Batavia 4e deel 1704, N1 / 2106 [folionummer in de band ?].",
    "dc:type": "tekening",
    "dc:identifier": "VEL0297",
    "dc:subject": ["gebouw", "plattegrond / kaart", "vesting"],
    "dc:language": "nl",
    "dcterms:medium": "papier",
    "edmfp:technique": "ingekleurde tekening",
    "dcterms:extent": "41,5 x 54,5 cm",
    "dcterms:date": "1680-1704",
    "dcterms:provenance": "Nationaal Archief",
    "dcterms:isPartOf": "Atlas of Mutual Heritage",
    "seeAlso": "https://www.atlasofmutualheritage.nl/page/7863/plattegrond-van-het-kasteel-st.jago-te-manilha"
  },
  "edm:isShownBy": {
    "id": "https://service.archief.nl/iip/96/98/8a/b6/17/f4/42/0f/97/b9/eb/ce/9f/aa/28/65/7b0fecf8-26da-4bb6-8fd6-73cef3002bd5.jp2/full/full/0/default.jpg",
    "type": "edm:WebResource",
    "svcs:has_service": {
      "id": "https://service.archief.nl/iip/96/98/8a/b6/17/f4/42/0f/97/b9/eb/ce/9f/aa/28/65/7b0fecf8-26da-4bb6-8fd6-73cef3002bd5.jp2",
      "type": "svcs:Service",
      "profile": "http://iiif.io/api/image",
      "implements": "http://iiif.io/api/image/2/level1.json"
    },
    "rights": "https://creativecommons.org/publicdomain/mark/1.0/",
    "isReferencedBy": {
      "id": "https://globalise-huygens.github.io/datasprint-amh/manifests/4.VEL/297.json",
      "type": "iiif:Manifest",
      "rdfs:label": "Platte grond van het Kasteel St. Jago en de Stadt Manilha."
    }
  },
  "edm:dataProvider": "Rijksdienst voor het Cultureel Erfgoed",
  "edm:provider": "Nationaal Archief",
  "edm:rights": "https://creativecommons.org/publicdomain/mark/1.0/"
}
```

An RDF dump of all the aggregations (in text/turtle) can be found in the [rdf](rdf) folder.

## Scripts

- `inventory2handle_title_date.py`: Used to create a mapping between the inventory number and the title and date of the map. Data stored as JSON.
- `inventory2hierarchy.py`: Used to create a mapping between the inventory number and the hierarchy of the map (its archival (sub)series and file structure). Data stored as JSON.
- `make_manifest_v3.py`: Used to create IIIF Manifests (v3) for the maps. Also outputs ore:Aggregations and EDM RDF. Data stored as JSON-LD.
- `make_manifest_v2.py`: Used to create IIIF Manifests (v2) for the maps, for use in Recogito.
- `jsonld2ttl.py`: Used to convert the JSON-LD output of `make_manifest_v3.py` to text/turtle RDF (as a dump instead of individual files).

## About

The scripts and data in this repository were created for the GLOBALISE and [CREATE](https://create.humanities.uva.nl/) datasprint in spring 2023. A blog post is written about the sprint's results: https://globalise.huygens.knaw.nl/old-maps-new-discoveries-a-datasprints-digital-exploration/.

See https://globalise.huygens.knaw.nl/ for more information about the project.
