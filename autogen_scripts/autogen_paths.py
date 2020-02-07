import json

swagger_file = open("api_v3.json")
json_data = swagger_file.read()
swagger_file.close()

data = json.loads(json_data)

api_version = data["info"]["version"]
paths = data["paths"]
model_schemas = data["components"]["schemas"]

header = """from converter import *"""

function_template = """
def {operation_id}(tba, {params}):
    \"\"\"{description}\"\"\"
    return {prefix}tba.get(f"{templated_path}"){postfix}"""

request_parameter_types = {
    "page_num": "int",
    "year": "int",
    "media_tag": "str",
    "team_key": "str",
    "event_key": "str",
    "match_key": "str",
    "district_key": "str"
}

def convert_to_class_case(underscore_case):
    split = underscore_case.split("_")
    return "".join(word[0].capitalize() + word[1:] for word in split)


def function_for_api_path(path_name, path_def):
    get_request_definition = path_def["get"]
    operation_id = get_request_definition["operationId"]
    description = get_request_definition["description"]
    params = get_request_definition["parameters"]
    actual_params = []

    for i in range(len(params)):
        param = params[i]
        if "$ref" in param:
            param_name = params[i]["$ref"].split("/")[-1]
            if param_name != "If-Modified-Since":
                actual_params.append(param_name)
        else:
            actual_params.append(param["name"]) #FIXME

    get_response_schema = get_request_definition["responses"]["200"]["content"]["application/json"]["schema"]
    templated_path = path_name

    if len(actual_params) == 0:
        params_string = ""
    else:
        pdef = [x + ": " + request_parameter_types[x] for x in actual_params]
        params_string = ", ".join(pdef)

    if "$ref" in get_response_schema:
        func_name = "get"
        referenced_definition = get_response_schema["$ref"].split("/")[-1]
        clz = convert_to_class_case(referenced_definition)
        prefix = f"convertTo{clz}("
        postfix = f")"
    elif get_response_schema["type"] == "array":
        it = get_response_schema["items"]
        func_name = "getArray"
        if "$ref" in it:
            referenced_definition = it["$ref"].split("/")[-1]
            clz = convert_to_class_case(referenced_definition)
            prefix = f"[convertTo{clz}(item) for item in "
            postfix = "]"
        elif it["type"] == "string":
            prefix = ""
            postfix = ""
        elif it["type"] == "integer":
            prefix = ""
            postfix = ""
        elif it["type"] == "object":
            prefix = ""
            postfix = ""
        else:
            raise TypeError()

    elif get_response_schema["type"] == "object":
        func_name = "get"
        referenced_definition = get_response_schema["additionalProperties"]["$ref"].split("/")[-1]
        clz = convert_to_class_case(referenced_definition)
        prefix = f"[convertTo{clz}(v) for v in "
        postfix = ".values()]"
    else:
        raise TypeError()

    return function_template.format(
        description=description, operation_id=operation_id, params=params_string,
        templated_path=templated_path, prefix=prefix, postfix=postfix, func_name=func_name)


with open("../tba_python/paths.py", mode="w") as f:
    print("# API Version", api_version, "\n", file=f)
    print(header, file=f)
    for path_key, path_definition in paths.items():
        print(function_for_api_path(path_key, path_definition), file=f)
