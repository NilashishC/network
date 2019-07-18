#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for iosxr_lag_interfaces
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'network'
}

DOCUMENTATION = """
---
module: iosxr_lag_interfaces
version_added: 2.9
short_description: Manages attributes of LAG/Ether-Bundle interfaces on IOS-XR devices.
description:
  - This module manages the attributes of LAG/Ether-Bundle interfaces on IOS-XR devices.
author: Nilashish Chakraborty (@Nilashishc)
options:
  config:
    description: A list of link aggregation group configurations.
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Name/Identifier of the LAG/Ether-Bundle to configure.
        type: str
        required: True
      members:
        description:
          - List of member interfaces for the LAG/Ether-Bundle.
        type: list
        elements: dict
        suboptions:
          member:
            description:
              - Name of the member interface.
            type: str
          mode:
            description:
              - Specifies the mode of the operation for the member interface.
              - Mode 'active' runs LACP in active mode.
              - Mode 'on' does not run LACP over the port.
              - Mode 'passive' runs LACP in passive mode over the port.
              - Mode 'inherit' runs LACP as configured in the bundle.
            choices: ['on', 'active', 'passive']
            type: str
      mode:
        description:
          - LAG mode.
          - Mode 'active' runs LACP in active mode over the port.
          - Mode 'on' does not run LACP over the port.
          - Mode 'passive' runs LACP in passive mode over the port.
        choices: ['on', 'active', 'passive']
        type: str
      links:
        description:
          - This dict contains configurable options related to LAG/Ether-Bundle links.
        type: dict
        suboptions:
          max_active:
            description:
              - Specifies the limit on the number of links that can be active in the LAG/Ether-Bundle.
              - Refer to vendor documentation for valid values.
            type: int
          min_active:
            description:
              - Specifies the minimum number of active links needed to bring up the LAG/Ether-Bundle.
              - Refer to vendor documentation for valid values.
            type: int
      load_balancing_hash:
        description:
          - Specifies the hash function used for traffic forwarded over the LAG/Ether-Bundle.
          - Option 'dst-ip' uses the destination IP as the hash function.
          - Option 'src-ip' uses the source IP as the hash function.
        type: str
        choices: ['dst-ip', 'src-ip']
  state:
    description:
      - The state the configuration should be left in.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    default: merged
"""
EXAMPLES = """
# Using merged
#
#
# ------------
# Before state
# ------------
#
# RP/0/0/CPU0:iosxr01#show run int
# Sun Jul  7 19:42:59.416 UTC
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description "GigabitEthernet - 1"
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
# !
#
#
- name: Merge provided configuration with device configuration
  iosxr_lag_interfaces:
    config:
      - name: Bundle-Ether10
        members:
          - member: GigabitEthernet0/0/0/1
            mode: inherit
          - member: GigabitEthernet0/0/0/3
            mode: inherit
        mode: active
        links:
          max_active: 5
          min_active: 2
        load_balancing_hash: src-ip

      - name: Bundle-Ether12
        members:
          - member: GigabitEthernet0/0/0/2
            mode: passive
          - member: GigabitEthernet0/0/0/4
            mode: passive
        load_balancing_hash: dst-ip
    state: merged
#
#
# -----------------------
# Module Execution Result
# -----------------------
#
#
#
#
#
# -----------
# After state
# -----------
#
# RP/0/0/CPU0:iosxr01#show run int
# Sun Jul  7 20:51:17.685 UTC
# interface Bundle-Ether10
#  lacp mode active
#  bundle load-balancing hash src-ip
#  bundle maximum-active links 5
#  bundle minimum-active links 2
# !
# interface Bundle-Ether12
#  bundle load-balancing hash dst-ip
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
   bundle id 12 mode passive
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
#  bundle id 12 mode passive
# !
#


# Using replaced
#
#
# -------------
# Before state
# -------------
#
#
# RP/0/0/CPU0:iosxr01#sho run int
# Sun Jul  7 20:58:06.527 UTC
# interface Bundle-Ether10
#  lacp mode active
#  bundle load-balancing hash src-ip
#  bundle maximum-active links 5
#  bundle minimum-active links 2
# !
# interface Bundle-Ether12
#  bundle load-balancing hash dst-ip
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
#  bundle id 12 mode passive
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
#  bundle id 12 mode passive
# !
#
#
- name: Replace device configuration of listed Bundles with provided configurations
  iosxr_lag_interfaces:
    config:
      - name: Bundle-Ether12
        members:
          - name: GigabitEthernet0/0/0/2
        mode: passive

      - name: Bundle-Ether11
        members:
          - name: GigabitEthernet0/0/0/4
        load_balancing_hash: src-ip
    state: replaced
#
#
# -----------------------
# Module Execution Result
# -----------------------
#
#
#
#
#
#
# -----------
# After state
# -----------
#
#
# RP/0/0/CPU0:iosxr01#sh run int
# Sun Jul  7 21:22:27.397 UTC
# interface Bundle-Ether10
#  lacp mode active
#  bundle load-balancing hash src-ip
#  bundle maximum-active links 5
#  bundle minimum-active links 2
# !
# interface Bundle-Ether11
#  bundle load-balancing hash src-ip
# !
# interface Bundle-Ether12
#  lacp mode passive
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
#  bundle id 12 mode on
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
#  bundle id 11 mode on
# !
#
#


# Using overridden
#
#
# ------------
# Before state
# ------------
#
#
# RP/0/0/CPU0:iosxr01#sh run int
# Sun Jul  7 21:22:27.397 UTC
# interface Bundle-Ether10
#  lacp mode active
#  bundle load-balancing hash src-ip
#  bundle maximum-active links 5
#  bundle minimum-active links 2
# !
# interface Bundle-Ether11
#  bundle load-balancing hash src-ip
# !
# interface Bundle-Ether12
#  lacp mode passive
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
#  bundle id 12 mode on
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
#  bundle id 11 mode on
# !
#
#

- name: Overrides all device configuration with provided configuration
  iosxr_lag_interfaces:
    config:
      - name: Bundle-Ether10
        members:
          - member: GigabitEthernet0/0/0/1
            mode: inherit
          - member: GigabitEthernet0/0/0/2
            mode: inherit
        mode: active
        load_balancing_hash: dst-ip
    state: overridden
#
#
# -----------------------
# Module Execution Result
# -----------------------
#
#
#
#
#
#
# ------------
# After state
# ------------
#
#
# RP/0/0/CPU0:iosxr01#sh run int
# Sun Jul  7 21:43:04.802 UTC
# interface Bundle-Ether10
#  lacp mode active
#  bundle load-balancing hash dst-ip
# !
# interface Bundle-Ether11
# !
# interface Bundle-Ether12
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
# !
#
#


# Using deleted
#
#
# ------------
# Before state
# ------------
#
# RP/0/0/CPU0:iosxr01#sh run int
# Sun Jul  7 21:22:27.397 UTC
# interface Bundle-Ether10
#  lacp mode active
#  bundle load-balancing hash src-ip
#  bundle maximum-active links 5
#  bundle minimum-active links 2
# !
# interface Bundle-Ether11
#  bundle load-balancing hash src-ip
# !
# interface Bundle-Ether12
#  lacp mode passive
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
#  bundle id 12 mode on
# !n
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
#  bundle id 11 mode on
# !
#
#

- name: Delete attributes and members of given bundles (Note: This won't delete the bundles)
  iosxr_lag_interfaces:
    config:
      - name: Bundle-Ether10
      - name: Bundle-Ether11
      - name: Bundle-Ether12
    state: deleted

#
#
# -----------------------
# Module Execution Result
# -----------------------
#
#
#
#
#
#
#
# ------------
# After state
# ------------
# RP/0/0/CPU0:iosxr01#sh run int
# Sun Jul  7 21:49:50.004 UTC
# interface Bundle-Ether10
# !
# interface Bundle-Ether11
# !
# interface Bundle-Ether12
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
# !
#
#


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['interface Bundle-Ether10', 'lacp mode active', 'bundle maximum-active links 10']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.iosxr.argspec.lag_interfaces.lag_interfaces import Lag_interfacesArgs
from ansible.module_utils.network.iosxr.config.lag_interfaces.lag_interfaces import Lag_interfaces


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Lag_interfacesArgs.argument_spec,
                           supports_check_mode=True)

    result = Lag_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
