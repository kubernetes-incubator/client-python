# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import unittest

import yaml
from kubernetes import utils, client
from datetime import datetime


class TestUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.json_path_prefix = "kubernetes/e2e_test/test_json/"
        cls.yaml_path_prefix = "kubernetes/e2e_test/test_yaml/"

    def test_load_config_map_env_source_from_simple_dict(self):
        """
        Should be able to load an object with limited data
        and passing the klass.
        """
        data = {"name": "source"}
        obj = utils.load_from_dict(data, klass="V1ConfigMapEnvSource")
        self.assertIsInstance(obj, client.models.v1_config_map_env_source.V1ConfigMapEnvSource)
        self.assertEqual(obj.name, "source")

    def test_load_secret_env_source_from_simple_dict(self):
        """
        Should be able to load an object with limited data
        and passing the klass.
        """
        data = {"name": "source"}
        obj = utils.load_from_dict(data, klass="V1SecretEnvSource")
        self.assertIsInstance(obj, client.models.v1_secret_env_source.V1SecretEnvSource)
        self.assertEqual(obj.name, "source")

    def test_load_apps_deployment_from_dict(self):
        """
        Should be able to load  apps/v1 deployment.
        """
        with open(self.yaml_path_prefix + "apps-deployment.yaml") as f:
            yml_obj = yaml.safe_load(f)
        obj = utils.load_from_dict(yml_obj)
        self.assertIsInstance(obj, client.models.v1_deployment.V1Deployment)

    def test_load_apps_deployment_from_yaml(self):
        """
        Should be able to load  apps/v1 deployment.
        """
        obj = utils.load_from_yaml(self.yaml_path_prefix + "apps-deployment.yaml")
        self.assertIsInstance(obj, client.models.v1_deployment.V1Deployment)

    def test_load_pod_from_dict(self):
        """
        Should be able to load a pod object.
        """
        with open(self.yaml_path_prefix + "core-pod.yaml") as f:
            yml_obj = yaml.safe_load(f)
        obj = utils.load_from_dict(yml_obj)
        self.assertIsInstance(obj, client.models.v1_pod.V1Pod)

    def test_load_pod_from_yaml(self):
        """
        Should be able to load a pod.
        """
        obj = utils.load_from_yaml(self.yaml_path_prefix + "core-pod.yaml")
        self.assertIsInstance(obj, client.models.v1_pod.V1Pod)

    def test_load_service_from_dict(self):
        """
        Should be able to load a service.
        """
        with open(self.yaml_path_prefix + "core-service.yaml") as f:
            yml_obj = yaml.safe_load(f)

        obj = utils.load_from_dict(yml_obj)
        self.assertIsInstance(obj, client.models.v1_service.V1Service)

    def test_load_service_from_yaml(self):
        """
        Should be able to load a service.
        """
        with open(self.yaml_path_prefix + "core-service.yaml") as f:
            yml_obj = yaml.safe_load(f)

        obj = utils.load_from_yaml(self.yaml_path_prefix + "core-service.yaml")
        self.assertIsInstance(obj, client.models.v1_service.V1Service)

    def test_load_namespace_from_dict(self):
        """
        Should be able to load a namespace.
        """
        with open(self.yaml_path_prefix + "core-namespace.yaml") as f:
            yml_obj = yaml.safe_load(f)

        obj = utils.load_from_dict(yml_obj)
        self.assertIsInstance(obj, client.models.v1_namespace.V1Namespace)

    def test_load_namespace_from_yaml(self):
        """
        Should be able to load a namespace.
        """
        obj = utils.load_from_yaml(self.yaml_path_prefix + "core-namespace.yaml")
        self.assertIsInstance(obj, client.models.v1_namespace.V1Namespace)

    def test_load_rbac_role_from_dict(self):
        """
        Should be able to load an rbac role.
        """
        with open(self.yaml_path_prefix + "rbac-role.yaml") as f:
            yml_obj = yaml.safe_load(f)

        obj = utils.load_from_dict(yml_obj)
        self.assertIsInstance(obj, client.models.v1_role.V1Role)

    def test_load_rbac_role_from_yaml(self):
        """
        Should be able to load an rbac role.
        """
        with open(self.yaml_path_prefix + "rbac-role.yaml") as f:
            yml_obj = yaml.safe_load(f)

        obj = utils.load_from_yaml(self.yaml_path_prefix + "rbac-role.yaml")
        self.assertIsInstance(obj, client.models.v1_role.V1Role)

    def test_load_non_default_namespace_from_dict(self):
        """
        Should be able to load a namespace "dep"
        """
        with open(self.yaml_path_prefix + "dep-namespace.yaml") as f:
            yml_obj = yaml.safe_load(f)

        obj = utils.load_from_dict(yml_obj)
        self.assertIsInstance(obj, client.models.v1_namespace.V1Namespace)
        self.assertEqual(obj.metadata.name, "dep")

    def test_load_non_default_namespace_from_yaml(self):
        """
        Should be able to load a namespace "dep",
        """
        obj = utils.load_from_yaml(self.yaml_path_prefix + "dep-namespace.yaml")
        self.assertIsInstance(obj, client.models.v1_namespace.V1Namespace)
        self.assertEqual(obj.metadata.name, "dep")

    def test_load_deployment_non_default_namespace_from_dict(self):
        """
        Should be able to load a namespace "dep",
        """
        with open(self.yaml_path_prefix + "dep-deployment.yaml") as f:
            yml_obj = yaml.safe_load(f)

        obj = utils.load_from_dict(yml_obj)
        self.assertIsInstance(obj, client.models.v1_deployment.V1Deployment)

    def test_load_deployment_non_default_namespace_from_yaml(self):
        """
        Should be able to load a namespace "dep",
        and then create a deployment in the just-created namespace.
        """
        obj = utils.load_from_yaml(self.yaml_path_prefix + "dep-deployment.yaml")
        self.assertIsInstance(obj, client.models.v1_deployment.V1Deployment)

    def test_load_apiservice_from_dict(self):
        """
        Should be able to load an API service.
        """
        with open(self.yaml_path_prefix + "api-service.yaml") as f:
            yml_obj = yaml.safe_load(f)

        obj = utils.load_from_dict(yml_obj)
        self.assertIsInstance(obj, client.models.v1beta1_api_service.V1beta1APIService)

    def test_load_apiservice_from_yaml(self):
        """
        Should be able to load an API service.
        """
        obj = utils.load_from_yaml(self.yaml_path_prefix + "api-service.yaml")
        self.assertIsInstance(obj, client.models.v1beta1_api_service.V1beta1APIService)

    # # Tests for creating API objects from lists
    #
    def test_load_general_list_from_dict(self):
        """
        Should be able to load a service and a deployment
        from a kind: List yaml file
        """
        with open(self.yaml_path_prefix + "list.yaml") as f:
            yml_obj = yaml.safe_load(f)

        obj = utils.load_from_dict(yml_obj)
        self.assertIsInstance(obj, list)
        self.assertEqual(len(obj), 2)
        self.assertIsInstance(obj[0], client.models.v1_service_list.V1ServiceList)
        self.assertIsInstance(obj[0].items[0], client.models.v1_service.V1Service)
        self.assertIsInstance(obj[1], client.models.v1_deployment_list.V1DeploymentList)
        self.assertIsInstance(obj[1].items[0], client.models.v1_deployment.V1Deployment)

    def test_load_general_list_from_yaml(self):
        obj = utils.load_from_yaml(self.yaml_path_prefix + "list.yaml")
        self.assertIsInstance(obj, list)
        self.assertEqual(len(obj), 2)
        self.assertIsInstance(obj[0], client.models.v1_service_list.V1ServiceList)
        self.assertIsInstance(obj[0].items[0], client.models.v1_service.V1Service)
        self.assertIsInstance(obj[1], client.models.v1_deployment_list.V1DeploymentList)
        self.assertIsInstance(obj[1].items[0], client.models.v1_deployment.V1Deployment)

    def test_load_namespace_list_from_dict(self):
        """
        Should be able to load two namespaces
        from a kind: NamespaceList yaml file
        """
        with open(self.yaml_path_prefix + "namespace-list.yaml") as f:
            yml_obj = yaml.safe_load(f)

        obj = utils.load_from_dict(yml_obj)
        self.assertIsInstance(obj, client.models.v1_namespace_list.V1NamespaceList)
        self.assertEqual(len(obj.items), 2)
        self.assertIsInstance(obj.items[0], client.models.v1_namespace.V1Namespace)
        self.assertIsInstance(obj.items[1], client.models.v1_namespace.V1Namespace)
        nmsp_1 = obj.items[0]
        self.assertIsNotNone(nmsp_1)
        nmsp_2 = obj.items[1]
        self.assertIsNotNone(nmsp_2)
        self.assertEqual(nmsp_1.metadata.name, "mock-1")
        self.assertEqual(nmsp_2.metadata.name, "mock-2")

    def test_load_namespace_list_from_yaml(self):
        """
        Should be able to load two namespaces
        from a kind: NamespaceList yaml file
        """
        obj = utils.load_from_yaml(self.yaml_path_prefix + "namespace-list.yaml")
        self.assertIsInstance(obj, client.models.v1_namespace_list.V1NamespaceList)
        self.assertEqual(len(obj.items), 2)
        self.assertIsInstance(obj.items[0], client.models.v1_namespace.V1Namespace)
        self.assertIsInstance(obj.items[1], client.models.v1_namespace.V1Namespace)
        nmsp_1 = obj.items[0]
        self.assertIsNotNone(nmsp_1)
        nmsp_2 = obj.items[1]
        self.assertIsNotNone(nmsp_2)
        self.assertEqual(nmsp_1.metadata.name, "mock-1")
        self.assertEqual(nmsp_2.metadata.name, "mock-2")

    # Tests for multi-resource yaml objects
    def test_load_from_multi_resource_yaml(self):
        """
        Should be able to load a service and a replication controller
        from a multi-resource yaml file
        """
        obj = utils.load_from_yaml(self.yaml_path_prefix + "multi-resource.yaml")
        self.assertIsInstance(obj, list)
        self.assertEqual(len(obj), 2)
        self.assertIsInstance(obj[0], client.models.v1_service.V1Service)
        self.assertIsInstance(
            obj[1], client.models.v1_replication_controller.V1ReplicationController
        )

    def test_load_from_list_in_multi_resource_yaml(self):
        """
        Should be able to load the items in the PodList and a deployment
        specified in the multi-resource file
        """
        obj = utils.load_from_yaml(
            self.yaml_path_prefix + "multi-resource-with-list.yaml"
        )
        self.assertIsInstance(obj, list)
        self.assertEqual(len(obj), 2)
        self.assertIsInstance(obj[0], client.models.v1_pod_list.V1PodList)
        self.assertEqual(len(obj[0].items), 2)
        self.assertIsInstance(obj[0].items[0], client.models.v1_pod.V1Pod)
        self.assertIsInstance(obj[1], client.models.v1_deployment.V1Deployment)

    def test_load_namespaced_apps_deployment_from_yaml(self):
        """
        Should be able to load an apps/v1beta1 deployment
        in a test namespace.
        """
        obj = utils.load_from_yaml(self.yaml_path_prefix + "apps-deployment.yaml")
        self.assertIsInstance(obj, client.models.v1_deployment.V1Deployment)

    # Test json files
    def test_load_pod_list_from_json(self):
        """
        Should be able to load a list of pods objects
        """
        pods = utils.load_from_json(self.json_path_prefix + "pod-list.json")
        self.assertIsInstance(pods, client.models.v1_pod_list.V1PodList)
        self.assertEqual(len(pods.items), 2)
        for pod in pods.items:
            self.assertIsInstance(pod, client.models.v1_pod.V1Pod)
            self.assertEqual(pod.metadata.namespace, "default")
            self.assertIsInstance(pod.metadata.creation_timestamp, datetime)

    def test_load_pod_list_with_klass_from_json(self):
        """
        Should be able to load a list of pods objects
        """
        pods = utils.load_from_json(self.json_path_prefix + "pod-list.json", klass="V1PodList")
        self.assertIsInstance(pods, client.models.v1_pod_list.V1PodList)
        self.assertEqual(len(pods.items), 2)
        for pod in pods.items:
            self.assertIsInstance(pod, client.models.v1_pod.V1Pod)
            self.assertEqual(pod.metadata.namespace, "default")
            self.assertIsInstance(pod.metadata.creation_timestamp, datetime)

    def test_load_pod_from_json(self):
        """
        Should be able to load a pod object
        """
        pod = utils.load_from_json(self.json_path_prefix + "pod.json")
        self.assertIsInstance(pod, client.models.v1_pod.V1Pod)
        self.assertEqual(pod.metadata.name, "nginx-deployment-54f57cf6bf-hpphg")
        self.assertEqual(pod.metadata.namespace, "default")
        self.assertIsInstance(pod.metadata.creation_timestamp, datetime)

    def test_load_pod_with_klass_from_json(self):
        """
        Should be able to load a pod object
        """
        pod = utils.load_from_json(self.json_path_prefix + "pod.json", klass="V1Pod")
        self.assertIsInstance(pod, client.models.v1_pod.V1Pod)
        self.assertEqual(pod.metadata.name, "nginx-deployment-54f57cf6bf-hpphg")
        self.assertEqual(pod.metadata.namespace, "default")
        self.assertIsInstance(pod.metadata.creation_timestamp, datetime)

    def test_load_deployment_from_json(self):
        """
        Should be able to load a deployment object
        """
        deployment = utils.load_from_json(self.json_path_prefix + "deployment.json")
        self.assertIsInstance(deployment, client.models.v1_deployment.V1Deployment)
        self.assertEqual(deployment.metadata.namespace, "default")
        self.assertIsInstance(deployment.metadata.creation_timestamp, datetime)

    def test_load_replicaset_from_json(self):
        """
        Should be able to load a replicaset object
        """
        replicaset = utils.load_from_json(self.json_path_prefix + "replicaset.json")
        self.assertIsInstance(replicaset, client.models.v1_replica_set.V1ReplicaSet)
        self.assertEqual(replicaset.metadata.name, "curl3-748c7587cf")
        self.assertEqual(replicaset.metadata.namespace, "default")
        self.assertIsInstance(replicaset.metadata.creation_timestamp, datetime)

    # Try non-namespaced objects
    def test_load_namespace_from_json(self):
        """
        Should be able to load a namespace objects
        """
        namespace = utils.load_from_json(self.json_path_prefix + "namespace.json")
        self.assertIsInstance(namespace, client.models.v1_namespace.V1Namespace)
        self.assertIsInstance(namespace.metadata.creation_timestamp, datetime)
        self.assertEqual(namespace.kind, "Namespace")
        self.assertEqual(namespace.metadata.name, "default")

    def test_load_node_from_json(self):
        """
        Should be able to load a node object
        """
        node = utils.load_from_json(self.json_path_prefix + "node.json")
        self.assertIsInstance(node, client.models.v1_node.V1Node)
        self.assertIsInstance(node.metadata.creation_timestamp, datetime)
        self.assertEqual(node.kind, "Node")
        self.assertEqual(node.metadata.name, "minikube")

    def test_load_apiservice_from_json(self):
        """
        Should be able to load an apiservice objects
        """
        apiservice = utils.load_from_json(self.json_path_prefix + "apiservice.json")
        self.assertIsInstance(apiservice, client.models.v1_api_service.V1APIService)
        self.assertIsInstance(apiservice.metadata.creation_timestamp, datetime)
        self.assertEqual(apiservice.kind, "APIService")
        self.assertEqual(apiservice.metadata.name, "v1.")

    # Try different failures
    def test_load_apiservice_from_json_fail(self):
        """
        Should not be able to load an apiservice object
        """

        with self.assertRaises(ValueError) as cm:
            apiservice = utils.load_from_json(
                self.json_path_prefix + "apiservice-fail.json"
            )
        exp_error = "Invalid value for `service`, must not be `None`"
        self.assertEqual(exp_error, str(cm.exception))

    def test_load_failure_from_bad_dict(self):
        """
        Try with a couple of of malformed dictionaries
        """
        # Omit kind and apiVersion
        # use keys as expected str in exceptions
        bad_dicts = {
            "'apiVersion'": {"BadDict": 12345, "kind": "Pod"},
            "'kind'": {"BadDict": 12345, "apiVersion": "v1"},
        }

        for k in bad_dicts:
            with self.assertRaises(KeyError) as cm:
                utils.load_from_dict(bad_dicts[k])

            self.assertEqual(k, str(cm.exception))

    def test_load_failure_from_bad_json(self):
        """
        Try with a malformed kind string
        """
        with self.assertRaises(AttributeError) as cm:
            utils.load_from_json(self.json_path_prefix + "bad-data.json")

        exp_error = "has no attribute 'CoreV1badApi'"
        self.assertIn(exp_error, str(cm.exception))
