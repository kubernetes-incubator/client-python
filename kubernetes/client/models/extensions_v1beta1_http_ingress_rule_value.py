# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: v1.15.8
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ExtensionsV1beta1HTTPIngressRuleValue(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'paths': 'list[ExtensionsV1beta1HTTPIngressPath]'
    }

    attribute_map = {
        'paths': 'paths'
    }

    def __init__(self, paths=None):  # noqa: E501
        """ExtensionsV1beta1HTTPIngressRuleValue - a model defined in OpenAPI"""  # noqa: E501

        self._paths = None
        self.discriminator = None

        self.paths = paths

    @property
    def paths(self):
        """Gets the paths of this ExtensionsV1beta1HTTPIngressRuleValue.  # noqa: E501

        A collection of paths that map requests to backends.  # noqa: E501

        :return: The paths of this ExtensionsV1beta1HTTPIngressRuleValue.  # noqa: E501
        :rtype: list[ExtensionsV1beta1HTTPIngressPath]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """Sets the paths of this ExtensionsV1beta1HTTPIngressRuleValue.

        A collection of paths that map requests to backends.  # noqa: E501

        :param paths: The paths of this ExtensionsV1beta1HTTPIngressRuleValue.  # noqa: E501
        :type: list[ExtensionsV1beta1HTTPIngressPath]
        """
        if paths is None:
            raise ValueError("Invalid value for `paths`, must not be `None`")  # noqa: E501

        self._paths = paths

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExtensionsV1beta1HTTPIngressRuleValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
