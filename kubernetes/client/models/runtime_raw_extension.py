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


class RuntimeRawExtension(object):
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
        'raw': 'str'
    }

    attribute_map = {
        'raw': 'Raw'
    }

    def __init__(self, raw=None):  # noqa: E501
        """RuntimeRawExtension - a model defined in OpenAPI"""  # noqa: E501

        self._raw = None
        self.discriminator = None

        self.raw = raw

    @property
    def raw(self):
        """Gets the raw of this RuntimeRawExtension.  # noqa: E501

        Raw is the underlying serialization of this object.  # noqa: E501

        :return: The raw of this RuntimeRawExtension.  # noqa: E501
        :rtype: str
        """
        return self._raw

    @raw.setter
    def raw(self, raw):
        """Sets the raw of this RuntimeRawExtension.

        Raw is the underlying serialization of this object.  # noqa: E501

        :param raw: The raw of this RuntimeRawExtension.  # noqa: E501
        :type: str
        """
        if raw is None:
            raise ValueError("Invalid value for `raw`, must not be `None`")  # noqa: E501
        if raw is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', raw):  # noqa: E501
            raise ValueError(r"Invalid value for `raw`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._raw = raw

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
        if not isinstance(other, RuntimeRawExtension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
