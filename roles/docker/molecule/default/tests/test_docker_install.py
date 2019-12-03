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


def test_user_root_is_allowed(host):
    passwd = host.file("/etc/passwd")

    assert passwd.contains("root")
    assert passwd.user == "root"
    assert passwd.group == "root"


def test_docker_repository_exists(host):
    f = host.file('/etc/yum.repos.d/docker-ce.repo')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_docker_is_installed(host):
    dockerd = host.service("docker")

    assert dockerd.is_running
    assert dockerd.is_enabled
