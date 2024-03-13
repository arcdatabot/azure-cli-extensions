# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
import unittest

from azext_cloudservice.tests import try_manual
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from azure.cli.testsdk.scenario_tests import AllowLargeResponse

TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Test class for Scenario
@try_manual
class CloudServiceScenarioTest(ScenarioTest):

    @unittest.skip('skip')
    @ResourceGroupPreparer(name_prefix='cli_test_cloud_service_create_')
    def test_cloud_service_create(self, resource_group):
        self.cmd('cloud-service create -g {rg} -n cs '
                 '--roles ContosoFrontend:Standard_D1_v2:1:Standard ContosoBackend:Standard_D1_v2:1:Standard '
                 '--package-url packageurl '
                 '--configuration config '
                 '--load-balancer-configurations myLoadBalancer:myfe:publicip:: '
                 'myLoadBalancer2:myfe2::subnetid:privateip '
                 '--secrets vault0:cert0:cert1 vault1:cert2:cert3:cert4 '
                 '--extensions "@extensions.json"')

    @unittest.skip('skip')
    @ResourceGroupPreparer(name_prefix='cli_test_cloud_service_')
    def test_cloud_service(self, rg):
        self.cmd('cloud-service show -g {rg} -n cs')
        self.cmd('cloud-service show-instance-view -g {rg} -n cs')
        self.cmd('cloud-service list -g {rg}')
        self.cmd('cloud-service list-all')
        self.cmd('cloud-service power-off -g {rg} -n cs')
        self.cmd('cloud-service rebuild -g {rg} -n cs')
        self.cmd('cloud-service reimage -g {rg} -n cs')
        self.cmd('cloud-service start -g {rg} -n cs')
        self.cmd('cloud-service restart -g {rg} -n cs')
        self.cmd('cloud-service delete -g {rg} -n cs')

    @unittest.skip('skip')
    @ResourceGroupPreparer(name_prefix='cli_test_cloud_service_role_')
    def test_cloud_service_role(self, rg):
        self.cmd('cloud-service role list')
        self.cmd('cloud-service role show -g {rg} --cloud-service-name cs --role-name role')

    @unittest.skip('skip')
    @ResourceGroupPreparer(name_prefix='cli_test_cloud_service_role_instance_')
    def test_cloud_service_role_instance(self, rg):
        self.cmd('cloud-service role-instance list')
        self.cmd('cloud-service role-instance show -g {rg}')
        self.cmd('cloud-service role-instance show-instance-view -g {rg}')
        self.cmd('cloud-service role-instance show-remote-desktop-file')
        self.cmd('cloud-service role-instance delete -g {rg}')
        self.cmd('cloud-service role-instance rebuild -g {rg}')
        self.cmd('cloud-service role-instance reimage -g {rg}')
        self.cmd('cloud-service role-instance restart -g {rg}')

    @unittest.skip('skip')
    @ResourceGroupPreparer(name_prefix='cli_test_cloud_service_update_domain_')
    def test_cloud_service_update_domain(self, rg):
        self.cmd('cloud-service update-domain list-update-domain')
        self.cmd('cloud-service update-domain show-update-domain')
        self.cmd('cloud-service update-domain walk-update-domain')

    @AllowLargeResponse()
    @ResourceGroupPreparer(name_prefix='cli_test_cloud_service_os_version_and_os_family')
    def test_cloud_service_os_version_and_os_family(self):
        self.cmd('cloud-service os-version list -l eastus', checks=[
            self.check('[0].type', 'Microsoft.Compute/locations/cloudServiceOSVersions')
        ])
        self.cmd('cloud-service os-version show -n WA-GUEST-OS-5.78_202302-01 -l eastus', checks=[
            self.check('type', 'Microsoft.Compute/locations/cloudServiceOSVersions')
        ])
        self.cmd('cloud-service os-family list -l eastus', checks=[
            self.check('[0].type', 'Microsoft.Compute/locations/cloudServiceOSFamilies')
        ])
        self.cmd('cloud-service os-family show -n 5 -l eastus', checks=[
            self.check('type', 'Microsoft.Compute/locations/cloudServiceOSFamilies')
        ])
