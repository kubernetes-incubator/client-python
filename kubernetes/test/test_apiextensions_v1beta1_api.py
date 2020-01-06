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
from kubernetes.client.api.apiextensions_v1beta1_api import ApiextensionsV1beta1Api  # noqa: E501
from kubernetes.client.rest import ApiException


class TestApiextensionsV1beta1Api(unittest.TestCase):
    """ApiextensionsV1beta1Api unit test stubs"""

    def setUp(self):
        self.api = kubernetes.client.api.apiextensions_v1beta1_api.ApiextensionsV1beta1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_custom_resource_definition(self):
        """Test case for create_custom_resource_definition

        """
        pass

    def test_delete_collection_custom_resource_definition(self):
        """Test case for delete_collection_custom_resource_definition

        """
        pass

    def test_delete_custom_resource_definition(self):
        """Test case for delete_custom_resource_definition

        """
        pass

    def test_get_api_resources(self):
        """Test case for get_api_resources

        """
        pass

    def test_list_custom_resource_definition(self):
        """Test case for list_custom_resource_definition

        """
        pass

    def test_patch_custom_resource_definition(self):
        """Test case for patch_custom_resource_definition

        """
        pass

    def test_patch_custom_resource_definition_status(self):
        """Test case for patch_custom_resource_definition_status

        """
        pass

    def test_read_custom_resource_definition(self):
        """Test case for read_custom_resource_definition

        """
        pass

    def test_read_custom_resource_definition_status(self):
        """Test case for read_custom_resource_definition_status

        """
        pass

    def test_replace_custom_resource_definition(self):
        """Test case for replace_custom_resource_definition

        """
        pass

    def test_replace_custom_resource_definition_status(self):
        """Test case for replace_custom_resource_definition_status

        """
        pass


if __name__ == '__main__':
    unittest.main()
