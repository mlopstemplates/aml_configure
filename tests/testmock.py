
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



@mock.patch("main.ServicePrincipalCredentials",return_value="check3",autospec=True)
def test_main_validation_fails(mock_check): 
    os.environ["INPUT_AZURE_CREDENTIALS"] =get_sample_credentials()
    os.environ["INPUT_MAPPED_PARAMS"] ='{"testParams":"testValue"}'
    os.environ["INPUT_RESOURCE_GROUP"] = "testGroup"
 
        

