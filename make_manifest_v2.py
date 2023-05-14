"""
Generate two IIIF v2 manifests for the 4.VEL Asia collection to be used in Recogito.
"""

import json
from iiif_prezi.factory import ManifestFactory

IIIF_BASE_URL = "https://service.archief.nl/iipsrv?IIIF="

# Define our Manifest factory
fac = ManifestFactory()
fac.set_base_prezi_uri(
    "https://globalise-huygens.github.io/datasprint-amh/manifests/4.VEL/v2/"
)
fac.set_base_image_uri(IIIF_BASE_URL)
# fac.set_base_prezi_dir("./")
fac.set_iiif_image_info(2.0, 2)  # Version, ComplianceLevel
# fac.set_debug("warn")


def main():
    # Read in the V3 Collections
    for jsonfile in ["B.3.json", "C.2.json"]:
        with open("manifests/" + jsonfile) as f:
            data = json.load(f)

        # Get every manifest in the collection
        manifests = []
        for manifest in data["items"]:
            id = manifest["id"].split("/manifests/")[1]
            manifests.append(id)

        # Combine the canvases into a single list
        canvases = []
        for manifest in manifests:
            with open("manifests/" + manifest) as f:
                data = json.load(f)
            canvases += data["items"]

        # Extract the label + service (all we need)
        labels_handles_services = []
        for canvas in canvases:
            label = canvas["label"]["nl"][0].strip()

            for meta in canvas["metadata"]:
                if meta["label"]["nl"][0] == "Permalink":
                    handle = meta["value"]["en"][0]
                    break

            service = canvas["items"][0]["items"][0]["body"]["service"][0]["@id"]

            labels_handles_services.append((label, handle, service))

        # Create the manifest
        manifest = make_manifest_v2(labels_handles_services, jsonfile)

        # And save it
        with open("manifests/4.VEL/v2/" + jsonfile, "w") as f:
            manifest_json = manifest.toJSON(top=True)
            manifest_json["@id"] = manifest_json["@id"].replace(
                "manifest.json", jsonfile
            )

            json.dump(manifest_json, f, indent=4)


def make_manifest_v2(data, jsonfile):
    # Create the manifest itself with basic metadata
    manifest = fac.manifest(label=jsonfile.replace(".json", ""))
    manifest.viewingDirection = "left-to-right"

    # And then the canvases in a sequence
    seq = manifest.sequence()

    for n, (label, handle, service) in enumerate(data, 1):
        print(f"Processing {n}/{len(data)}\t{label}...")
        cvs = seq.canvas(
            ident=f"https://globalise-huygens.github.io/datasprint-amh/manifests/4.VEL/v2/{jsonfile}/canvas/p{n}",
            label=label,
        )
        cvs.set_image_annotation(imgid=service.replace(IIIF_BASE_URL, ""), iiif=True)

        cvs.set_metadata({"Permalink": handle})

    return manifest


if __name__ == "__main__":
    main()
