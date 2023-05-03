import os
import json
import xml.etree.ElementTree as ET


def get_inventory2handle_title_date(xmlfile, destination):
    inventory2handle = dict()
    inventory2title = dict()
    inventory2date = dict()

    tree = ET.parse(xmlfile)
    dids = tree.findall(".//c[@level='file']/did")

    for did in dids:
        inventorynumber_el = did.find("unitid[@type='ABS']")
        if inventorynumber_el is not None:
            inventorynumber = inventorynumber_el.text
        else:
            inventorynumber = ""

        permalink = did.find("unitid[@type='handle']").text
        inventory2handle[inventorynumber] = permalink

        title = "".join(did.find("unittitle").itertext())
        inventory2title[inventorynumber] = title

        date_el = did.find("unitdate")
        if date_el is not None:
            date = date_el.attrib.get("normal", date_el.attrib.get("text"))
        else:
            date = ""

        inventory2date[inventorynumber] = date

    with open(os.path.join(destination, "inventory2handle.json"), "w") as outfile:
        json.dump(inventory2handle, outfile, indent=2)

    with open(os.path.join(destination, "inventory2title.json"), "w") as outfile:
        json.dump(inventory2title, outfile, indent=2)

    with open(os.path.join(destination, "inventory2date.json"), "w") as outfile:
        json.dump(inventory2date, outfile, indent=2)


if __name__ == "__main__":
    get_inventory2handle_title_date(xmlfile="data/4.VEL.xml", destination="data/")
