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

# For the hierarchy and collections

with open("data/series2files.json") as infile:
    series2files = json.load(infile)

with open("data/series2title.json") as infile:
    series2title = json.load(infile)

# Manifest store

code2manifest = {}


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
    collection_content: list,
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
                value={
                    "en": [
                        f'<a href="{collection_permalink}">{collection_permalink}</a>'
                    ]
                },
            ),
        ],
    )

    manifests = []
    for n, i in enumerate(collection_content, 1):
        print(f"Processing {n}/{len(collection_content)}", end="\r")
        if type(i) == dict:
            inventory_number, inventory_content = list(i.items())[0]
        else:
            inventory_number = i
            inventory_content = [i]

        if inventory_content:
            manifest = make_manifest(
                inventory_number,
                inventory_content,
                collection_number,
                metadata_file,
                base_url,
            )
        else:
            manifest = None

        if manifest:
            manifests.append(manifest)
            collection.add_item(manifest)

            code2manifest[inventory_number] = manifest

    with open(collection_filename, "w") as outfile:
        outfile.write(collection.json(indent=4))

    return collection


def make_manifest(
    inventory_number: str,
    inventory_content: list,
    collection_number: str,
    metadata_file: str,
    base_url: str,
    license_id: str = "https://creativecommons.org/publicdomain/mark/1.0/",
) -> iiif_prezi3.Manifest:
    manifest_filename = f"manifests/{collection_number}/{inventory_number}.json"
    manifest_filename = manifest_filename.replace(", ", "+")
    manifest_id = base_url + manifest_filename

    aggregations = []
    titles = []
    handles = []
    dates = []
    iiif_services = []
    for c in inventory_content:
        if c not in metadata_file:
            print(f"\nSkipping {c}")
            return

        metadata = metadata_file[c]

        aggregation_filename = f"aggregations/{collection_number}/{c}.json"
        aggregation_id = base_url + aggregation_filename

        handle = inventory2handle[c]
        iiif_service = inventory2info[c].replace("/info.json", "")
        title = inventory2title[c]
        date = inventory2date[c]

        titles.append(title)
        handles.append(handle)
        dates.append(date)
        iiif_services.append(iiif_service)

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
        aggregations.append(ore_aggregation)

    amh_metadata_blobs = []
    for a in aggregations:
        amh_metadata_title = a["edm:aggregatedCHO"]["dc:title"]
        amh_metadata_description = (
            a["edm:aggregatedCHO"].get("dc:description", "").replace("\n", "<br>")
        )
        amh_metadata_url = a["edm:aggregatedCHO"]["seeAlso"]
        amh_metadata_blob = f"""
        <strong>Title</strong>: {amh_metadata_title}<br>
        <strong>Description</strong>: {amh_metadata_description}<br>
        <strong>URL</strong>: <a href="{amh_metadata_url}">{amh_metadata_url}</a>
        """
        amh_metadata_blobs.append(amh_metadata_blob)

    manifest = iiif_prezi3.Manifest(
        id=manifest_id,
        label=series2title.get(inventory_number, title),
        metadata=[
            iiif_prezi3.KeyValueString(
                label="Identifier",
                value={"en": [inventory_number]},
            ),
            iiif_prezi3.KeyValueString(
                label="Date",
                value={"en": [date or "?" for date in dates]},
            ),
            iiif_prezi3.KeyValueString(
                label="Permalink",
                value={
                    "en": [f'<a href="{handle}">{handle}</a>' for handle in handles]
                },
            ),
            iiif_prezi3.KeyValueString(
                label="Metadata from the Atlas of Mutual Heritage",
                value={
                    "en": [
                        amh_metadata_blob for amh_metadata_blob in amh_metadata_blobs
                    ]
                },
            ),
        ],
        seeAlso=[ore_aggregation],
        rights=license_id,
    )

    c_titles_handles_dates_services_amh = zip(
        inventory_content, titles, handles, dates, iiif_services, amh_metadata_blobs
    )

    for n, (c, title, handle, date, iiif_service, amh) in enumerate(
        c_titles_handles_dates_services_amh, 1
    ):
        try:
            canvas = manifest.make_canvas_from_iiif(
                url=iiif_service,
                id=f"{manifest_id}/canvas/p{n}",
                label=title,
                anno_id=f"{manifest_id}/canvas/p{n}/anno",
                anno_page_id=f"{manifest_id}/canvas/p{n}/annotationpage",
                metadata=[
                    iiif_prezi3.KeyValueString(
                        label="Identifier",
                        value={"en": [c]},
                    ),
                    iiif_prezi3.KeyValueString(
                        label="Date",
                        value={"en": [date or "?"]},
                    ),
                    iiif_prezi3.KeyValueString(
                        label="Permalink",
                        value={"en": [f'<a href="{handle}">{handle}</a>']},
                    ),
                    iiif_prezi3.KeyValueString(
                        label="Metadata from the Atlas of Mutual Heritage",
                        value={"en": [amh]},
                    ),
                ],
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
    # First, the main collection with everything
    collection_content = series2files[collection_number]

    collection = make_collection(
        collection_number,
        collection_label,
        collection_permalink,
        collection_content,
        metadata_file,
        base_url,
    )

    # Then, the subcollections
    for collection_code, collection_content in series2files.items():
        if collection_code == collection_number:
            continue
        elif "B.3" not in collection_code:  # Asia only (and first level) for now
            continue

        collection_title = series2title[collection_code]

        collection_filename = f"manifests/{collection_code}.json"
        collection_filename = collection_filename.replace(" ", "_")
        collection_id = base_url + collection_filename

        manifests = []
        for c in collection_content:
            if type(c) == dict:
                c = list(c.keys())[0]

            if c in code2manifest:
                manifests.append(code2manifest[c])

        collection = iiif_prezi3.Collection(
            id=collection_id,
            label=collection_title,
            metadata=[
                iiif_prezi3.KeyValueString(
                    label="Identifier",
                    value={"en": [collection_code]},
                ),
            ],
        )

        for m in manifests:
            collection.add_item(m)

        with open(collection_filename, "w") as outfile:
            outfile.write(collection.json(indent=4))


if __name__ == "__main__":
    main(
        metadata_file=metadata_VEL,
        collection_number="4.VEL",
        collection_label="Inventaris van de verzameling buitenlandse kaarten Leupe, 1584-1813 (1865)",
        collection_permalink="http://hdl.handle.net/10648/2baed20f-8a3e-4ae7-b8f8-cd9d9fa88646",
        base_url="https://globalise-huygens.github.io/datasprint-amh/",
    )
