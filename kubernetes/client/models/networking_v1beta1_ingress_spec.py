# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: v1.14.6
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class NetworkingV1beta1IngressSpec(object):
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
        'backend': 'NetworkingV1beta1IngressBackend',
        'rules': 'list[NetworkingV1beta1IngressRule]',
        'tls': 'list[NetworkingV1beta1IngressTLS]'
    }

    attribute_map = {
        'backend': 'backend',
        'rules': 'rules',
        'tls': 'tls'
    }

    def __init__(self, backend=None, rules=None, tls=None):  # noqa: E501
        """NetworkingV1beta1IngressSpec - a model defined in OpenAPI"""  # noqa: E501

        self._backend = None
        self._rules = None
        self._tls = None
        self.discriminator = None

        if backend is not None:
            self.backend = backend
        if rules is not None:
            self.rules = rules
        if tls is not None:
            self.tls = tls

    @property
    def backend(self):
        """Gets the backend of this NetworkingV1beta1IngressSpec.  # noqa: E501


        :return: The backend of this NetworkingV1beta1IngressSpec.  # noqa: E501
        :rtype: NetworkingV1beta1IngressBackend
        """
        return self._backend

    @backend.setter
    def backend(self, backend):
        """Sets the backend of this NetworkingV1beta1IngressSpec.


        :param backend: The backend of this NetworkingV1beta1IngressSpec.  # noqa: E501
        :type: NetworkingV1beta1IngressBackend
        """

        self._backend = backend

    @property
    def rules(self):
        """Gets the rules of this NetworkingV1beta1IngressSpec.  # noqa: E501

        A list of host rules used to configure the Ingress. If unspecified, or no rule matches, all traffic is sent to the default backend.  # noqa: E501

        :return: The rules of this NetworkingV1beta1IngressSpec.  # noqa: E501
        :rtype: list[NetworkingV1beta1IngressRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this NetworkingV1beta1IngressSpec.

        A list of host rules used to configure the Ingress. If unspecified, or no rule matches, all traffic is sent to the default backend.  # noqa: E501

        :param rules: The rules of this NetworkingV1beta1IngressSpec.  # noqa: E501
        :type: list[NetworkingV1beta1IngressRule]
        """

        self._rules = rules

    @property
    def tls(self):
        """Gets the tls of this NetworkingV1beta1IngressSpec.  # noqa: E501

        TLS configuration. Currently the Ingress only supports a single TLS port, 443. If multiple members of this list specify different hosts, they will be multiplexed on the same port according to the hostname specified through the SNI TLS extension, if the ingress controller fulfilling the ingress supports SNI.  # noqa: E501

        :return: The tls of this NetworkingV1beta1IngressSpec.  # noqa: E501
        :rtype: list[NetworkingV1beta1IngressTLS]
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this NetworkingV1beta1IngressSpec.

        TLS configuration. Currently the Ingress only supports a single TLS port, 443. If multiple members of this list specify different hosts, they will be multiplexed on the same port according to the hostname specified through the SNI TLS extension, if the ingress controller fulfilling the ingress supports SNI.  # noqa: E501

        :param tls: The tls of this NetworkingV1beta1IngressSpec.  # noqa: E501
        :type: list[NetworkingV1beta1IngressTLS]
        """

        self._tls = tls

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
        if not isinstance(other, NetworkingV1beta1IngressSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
