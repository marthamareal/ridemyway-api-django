""" Renderer class for the API"""

from rest_framework.renderers import JSONRenderer
from rest_framework.utils import json


class ApiRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        # Ovveride the default renderer method in JSONRenderer
        return json.dumps(data)
