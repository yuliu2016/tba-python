import json

swagger_file = open("api_v3.json")
json_data = swagger_file.read()
swagger_file.close()

data = json.loads(json_data)

api_version = data["info"]["version"]

model_schemas = data["components"]["schemas"]

header = """from typing import *

V = TypeVar("V")

class Alliances(NamedTuple, Generic[V]):
    blue: V
    red: V"""

template = """
class {clz}(NamedTuple):{class_description}
    data: dict{fields}"""

class_field_template = """
    {property_name}: {py_type}{field_description}"""


def schema_to_class(key, definition):
    if "properties" in definition:
        properties = definition["properties"]
    else:
        properties = {}

    if "description" in definition:
        description = '\n    """' + definition["description"] + '"""'
    else:
        description = ""

    class_fields = ""

    for propperty_name, property_def in properties.items():

        if "description" in property_def:
            field_description = '  # ' + property_def["description"]
        else:
            field_description = ""

        if "$ref" in property_def:
            reference_class = property_def["$ref"].split("/")[-1]
            py_type = '\"' + convert_to_class_case(reference_class) + '\"'

        elif propperty_name == "alliances":

            alliance_property_def = property_def["properties"]["blue"]

            if "$ref" in alliance_property_def:
                reference_class = alliance_property_def["$ref"].split("/")[-1]
            else:
                reference_class = alliance_property_def["items"]["$ref"].split("/")[-1]
            py_type = "\"Alliances[{kk}]\"".format(kk=convert_to_class_case(reference_class))

        else:
            data_type = property_def["type"]
            if data_type == "object":
                py_type = "dict"
            elif data_type == "number":
                py_type = "float"
            elif data_type == "string":
                py_type = "str"
            elif data_type == "integer":
                py_type = "int"
            elif data_type == "boolean":
                py_type = "bool"
            elif data_type == "array":
                array_items = property_def["items"]

                if "$ref" in array_items:
                    reference_class = array_items["$ref"].split("/")[-1]
                    py_type = "\"List[" + convert_to_class_case(reference_class) + "]\""
                else:
                    array_type = array_items["type"]
                    if array_type == "object":
                        py_type = "List[dict]"
                    elif array_type == "number":
                        py_type = "List[float]"
                    elif array_type == "string":
                        py_type = "List[str]"
                    elif array_type == "integer":
                        py_type = "List[int]"
                    elif array_type == "boolean":
                        py_type = "List[bool]"
                    else:
                        print(array_items)
                        raise TypeError()
            else:
                raise TypeError()

        # "in" is reserved in Kotlin
        if propperty_name == "in":
            propperty_name = "_in"

        class_fields += class_field_template.format(
            field_description=field_description, property_name=propperty_name, py_type=py_type)
    return template.format(class_description=description, clz=key, fields=class_fields)


def convert_to_class_case(underscore_case):
    split = underscore_case.split("_")
    return "".join(word[0].capitalize() + word[1:] for word in split)


with open("../tba_python/models.py", mode="w") as f:
    print("# The Blue Alliance API Version", api_version, "\n", file=f)
    print(header, file=f)
    for schema_key, schema_definition in model_schemas.items():
        kotlin_name = convert_to_class_case(schema_key)
        print(schema_to_class(kotlin_name, schema_definition), file=f)
