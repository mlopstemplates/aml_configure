
import os
import sys
import pytest
from unittest import mock

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(myPath, "..", "code"))

from main import main
from utils import AMLConfigurationException, CredentialsVerificationError, ResourceManagementError, ActionDeploymentError

def get_sample_credentials():
    return """{
        "clientId": "test",
        "clientSecret": "test",
        "subscriptionId": "test",
        "tenantId": "test"
    }""" 


def test_main_no_input():
    """
    Unit test to check the main function with no inputs
    """
    with pytest.raises(AMLConfigurationException):
        assert main()


def test_main_invalid_azure_credentials():
    os.environ["INPUT_AZURE_CREDENTIALS"] = ""
    with pytest.raises(AMLConfigurationException):
        assert main()

def test_main_resource_grp_not_provided():
    os.environ["INPUT_AZURE_CREDENTIALS"] = get_sample_credentials()
    os.environ["INPUT_MAPPED_PARAMS"] ='{"testParams":"testValue"}'
    with pytest.raises(AMLConfigurationException):
        assert main()
        
def test_main_invalid_mapped_parameters():
    os.environ["INPUT_AZURE_CREDENTIALS"] = get_sample_credentials()
    os.environ["INPUT_MAPPED_PARAMS"] ="wrong mapped params"
    with pytest.raises(AMLConfigurationException):
        assert main()        
        

def test_main_invalid_parameters_file():
    os.environ["INPUT_AZURE_CREDENTIALS"] =get_sample_credentials()
    os.environ["INPUT_MAPPED_PARAMS"] ='{"testParams":"testValue"}'
    os.environ["INPUT_PARAMETERS_FILE"] = "wrongfile.json"
    with pytest.raises(AMLConfigurationException):
        assert main()

def test_main_invalid_credentials():        
    os.environ["INPUT_AZURE_CREDENTIALS"] =get_sample_credentials()
    os.environ["INPUT_MAPPED_PARAMS"] ='{"testParams":"testValue"}'
    os.environ["INPUT_RESOURCE_GROUP"] = "testGroup"
    with pytest.raises(CredentialsVerificationError):
        assert main()
        
@mock.patch("main.ServicePrincipalCredentials",return_value="check3",autospec=True)
def test_main_validation_fails(mock_check): 
    os.environ["INPUT_AZURE_CREDENTIALS"] =get_sample_credentials()
    os.environ["INPUT_MAPPED_PARAMS"] ='{"testParams":"testValue"}'
    os.environ["INPUT_RESOURCE_GROUP"] = "testGroup"
    with pytest.raises(ActionDeploymentError):
        assert main()          
        

@mock.patch("main.ServicePrincipalCredentials",return_value="check3",autospec=True)
def test_main_invalid_template_file_provided(mock_check): 
    os.environ["INPUT_AZURE_CREDENTIALS"] =get_sample_credentials()
    os.environ["INPUT_MAPPED_PARAMS"] ='{"testParams":"testValue"}'
    os.environ["INPUT_RESOURCE_GROUP"] = "testGroup"
    os.environ["INPUT_ARMTEMPLATE_FILE"] = "InvalidFile.json"    
    with pytest.raises(FileNotFoundError):
        assert main()        
