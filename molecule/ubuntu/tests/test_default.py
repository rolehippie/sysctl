import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("name,value", [
    ("net.ipv4.ip_forward", 1),
    ("net.ipv6.conf.all.forwarding", 1),
    ("kernel.panic", 10),
])
def test_defined_values(host, name, value):
    assert host.sysctl(name) == value
