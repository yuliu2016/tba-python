import json

swagger_file = open("api_v3.json")
json_data = swagger_file.read()
swagger_file.close()

data = json.loads(json_data)

api_version = data["info"]["version"]

model_schemas = data["components"]["schemas"]

header = """from models import *"""

class_function_template = """
def convertTo{clz}(data):
    return {clz}(
        data,
        {param_body}
    )"""

primitives = {
    "object": "obj",
    "number": "double",
    "string": "string",
    "integer": "int",
    "boolean": "boolean"
}

array_primitives = {
    "object": "objList",
    "number": "doubleList",
    "string": "stringList",
    "integer": "intList",
    "boolean": "booleanList"
}


data_get_call_template = """data["{property_name}"]"""

alliance_template = """Alliances(
            convertTo{clz}(data["{property_name}"]["blue"]),
            convertTo{clz}(data["{property_name}"]["red"])
        )"""


def function_code_for_definition(key, definition):
    if "properties" in definition:
        properties = definition["properties"]
    else:
        properties = {}

    parameter_list = []

    for property_name, property_def in properties.items():

        if "$ref" in property_def:
            referenced_definition = property_def["$ref"].split("/")[-1]
            clz = convert_to_class_case(referenced_definition)
            kotlin_param_data = f"""convertTo{clz}(data["{property_name}"])"""

        elif property_name == "alliances":
            alliance_property_def = property_def["properties"]["blue"]

            if "$ref" in alliance_property_def:
                referenced_definition = alliance_property_def["$ref"].split("/")[-1]
            else:
                referenced_definition = alliance_property_def["items"]["$ref"].split("/")[-1]
            kotlin_param_data = alliance_template.format(
                property_name=property_name, clz=convert_to_class_case(referenced_definition))
        else:
            data_type = property_def["type"]

            if data_type in primitives.keys():
                kotlin_param_data = data_get_call_template.format(
                    func_name=primitives[data_type], property_name=property_name)

            elif data_type == "array":
                array_items = property_def["items"]

                if "$ref" in array_items:
                    referenced_definition = array_items["$ref"].split("/")[-1]
                    clz = convert_to_class_case(referenced_definition)
                    kotlin_param_data = f"""[convertTo{clz} (item) for item in data["{property_name}"]]"""
                else:
                    array_type = array_items["type"]
                    if array_type in array_primitives:
                        kotlin_param_data = data_get_call_template.format(
                            func_name=array_primitives[array_type], property_name=property_name)
                    else:
                        print(array_items)
                        raise TypeError()
            else:
                raise TypeError()

        parameter_list.append(kotlin_param_data)

    return class_function_template.format(clz=key, param_body=",\n        ".join(parameter_list))


def convert_to_class_case(underscore_case):
    split = underscore_case.split("_")
    return "".join(word[0].capitalize() + word[1:] for word in split)


with open("../tba_python/converter.py", mode="w") as f:
    print("# The Blue Alliance API Version", api_version, "\n", file=f)
    print(header, file=f)
    for schema_key, schema_definition in model_schemas.items():
        kotlin_name = convert_to_class_case(schema_key)
        print(function_code_for_definition(kotlin_name, schema_definition), file=f)
