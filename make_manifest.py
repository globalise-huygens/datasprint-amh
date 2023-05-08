import os
import json
import iiif_prezi3
from requests.exceptions import HTTPError

with open("data/inventory2info.json", "r") as infile:
    inventory2info = json.load(infile)

with open("data/inventory2handle.json", "r") as infile:
    inventory2handle = json.load(infile)

with open("data/inventory2title.json", "r") as infile:
    inventory2title = json.load(infile)

with open("data/inventory2date.json", "r") as infile:
    inventory2date = json.load(infile)

with open("data/4.VEL_metadata.json") as infile:
    metadata_VEL = json.load(infile)


def get_rdf(
    cho_id: str,
    aggregation_filename: str,
    aggregation_id: str,
    metadata: dict,
    iiif_service: str,
    manifest_id: str,
    manifest_label: str,
    license_id: str,
    base_url: str,
) -> dict:
    iiif_default_url = iiif_service + "/full/full/0/default.jpg"  # IIIF2

    cho = {
        "id": cho_id,
        "type": ["edm:ProvidedCHO", "schema:Map"],
        "image": metadata["og:image"],
        "schema:text": metadata.get("inscription"),
        "dc:title": metadata["og:title"],
        "dc:description": "\n".join(metadata["comments"]),
        "dc:type": metadata.get("kind"),
        "dc:identifier": metadata["number"],
        "dc:subject": metadata.get("tags"),
        "dc:language": "nl",
        "dcterms:medium": metadata["material"],
        "edmfp:technique": metadata.get("technique"),
        "dcterms:extent": metadata.get("dimension"),
        "dcterms:date": metadata.get("period"),
        "dcterms:provenance": "Nationaal Archief",
        "dcterms:isPartOf": "Atlas of Mutual Heritage",
        "seeAlso": metadata["og:url"].replace("/nl/page/", "/page/"),
    }
    cho = {k: v for k, v in cho.items() if v}

    webResource = {
        "id": iiif_default_url,
        "type": "edm:WebResource",
        "svcs:has_service": {
            "id": iiif_service,
            "type": "svcs:Service",
            "profile": "http://iiif.io/api/image",
            "implements": "http://iiif.io/api/image/2/level1.json",  # Original says "http://iiif.io/api/image/2/level1"?
        },
        "rights": license_id,
        "isReferencedBy": {
            "id": manifest_id,
            "type": "iiif:Manifest",
            "rdfs:label": manifest_label,
        },
    }

    aggregation = {
        "@context": base_url + "context.json",
        "id": aggregation_id,
        "type": "ore:Aggregation",
        "edm:aggregatedCHO": cho,
        "edm:isShownBy": webResource,
        "edm:dataProvider": "Rijksdienst voor het Cultureel Erfgoed",
        "edm:provider": "Nationaal Archief",
        "edm:rights": license_id,
    }

    with open(aggregation_filename, "w") as outfile:
        json.dump(aggregation, outfile, indent=4)

    return aggregation


def make_collection(
    collection_number: str,
    collection_label: str,
    collection_permalink: str,
    metadata_file: str,
    base_url: str,
    language: str = "nl",
) -> iiif_prezi3.Collection:
    collection_filename = f"manifests/{collection_number}.json"
    collection_id = base_url + collection_filename

    os.makedirs(f"manifests/{collection_number}", exist_ok=True)
    os.makedirs(f"aggregations/{collection_number}", exist_ok=True)

    iiif_prezi3.config.configs["helpers.auto_fields.AutoLang"].auto_lang = language

    collection = iiif_prezi3.Collection(
        id=collection_id,
        label=collection_label,
        metadata=[
            iiif_prezi3.KeyValueString(
                label="Identifier",
                value={"en": [collection_number]},
            ),
            iiif_prezi3.KeyValueString(
                label="Permalink",
                value={"en": [f'<a href="{collection_permalink}"></a>']},
            ),
        ],
    )

    manifests = []
    for n, (inventory_number, metadata) in enumerate(metadata_file, 1):
        print(f"Processing {n}/{len(metadata_file)}", end="\r")

        manifest = make_manifest(
            inventory_number,
            collection_number,
            metadata,
            base_url,
        )
        manifests.append(manifest)
        collection.add_item(manifest)

    with open(collection_filename, "w") as outfile:
        outfile.write(collection.json(indent=4))

    return collection


def make_manifest(
    inventory_number: str,
    collection_number: str,
    metadata: dict,
    base_url: str,
    license_id: str = "https://creativecommons.org/publicdomain/mark/1.0/",
) -> iiif_prezi3.Manifest:
    manifest_filename = f"manifests/{collection_number}/{inventory_number}.json"
    manifest_id = base_url + manifest_filename

    aggregation_filename = f"aggregations/{collection_number}/{inventory_number}.json"
    aggregation_id = base_url + aggregation_filename

    handle = inventory2handle[inventory_number]
    iiif_service = inventory2info[inventory_number].replace("/info.json", "")
    title = inventory2title[inventory_number]
    date = inventory2date[inventory_number]

    ore_aggregation = get_rdf(
        cho_id=handle,
        aggregation_filename=aggregation_filename,
        aggregation_id=aggregation_id,
        metadata=metadata,
        iiif_service=iiif_service,
        manifest_id=manifest_id,
        manifest_label=title,
        license_id=license_id,
        base_url=base_url,
    )

    amh_metadata_title = ore_aggregation["edm:aggregatedCHO"]["dc:title"]
    amh_metadata_description = ore_aggregation["edm:aggregatedCHO"][
        "dc:description"
    ].replace("\n", "<br>")
    amh_metadata_url = ore_aggregation["edm:aggregatedCHO"]["seeAlso"]
    amh_metadata_blob = f"""
    <strong>Title</strong>: {amh_metadata_title}<br>
    <strong>Description</strong>: {amh_metadata_description}<br>
    <strong>URL</strong>: <a href="{amh_metadata_url}">{amh_metadata_url}</a>
    """

    manifest = iiif_prezi3.Manifest(
        id=manifest_id,
        label=title,
        metadata=[
            iiif_prezi3.KeyValueString(
                label="Identifier",
                value={"en": [inventory_number]},
            ),
            iiif_prezi3.KeyValueString(
                label="Date",
                value={"en": [date or "?"]},
            ),
            iiif_prezi3.KeyValueString(
                label="Permalink",
                value={"en": [f'<a href="{handle}"></a>']},
            ),
            iiif_prezi3.KeyValueString(
                label="Metadata from the Atlas of Mutual Heritage",
                value={"en": [amh_metadata_blob]},
            ),
        ],
        seeAlso=[ore_aggregation],
        rights=license_id,
    )
    try:
        canvas = manifest.make_canvas_from_iiif(
            url=iiif_service,
            id=f"{manifest_id}/canvas/p1",
            anno_id=f"{manifest_id}/canvas/p1/anno",
            anno_page_id=f"{manifest_id}/canvas/p1/annotationpage",
        )
    except HTTPError:
        pass

    with open(manifest_filename, "w") as outfile:
        outfile.write(manifest.json(indent=4))

    return manifest


def main(
    metadata_file: str,
    collection_number: str,
    collection_label: str,
    collection_permalink: str,
    base_url: str,
) -> None:
    collection = make_collection(
        collection_number,
        collection_label,
        collection_permalink,
        metadata_file,
        base_url,
    )


if __name__ == "__main__":
    main(
        metadata_file=metadata_VEL,
        collection_number="4.VEL",
        collection_label="Inventaris van de verzameling buitenlandse kaarten Leupe, 1584-1813 (1865)",
        collection_permalink="http://hdl.handle.net/10648/2baed20f-8a3e-4ae7-b8f8-cd9d9fa88646",
        base_url="https://globalise-huygens.github.io/datasprint-amh/",
    )
