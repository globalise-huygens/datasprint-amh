import os
import json
from lxml import etree as ET

from collections import defaultdict

# Globals
series2title = dict()
series2files = defaultdict(list)


def main(xmlfile, destination, collection_name=""):
    if collection_name:
        series2files[collection_name] = []  # template, first key

    tree = ET.parse(xmlfile)
    series_els = tree.findall(".//c[@level='series']")

    for series_el in series_els:
        series_code = series_el.find("did/unitid[@type='series_code']").text
        series_title = series_el.find("did/unittitle").text

        series2title[series_code] = series_title

        # Subseries
        subseries_els = series_el.findall("c[@level='subseries']")

        for subseries_el in subseries_els:
            get_subseries(subseries_el, series_code, collection_name)

    with open(os.path.join(destination, "series2title.json"), "w") as outfile:
        json.dump(series2title, outfile, indent=4)

    with open(os.path.join(destination, "series2files.json"), "w") as outfile:
        json.dump(series2files, outfile, indent=4)


def get_subseries(subseries_el, series_code, collection_name=""):
    subseries_code_el = subseries_el.find("did/unitid[@type='series_code']")
    subseries_title = "".join(subseries_el.find("did/unittitle").itertext()).strip()
    if subseries_code_el is not None:
        subseries_code = subseries_code_el.text
    else:
        subseries_code = subseries_title

    series2title[subseries_code] = subseries_title

    # # Only Asia
    # if "B.3" not in subseries_code:
    #     return

    subseries_els = subseries_el.findall("c[@level='subseries']")
    for subseries_el in subseries_els:
        get_subseries(subseries_el, series_code, collection_name)

    file_and_filegrp_els = subseries_el.xpath(
        "c[@level='file']|c[@otherlevel='filegrp']"
    )
    for el in file_and_filegrp_els:
        if el.get("level") == "file":
            file_code = get_file(el)

            if file_code:
                series2files[series_code].append(file_code)
                series2files[subseries_code].append(file_code)

                if collection_name:
                    series2files[collection_name].append(file_code)

        elif el.get("otherlevel") == "filegrp":
            filegrp_code = el.find("did/unitid").text
            filegrp_title = "".join(el.find("did/unittitle").itertext()).strip()

            series2title[filegrp_code] = filegrp_title

            filegrp_stack = {filegrp_code: []}
            file_els = el.findall("c[@level='file']")
            for file_el in file_els:
                file_code = get_file(file_el)
                filegrp_stack[filegrp_code].append(file_code)

            series2files[series_code].append(filegrp_stack)
            series2files[subseries_code].append(filegrp_stack)

            if collection_name:
                series2files[collection_name].append(filegrp_stack)


def get_file(file_el):
    did = file_el.find("did")
    inventorynumber_el = did.find("unitid[@type='ABS']")
    if inventorynumber_el is not None:
        inventorynumber = inventorynumber_el.text
    else:
        inventorynumber = ""

    return inventorynumber


if __name__ == "__main__":
    main(xmlfile="data/4.VEL.xml", destination="data/", collection_name="4.VEL")
