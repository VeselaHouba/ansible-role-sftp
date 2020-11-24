# Ansible Role: sFTP

[![CI](https://github.com/VeselaHouba/ansible-role-sftp/workflows/CI/badge.svg?event=push)](https://github.com/VeselaHouba/ansible-role-sftp/actions?query=workflow%3ACI)

Ansible role for sftp.

- sFTP instance is standalone port and independent on sshd.
- Only ssh key authentication is allowed.
- Users are created on OS level with minimal rights and are supposed to be sftp ONLY
- Be careful not to overwrite your OS level users.
- Auth keys don't sit in user's dir, but in separate dir.


## Tasks
### Variables:
- `sftp_sshd_config_file`: Where the config will be saved. Default `/etc/ssh/sshd_sftp_config`
- `sftp_port`: On which port he sftp will listen. Default `2020`
- `sftp_service_name`: Service name used in systemd. Default `sshd_sftp`
- `sftp_auth_files_dir`: Where the auth keyfiles are stored. Default `/etc/ssh/auth_files`
- `sftp_group`: All sftp users will share this group. Default `sftp`
- `sftp_users`: List of sftp user definition. See below. Default `[]`

### Examples
```yaml
sftp_users:
 - name: test01
   chroot_dir: /chroot/tes01
   ssh_key: |
     ssh-rsa blablabla comment1
     ssh-rsa blablabla comment2
```

**NOTE**

All components of the **chroot_dir** must be root-owned directories that are not writable by any other user or any group at all.

## Requirements
- Tested with molecule on Debian 9,10, Ubuntu 18.04,20.04
- Ansible 2.10


## Ansible Galaxy
https://galaxy.ansible.com/veselahouba/sftp
```
ansible-galaxy install veselahouba.sftp
```
