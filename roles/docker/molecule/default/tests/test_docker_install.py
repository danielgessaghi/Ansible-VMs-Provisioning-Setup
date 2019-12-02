import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_user_is_allowed(host):
    passwd = host.file("/etc/passwd") 
    assert passwd.contains("docker")
    assert passwd.user == "docker"
    assert passwd.group == "docker"


def test_docker_is_installed(host): 
    dockerd = host.service("dockerd")
    assert dockerd.is_running
    assert dockerd.is_enabled
