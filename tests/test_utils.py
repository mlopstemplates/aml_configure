import os
import sys
import pytest

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(myPath, "..", "code"))

from utils import AMLConfigurationException, InvalidDeploymentModeException, TemplateParameterException, get_deploy_mode_obj ,get_template_parameters, required_parameters_provided
from json import JSONDecodeError
from azure.mgmt.resource.resources.models import DeploymentMode

def get_sample_credentials():
    return """{
        "clientId": "test",
        "clientSecret": "test",
        "subscriptionId": "test",
        "tenantId": "test"
    }"""

def test_get_deploy_mode_incremental():
  assert get_deploy_mode_obj("Incremental") == DeploymentMode.incremental
  
def test_get_deploy_mode_complete():
  assert get_deploy_mode_obj("Complete") == DeploymentMode.complete

def test_get_deploy_mode_incremental():
  assert get_deploy_mode_obj("Incremental") == DeploymentMode.incremental
  
def test_get_deploy_mode_invalid_input():
  with pytest.raises(InvalidDeploymentModeException):
        assert get_deploy_mode_obj("InvalidInput")

def test_get_template_parameters_mapped_params_added():
    parameters=get_template_parameters("",{"testParams":"testValue"})
    assert parameters["testParams"]["value"] == "testValue"

    
def test_get_template_parameters_incorrect_parameter_file():
    with pytest.raises(FileNotFoundError):
        assert get_template_parameters("wrongFile.json",{})

        
def test_required_credential_parameters_specified():
        parameters=get_sample_credentials(),
        keys=["tenantId", "WrongclientId", "clientSecret"],
        message="Test Message"
        with pytest.raises(AMLConfigurationException):
          required_parameters_provided(parameters, keys,message)

      
