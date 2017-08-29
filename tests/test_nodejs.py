from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_nodejs(host):
    assert host.run('node --version').rc == 0
    assert host.run('nodejs --version').rc == 0


def test_root(host):
    assert host.run('npm --version').rc == 0
