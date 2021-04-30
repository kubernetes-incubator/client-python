# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.17
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.v1beta2_deployment_list import V1beta2DeploymentList  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1beta2DeploymentList(unittest.TestCase):
    """V1beta2DeploymentList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta2DeploymentList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1beta2_deployment_list.V1beta2DeploymentList()  # noqa: E501
        if include_optional :
            return V1beta2DeploymentList(
                api_version = '0', 
                items = [
                    kubernetes.client.models.v1beta2/deployment.v1beta2.Deployment(
                        api_version = '0', 
                        kind = '0', 
                        metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                            annotations = {
                                'key' : '0'
                                }, 
                            cluster_name = '0', 
                            creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            deletion_grace_period_seconds = 56, 
                            deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            finalizers = [
                                '0'
                                ], 
                            generate_name = '0', 
                            generation = 56, 
                            labels = {
                                'key' : '0'
                                }, 
                            managed_fields = [
                                kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                                    api_version = '0', 
                                    fields_type = '0', 
                                    fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                                    manager = '0', 
                                    operation = '0', 
                                    time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], 
                            name = '0', 
                            namespace = '0', 
                            owner_references = [
                                kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
                                    api_version = '0', 
                                    block_owner_deletion = True, 
                                    controller = True, 
                                    kind = '0', 
                                    name = '0', 
                                    uid = '0', )
                                ], 
                            resource_version = '0', 
                            self_link = '0', 
                            uid = '0', ), 
                        spec = kubernetes.client.models.v1beta2/deployment_spec.v1beta2.DeploymentSpec(
                            min_ready_seconds = 56, 
                            paused = True, 
                            progress_deadline_seconds = 56, 
                            replicas = 56, 
                            revision_history_limit = 56, 
                            selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                                match_expressions = [
                                    kubernetes.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                                        key = '0', 
                                        operator = '0', 
                                        values = [
                                            '0'
                                            ], )
                                    ], 
                                match_labels = {
                                    'key' : '0'
                                    }, ), 
                            strategy = kubernetes.client.models.v1beta2/deployment_strategy.v1beta2.DeploymentStrategy(
                                rolling_update = kubernetes.client.models.v1beta2/rolling_update_deployment.v1beta2.RollingUpdateDeployment(
                                    max_surge = kubernetes.client.models.max_surge.maxSurge(), 
                                    max_unavailable = kubernetes.client.models.max_unavailable.maxUnavailable(), ), 
                                type = '0', ), 
                            template = kubernetes.client.models.v1/pod_template_spec.v1.PodTemplateSpec(), ), 
                        status = kubernetes.client.models.v1beta2/deployment_status.v1beta2.DeploymentStatus(
                            available_replicas = 56, 
                            collision_count = 56, 
                            conditions = [
                                kubernetes.client.models.v1beta2/deployment_condition.v1beta2.DeploymentCondition(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    last_update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '0', 
                                    reason = '0', 
                                    status = '0', 
                                    type = '0', )
                                ], 
                            observed_generation = 56, 
                            ready_replicas = 56, 
                            replicas = 56, 
                            unavailable_replicas = 56, 
                            updated_replicas = 56, ), )
                    ], 
                kind = '0', 
                metadata = kubernetes.client.models.v1/list_meta.v1.ListMeta(
                    continue = '0', 
                    remaining_item_count = 56, 
                    resource_version = '0', 
                    self_link = '0', )
            )
        else :
            return V1beta2DeploymentList(
                items = [
                    kubernetes.client.models.v1beta2/deployment.v1beta2.Deployment(
                        api_version = '0', 
                        kind = '0', 
                        metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                            annotations = {
                                'key' : '0'
                                }, 
                            cluster_name = '0', 
                            creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            deletion_grace_period_seconds = 56, 
                            deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            finalizers = [
                                '0'
                                ], 
                            generate_name = '0', 
                            generation = 56, 
                            labels = {
                                'key' : '0'
                                }, 
                            managed_fields = [
                                kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                                    api_version = '0', 
                                    fields_type = '0', 
                                    fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                                    manager = '0', 
                                    operation = '0', 
                                    time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], 
                            name = '0', 
                            namespace = '0', 
                            owner_references = [
                                kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
                                    api_version = '0', 
                                    block_owner_deletion = True, 
                                    controller = True, 
                                    kind = '0', 
                                    name = '0', 
                                    uid = '0', )
                                ], 
                            resource_version = '0', 
                            self_link = '0', 
                            uid = '0', ), 
                        spec = kubernetes.client.models.v1beta2/deployment_spec.v1beta2.DeploymentSpec(
                            min_ready_seconds = 56, 
                            paused = True, 
                            progress_deadline_seconds = 56, 
                            replicas = 56, 
                            revision_history_limit = 56, 
                            selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                                match_expressions = [
                                    kubernetes.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                                        key = '0', 
                                        operator = '0', 
                                        values = [
                                            '0'
                                            ], )
                                    ], 
                                match_labels = {
                                    'key' : '0'
                                    }, ), 
                            strategy = kubernetes.client.models.v1beta2/deployment_strategy.v1beta2.DeploymentStrategy(
                                rolling_update = kubernetes.client.models.v1beta2/rolling_update_deployment.v1beta2.RollingUpdateDeployment(
                                    max_surge = kubernetes.client.models.max_surge.maxSurge(), 
                                    max_unavailable = kubernetes.client.models.max_unavailable.maxUnavailable(), ), 
                                type = '0', ), 
                            template = kubernetes.client.models.v1/pod_template_spec.v1.PodTemplateSpec(), ), 
                        status = kubernetes.client.models.v1beta2/deployment_status.v1beta2.DeploymentStatus(
                            available_replicas = 56, 
                            collision_count = 56, 
                            conditions = [
                                kubernetes.client.models.v1beta2/deployment_condition.v1beta2.DeploymentCondition(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    last_update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '0', 
                                    reason = '0', 
                                    status = '0', 
                                    type = '0', )
                                ], 
                            observed_generation = 56, 
                            ready_replicas = 56, 
                            replicas = 56, 
                            unavailable_replicas = 56, 
                            updated_replicas = 56, ), )
                    ],
        )

    def testV1beta2DeploymentList(self):
        """Test V1beta2DeploymentList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
