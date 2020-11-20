import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sftp_is_running(host):
    cmd = host.service('sshd_sftp')
    assert cmd.is_running
    assert cmd.is_enabled


def test_sftp_localhost_connection(host):
    cmd = host.run("sftp -P 2020 test01@localhost")
    assert cmd.succeeded


def test_sftp_localhost_download(host):
    host.run("echo testing_content > /chroot/test01/testfile")
    cmd = host.run("sftp -P 2020 test01@localhost:testfile /opt/testfile")
    assert cmd.succeeded
    assert host.file("/opt/testfile").contains("testing_content")


def test_sftp_localhost_upload(host):
    host.run("mkdir /chroot/test01/upload \
        chown test01:sftp /chroot/test01/upload")
    cmd = host.run("echo 'put /etc/shadow' |\
        sftp -P2020 test01@localhost:upload")
    assert cmd.succeeded
    uploaded = host.file("/chroot/test01/upload/shadow")
    assert uploaded.exists
    assert uploaded.contains("root:*")
