import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# def test_heplify_is_running(host):
#     cmd = host.service('heplify')
#     assert cmd.is_running
#     assert cmd.is_enabled
