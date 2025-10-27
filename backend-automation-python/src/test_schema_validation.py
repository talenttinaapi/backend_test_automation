import json
import os
from jsonschema import validate
from src.api_client import get_all_countries

def test_schema_validation():
    response = get_all_countries()
    schema_path = os.path.join(os.path.dirname(__file__), "schema.json")
    with open(schema_path, "r") as schema_file:
        schema = json.load(schema_file)
    validate(instance=response, schema=schema)
