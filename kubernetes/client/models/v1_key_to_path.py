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


class V1KeyToPath(object):
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
        'key': 'str',
        'mode': 'int',
        'path': 'str'
    }

    attribute_map = {
        'key': 'key',
        'mode': 'mode',
        'path': 'path'
    }

    def __init__(self, key=None, mode=None, path=None):  # noqa: E501
        """V1KeyToPath - a model defined in OpenAPI"""  # noqa: E501

        self._key = None
        self._mode = None
        self._path = None
        self.discriminator = None

        self.key = key
        if mode is not None:
            self.mode = mode
        self.path = path

    @property
    def key(self):
        """Gets the key of this V1KeyToPath.  # noqa: E501

        The key to project.  # noqa: E501

        :return: The key of this V1KeyToPath.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this V1KeyToPath.

        The key to project.  # noqa: E501

        :param key: The key of this V1KeyToPath.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def mode(self):
        """Gets the mode of this V1KeyToPath.  # noqa: E501

        Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.  # noqa: E501

        :return: The mode of this V1KeyToPath.  # noqa: E501
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this V1KeyToPath.

        Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.  # noqa: E501

        :param mode: The mode of this V1KeyToPath.  # noqa: E501
        :type: int
        """

        self._mode = mode

    @property
    def path(self):
        """Gets the path of this V1KeyToPath.  # noqa: E501

        The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.  # noqa: E501

        :return: The path of this V1KeyToPath.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this V1KeyToPath.

        The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.  # noqa: E501

        :param path: The path of this V1KeyToPath.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

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
        if not isinstance(other, V1KeyToPath):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
