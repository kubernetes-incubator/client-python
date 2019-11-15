# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: v1.15.7
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class V1WeightedPodAffinityTerm(object):
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
        'pod_affinity_term': 'V1PodAffinityTerm',
        'weight': 'int'
    }

    attribute_map = {
        'pod_affinity_term': 'podAffinityTerm',
        'weight': 'weight'
    }

    def __init__(self, pod_affinity_term=None, weight=None):  # noqa: E501
        """V1WeightedPodAffinityTerm - a model defined in OpenAPI"""  # noqa: E501

        self._pod_affinity_term = None
        self._weight = None
        self.discriminator = None

        self.pod_affinity_term = pod_affinity_term
        self.weight = weight

    @property
    def pod_affinity_term(self):
        """Gets the pod_affinity_term of this V1WeightedPodAffinityTerm.  # noqa: E501


        :return: The pod_affinity_term of this V1WeightedPodAffinityTerm.  # noqa: E501
        :rtype: V1PodAffinityTerm
        """
        return self._pod_affinity_term

    @pod_affinity_term.setter
    def pod_affinity_term(self, pod_affinity_term):
        """Sets the pod_affinity_term of this V1WeightedPodAffinityTerm.


        :param pod_affinity_term: The pod_affinity_term of this V1WeightedPodAffinityTerm.  # noqa: E501
        :type: V1PodAffinityTerm
        """
        if pod_affinity_term is None:
            raise ValueError("Invalid value for `pod_affinity_term`, must not be `None`")  # noqa: E501

        self._pod_affinity_term = pod_affinity_term

    @property
    def weight(self):
        """Gets the weight of this V1WeightedPodAffinityTerm.  # noqa: E501

        weight associated with matching the corresponding podAffinityTerm, in the range 1-100.  # noqa: E501

        :return: The weight of this V1WeightedPodAffinityTerm.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this V1WeightedPodAffinityTerm.

        weight associated with matching the corresponding podAffinityTerm, in the range 1-100.  # noqa: E501

        :param weight: The weight of this V1WeightedPodAffinityTerm.  # noqa: E501
        :type: int
        """
        if weight is None:
            raise ValueError("Invalid value for `weight`, must not be `None`")  # noqa: E501

        self._weight = weight

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
        if not isinstance(other, V1WeightedPodAffinityTerm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
