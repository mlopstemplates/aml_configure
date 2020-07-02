import os
import sys
import importlib
import json
from json import JSONDecodeError

class ActionDeploymentError(Exception):
    pass

class AMLConfigurationException(Exception):
    pass

class ResourceManagementError(Exception):
    pass

class CredentialsVerificationError(Exception):
    pass

class TemplateParameterException(Exception):
    pass


def get_template_parameters(template_params_file_path,mapped_params):
    parameters=None
    try:
        with open(template_params_file_path,"r") as f:
            jsonobject = json.load(f);
        parameters=jsonobject["parameters"]
        for k in mapped_params:
            parameters[k]={}
            parameters[k]["value"] = mapped_params[k]
   
    except JSONDecodeError:
        print("::error::Please check the parameter file for errors")
        raise TemplateParameterException(f"Incorrect or poorly formed template parameters")
        
    return parameters

def required_parameters_provided(parameters, keys, message="Required parameter not found in your parameters file. Please provide a value for the following key(s): "):
    missing_keys = []
    for key in keys:
        if key not in parameters:
            err_msg = f"{message} {key}"
            print(f"::error::{err_msg}")
            missing_keys.append(key)
    if len(missing_keys) > 0:
        raise AMLConfigurationException(f"{message} {missing_keys}")


def mask_parameter(parameter):
    print(f"::add-mask::{parameter}")

