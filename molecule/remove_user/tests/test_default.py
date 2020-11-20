import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sftp_is_running(host):
    cmd = host.service('sshd_sftp')
    assert cmd.is_running
    assert cmd.is_enabled


def test_sftp_localhost_connection(host):
    cmd = host.run("sftp -P 2020 test02@localhost")
    assert cmd.succeeded


def test_sftp_localhost_download(host):
    host.run("echo testing_content > /chroot/test02/testfile")
    cmd = host.run("sftp -P 2020 test02@localhost:testfile /opt/testfile")
    assert cmd.succeeded
    assert host.file("/opt/testfile").contains("testing_content")


def test_sftp_localhost_upload(host):
    host.run("mkdir -p /chroot/test02/upload && \
        chown test02:sftp /chroot/test02/upload")
    cmd = host.run("echo 'put /etc/shadow' |\
        sftp -P2020 test02@localhost:upload")
    assert cmd.succeeded
    uploaded = host.file("/chroot/test02/upload/shadow")
    assert uploaded.exists
    assert uploaded.contains("root:*")


def test_user_not_present(host):
    user = host.user('test01')
    assert not user.exists


def test_userauth_not_present(host):
    file = host.file("/etc/ssh/auth_files/test01")
    assert not file.exists


def test_sftp_localhost_connection_fails(host):
    cmd = host.run("sftp -P 2020 test01@localhost")
    assert not cmd.succeeded
