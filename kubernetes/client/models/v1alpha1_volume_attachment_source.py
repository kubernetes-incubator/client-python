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


class V1alpha1VolumeAttachmentSource(object):
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
        'inline_volume_spec': 'V1PersistentVolumeSpec',
        'persistent_volume_name': 'str'
    }

    attribute_map = {
        'inline_volume_spec': 'inlineVolumeSpec',
        'persistent_volume_name': 'persistentVolumeName'
    }

    def __init__(self, inline_volume_spec=None, persistent_volume_name=None):  # noqa: E501
        """V1alpha1VolumeAttachmentSource - a model defined in OpenAPI"""  # noqa: E501

        self._inline_volume_spec = None
        self._persistent_volume_name = None
        self.discriminator = None

        if inline_volume_spec is not None:
            self.inline_volume_spec = inline_volume_spec
        if persistent_volume_name is not None:
            self.persistent_volume_name = persistent_volume_name

    @property
    def inline_volume_spec(self):
        """Gets the inline_volume_spec of this V1alpha1VolumeAttachmentSource.  # noqa: E501


        :return: The inline_volume_spec of this V1alpha1VolumeAttachmentSource.  # noqa: E501
        :rtype: V1PersistentVolumeSpec
        """
        return self._inline_volume_spec

    @inline_volume_spec.setter
    def inline_volume_spec(self, inline_volume_spec):
        """Sets the inline_volume_spec of this V1alpha1VolumeAttachmentSource.


        :param inline_volume_spec: The inline_volume_spec of this V1alpha1VolumeAttachmentSource.  # noqa: E501
        :type: V1PersistentVolumeSpec
        """

        self._inline_volume_spec = inline_volume_spec

    @property
    def persistent_volume_name(self):
        """Gets the persistent_volume_name of this V1alpha1VolumeAttachmentSource.  # noqa: E501

        Name of the persistent volume to attach.  # noqa: E501

        :return: The persistent_volume_name of this V1alpha1VolumeAttachmentSource.  # noqa: E501
        :rtype: str
        """
        return self._persistent_volume_name

    @persistent_volume_name.setter
    def persistent_volume_name(self, persistent_volume_name):
        """Sets the persistent_volume_name of this V1alpha1VolumeAttachmentSource.

        Name of the persistent volume to attach.  # noqa: E501

        :param persistent_volume_name: The persistent_volume_name of this V1alpha1VolumeAttachmentSource.  # noqa: E501
        :type: str
        """

        self._persistent_volume_name = persistent_volume_name

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
        if not isinstance(other, V1alpha1VolumeAttachmentSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
