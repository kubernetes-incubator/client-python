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
from kubernetes.client.api.autoscaling_api import AutoscalingApi  # noqa: E501
from kubernetes.client.rest import ApiException


class TestAutoscalingApi(unittest.TestCase):
    """AutoscalingApi unit test stubs"""

    def setUp(self):
        self.api = kubernetes.client.api.autoscaling_api.AutoscalingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_api_group(self):
        """Test case for get_api_group

        """
        pass


if __name__ == '__main__':
    unittest.main()
