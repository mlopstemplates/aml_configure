import os
import sys
import pytest

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(myPath, "..", "code"))

from utils import validate_json, AMLConfigurationException, InvalidDeploymentModeException
from json import JSONDecodeError
from azure.mgmt.resource.resources.models import DeploymentMode


def test_get_deploy_mode_incremental():
  assert get_deploy_mode_obj("Incremental") == DeploymentMode.incremental
  
  
def test_get_deploy_mode_complete():
  assert get_deploy_mode_obj("Complete") == DeploymentMode.complete

def test_get_deploy_mode_incremental():
  assert get_deploy_mode_obj("Incremental") == DeploymentMode.incremental
  
def test_get_deploy_mode_invalid_input():
  with pytest.raises(InvalidDeploymentModeException):
        assert get_deploy_mode_obj("InvalidInput")
