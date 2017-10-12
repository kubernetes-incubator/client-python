# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.8.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1FSGroupStrategyOptions(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ranges': 'list[V1beta1IDRange]',
        'rule': 'str'
    }

    attribute_map = {
        'ranges': 'ranges',
        'rule': 'rule'
    }

    def __init__(self, ranges=None, rule=None):
        """
        V1beta1FSGroupStrategyOptions - a model defined in Swagger
        """

        self._ranges = None
        self._rule = None
        self.discriminator = None

        if ranges is not None:
          self.ranges = ranges
        if rule is not None:
          self.rule = rule

    @property
    def ranges(self):
        """
        Gets the ranges of this V1beta1FSGroupStrategyOptions.
        Ranges are the allowed ranges of fs groups.  If you would like to force a single fs group then supply a single range with the same start and end.

        :return: The ranges of this V1beta1FSGroupStrategyOptions.
        :rtype: list[V1beta1IDRange]
        """
        return self._ranges

    @ranges.setter
    def ranges(self, ranges):
        """
        Sets the ranges of this V1beta1FSGroupStrategyOptions.
        Ranges are the allowed ranges of fs groups.  If you would like to force a single fs group then supply a single range with the same start and end.

        :param ranges: The ranges of this V1beta1FSGroupStrategyOptions.
        :type: list[V1beta1IDRange]
        """

        self._ranges = ranges

    @property
    def rule(self):
        """
        Gets the rule of this V1beta1FSGroupStrategyOptions.
        Rule is the strategy that will dictate what FSGroup is used in the SecurityContext.

        :return: The rule of this V1beta1FSGroupStrategyOptions.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """
        Sets the rule of this V1beta1FSGroupStrategyOptions.
        Rule is the strategy that will dictate what FSGroup is used in the SecurityContext.

        :param rule: The rule of this V1beta1FSGroupStrategyOptions.
        :type: str
        """

        self._rule = rule

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1beta1FSGroupStrategyOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
