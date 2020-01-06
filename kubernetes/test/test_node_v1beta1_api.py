# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: v1.15.8
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kubernetes.client
from kubernetes.client.api.node_v1beta1_api import NodeV1beta1Api  # noqa: E501
from kubernetes.client.rest import ApiException


class TestNodeV1beta1Api(unittest.TestCase):
    """NodeV1beta1Api unit test stubs"""

    def setUp(self):
        self.api = kubernetes.client.api.node_v1beta1_api.NodeV1beta1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_runtime_class(self):
        """Test case for create_runtime_class

        """
        pass

    def test_delete_collection_runtime_class(self):
        """Test case for delete_collection_runtime_class

        """
        pass

    def test_delete_runtime_class(self):
        """Test case for delete_runtime_class

        """
        pass

    def test_get_api_resources(self):
        """Test case for get_api_resources

        """
        pass

    def test_list_runtime_class(self):
        """Test case for list_runtime_class

        """
        pass

    def test_patch_runtime_class(self):
        """Test case for patch_runtime_class

        """
        pass

    def test_read_runtime_class(self):
        """Test case for read_runtime_class

        """
        pass

    def test_replace_runtime_class(self):
        """Test case for replace_runtime_class

        """
        pass


if __name__ == '__main__':
    unittest.main()
