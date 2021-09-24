# Make coding more python3-ish, this is required for contributions to Ansible
from __future__ import (absolute_import, division, print_function)
import requests
from ansible.plugins.callback import CallbackBase
__metaclass__ = type

# not only visible to ansible-doc,
# it also 'declares' the options the plugin requires and how to configure them.
DOCUMENTATION = '''
callback: healthchecks
callback_type: notification
requirements:
    - enable in configuration
short_description: Sends status to healthchecks.io
# for collections, use the collection version, not the Ansible version
version_added: "0.1"
description:
    - This callback notifies healthchecks.io for successes and failures
options:
  url:
    description: Healthchecks URL
    default: "https://hc-ping.com"
    env:
      - name: HEALTHCHECKS_URL
    ini:
      - section: callback_healthchecks
        key: url
    version_added: 0.1
  uuid:
    description: Healthchecks UUID
    required: True
    env:
      - name: HEALTHCHECKS_UUID
    ini:
      - section: callback_healthchecks
        key: uuid
    version_added: 0.1
'''


class CallbackModule(CallbackBase):
    """
    This callback module notifies healthchecks.io.
    """
    CALLBACK_VERSION = 0.1
    CALLBACK_TYPE = 'notification'
    CALLBACK_NAME = 'healthchecks'

    # only needed if you ship it and don't want to enable by default
    CALLBACK_NEEDS_ENABLED = False

    def __init__(self, display=None):

        # make sure the expected objects are present,
        # calling the base's __init__
        super(CallbackModule, self).__init__(display=display)

        self.uuid = None
        self.url = None

    def set_options(self, task_keys=None, var_options=None, direct=None):
        super(CallbackModule, self).set_options(
            task_keys=task_keys, var_options=var_options, direct=direct)

        self.url = self.get_option('url')
        self.uuid = self.get_option('uuid')

        if self.uuid is None:
            self.disabled = True
            self._display.warning('Healthchecks UUID not provided')

    def call_healthchecks(self, call='', text=''):
        try:
            requests.get(self.url + "/" + self.uuid +
                         call, data=text, timeout=10)
        except requests.RequestException as e:
            # Log ping failure here...
            print("Call failed: %s" % e)

    def v2_playbook_on_start(self, playbook):
        self.call_healthchecks(call='/start', text='Starting playbook Run')

    def v2_playbook_on_stats(self, stats):
        total_tasks = 0
        total_updated = 0
        total_errors = 0
        error_hosts = []
        for host in stats.processed:
            # Aggregations for the event text
            summary = stats.summarize(host)
            total_tasks += sum([summary['ok'],
                               summary['failures'], summary['skipped']])
            total_updated += summary['changed']
            errors = sum([summary['failures'], summary['unreachable']])
            if errors > 0:
                error_hosts.append(
                    (host, summary['failures'], summary['unreachable']))
                total_errors += errors

        # If errors exists, then call fail with summary
        if total_errors > 0:
            self.call_healthchecks(call='/fail', text=summary)
        else:
            self.call_healthchecks(text=summary)
