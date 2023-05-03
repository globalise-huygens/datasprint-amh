import os
import json
import iiif_prezi3
from rdflib import Namespace

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

# Namespaces
BASE_URL = Namespace("https://globalise-huygens.github.io/datasprint-amh/")

# Config
collection_number = "4.VEL"
collection_filename = f"manifests/{collection_number}.json"
collection_id = BASE_URL.term(collection_filename)

os.makedirs(f"manifests/{collection_number}", exist_ok=True)
iiif_prezi3.config.configs["helpers.auto_fields.AutoLang"].auto_lang = "nl"

# Collection
collection = iiif_prezi3.Collection(id=collection_id)
collection.label = {"en": ["Leupe Collection"]}

# Manifest
for inventory_number, metadata in metadata_VEL[:1]:
    manifest_filename = f"manifests/{collection_number}/{inventory_number}.json"
    manifest_id = BASE_URL.term(manifest_filename)

    handle = inventory2handle[inventory_number]
    info_json = inventory2info[inventory_number].replace("/info.json", "")
    title = inventory2title[inventory_number]
    date = inventory2date[inventory_number]

    manifest = iiif_prezi3.Manifest(label=title, id=manifest_id)
    canvas = manifest.make_canvas_from_iiif(
        url=info_json,
        id=f"{manifest_id}#canvas/p1",
        anno_id=f"{manifest_id}#canvas/p1/anno",
        anno_page_id=f"{manifest_id}#canvas/p1/annotationpage",
    )

    collection.add_item(manifest)  # Just a ref!

    with open(manifest_filename, "w") as outfile:
        outfile.write(manifest.json(indent=2))

with open(collection_filename, "w") as outfile:
    outfile.write(collection.json(indent=2))

if __name__ == "__main__":
    pass
