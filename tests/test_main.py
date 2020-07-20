
import os
import sys
import pytest

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(myPath, "..", "code"))

from main import main
from utils import AMLConfigurationException, CredentialsVerificationError

def get_sample_credentials():
    return """{
        'clientId': 'test',
        'clientSecret': 'test',
        'subscriptionId': 'test',
        'tenantId': 'test'
    }"""  

def test_main_invalid_parameters_files(mocker):        
    os.environ["INPUT_AZURE_CREDENTIALS"] =get_sample_credentials()
    os.environ["INPUT_RESOURCE_GROUP"] = "testGroup"
    mocker.patch('utils.get_service_principal_credentials', return_value=None)
    with pytest.raises(ResourceManagementError):
      assert main()
    
        
