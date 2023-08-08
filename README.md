# sysctl

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&amp;logoColor=white)](https://github.com/rolehippie/sysctl)
[![General Workflow](https://github.com/rolehippie/sysctl/actions/workflows/general.yml/badge.svg)](https://github.com/rolehippie/sysctl/actions/workflows/general.yml)
[![Readme Workflow](https://github.com/rolehippie/sysctl/actions/workflows/readme.yml/badge.svg)](https://github.com/rolehippie/sysctl/actions/workflows/readme.yml)
[![Galaxy Workflow](https://github.com/rolehippie/sysctl/actions/workflows/galaxy.yml/badge.svg)](https://github.com/rolehippie/sysctl/actions/workflows/galaxy.yml)
[![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/sysctl)](https://github.com/rolehippie/sysctl/blob/master/LICENSE)
[![Ansible Role](https://img.shields.io/badge/role-rolehippie.sysctl-blue)](https://galaxy.ansible.com/rolehippie/sysctl)

Ansible role to configure sysctl settings.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [sysctl_defaults](#sysctl_defaults)
  - [sysctl_extra](#sysctl_extra)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.10`


## Default Variables

### sysctl_defaults

List of global sysctl settings

#### Default value

```YAML
sysctl_defaults: []
```

#### Example usage

```YAML
sysctl_defaults:
  - name: net.ipv4.ip_forward
    value: 1
  - name: net.ipv6.conf.all.forwarding
    value: 1
    ignoreerrors: True
    reload: True
    sysctl_file: /etc/sysctl.conf
    sysctl_set: True
  - name: kernel.panic
    state: absent
```

### sysctl_extra

List of extra sysctl settings

#### Default value

```YAML
sysctl_extra: []
```

#### Example usage

```YAML
sysctl_extra:
  - name: net.ipv4.ip_forward
    value: 1
  - name: net.ipv6.conf.all.forwarding
    value: 1
    ignoreerrors: True
    reload: True
    sysctl_file: /etc/sysctl.conf
    sysctl_set: True
  - name: kernel.panic
    state: absent
```

## Discovered Tags

**_sysctl_**


## Dependencies

- None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
