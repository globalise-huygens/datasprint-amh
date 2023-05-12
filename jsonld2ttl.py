import os
import json
from rdflib import ConjunctiveGraph

folder_name = "aggregations/4.VEL/"

# List of input JSON-LD files
input_files = os.listdir(folder_name)

# Create an empty rdflib graph
g = ConjunctiveGraph()

# Loop through input files
for f in input_files:
    # Open the file and load the JSON-LD data
    with open(os.path.join(folder_name, f)) as f:
        data = json.load(f)

    # Parse the JSON-LD data and add it to the rdflib graph
    g.parse(data=json.dumps(data), format="json-ld")

# Write the rdflib graph to a Turtle file
g.serialize(destination="rdf/aggregations.ttl", format="turtle")
