# work

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/sysctl) [![Testing Build](https://github.com/rolehippie/sysctl/workflows/testing/badge.svg)](https://github.com/rolehippie/sysctl/actions?query=workflow%3Atesting) [![Readme Build](https://github.com/rolehippie/sysctl/workflows/readme/badge.svg)](https://github.com/rolehippie/sysctl/actions?query=workflow%3Areadme) [![Galaxy Build](https://github.com/rolehippie/sysctl/workflows/galaxy/badge.svg)](https://github.com/rolehippie/sysctl/actions?query=workflow%3Agalaxy) [![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/sysctl)](https://github.com/rolehippie/sysctl/blob/master/LICENSE) 

Ansible role to configure sysctl settings. 

## Sponsor 

[![Proact Deutschland GmbH](https://proact.eu/wp-content/uploads/2020/03/proact-logo.png)](https://proact.eu) 

Building and improving this Ansible role have been sponsored by my employer **Proact Deutschland GmbH**.

## Table of content

* [Default Variables](#default-variables)
  * [sysctl_defaults](#sysctl_defaults)
  * [sysctl_extra](#sysctl_extra)
* [Dependencies](#dependencies)
* [License](#license)
* [Author](#author)

---

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

## Dependencies

* None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
