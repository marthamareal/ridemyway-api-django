# Third party libraries
import pytest

# Models
from ridemyway.api.utilities.base_model import BaseModel

class TestBaseModel:
    """Class for testing the BaseModel"""
    def tests_id_generation_succeeds(self):
        """Checks if the id is generated automatically and is uuid"""
        object = BaseModel()
        assert len(str(object.id)) == 36
