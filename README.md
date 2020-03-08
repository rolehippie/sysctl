# sysctl

[![Build Status](https://cloud.drone.io/api/badges/rolehippie/sysctl/status.svg)](https://cloud.drone.io/rolehippie/sysctl)

Ansible role to configure sysctl

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

- None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
