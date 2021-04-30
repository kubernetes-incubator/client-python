# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.17
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.v1_config_map_volume_source import V1ConfigMapVolumeSource  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1ConfigMapVolumeSource(unittest.TestCase):
    """V1ConfigMapVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1ConfigMapVolumeSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_config_map_volume_source.V1ConfigMapVolumeSource()  # noqa: E501
        if include_optional :
            return V1ConfigMapVolumeSource(
                default_mode = 56, 
                items = [
                    kubernetes.client.models.v1/key_to_path.v1.KeyToPath(
                        key = '0', 
                        mode = 56, 
                        path = '0', )
                    ], 
                name = '0', 
                optional = True
            )
        else :
            return V1ConfigMapVolumeSource(
        )

    def testV1ConfigMapVolumeSource(self):
        """Test V1ConfigMapVolumeSource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
