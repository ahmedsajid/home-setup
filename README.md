# Repo for home setup

[![Checks](https://github.com/ahmedsajid/home-setup/workflows/checks/badge.svg)](https://github.com/ahmedsajid/home-setup/actions?query=workflow%3A%22checks%22)
[![Deploy](https://healthchecks.io/badge/ddd55f41-eb2c-4f60-a543-5a9f58/pEfoA72_/deploy.svg)](https://healthchecks.io/badge/ddd55f41-eb2c-4f60-a543-5a9f58/pEfoA72_/deploy.svg)
[![License](https://img.shields.io/github/license/ahmedsajid/home-setup)](LICENSE)

I have chosen to use ansible pull mechanism as it doesn't require a controller.
Also ensures that my setup is always up to date.
And, my home setup can run on unreliable hardware with a small RTO (cattle NOT pet).

## First install (ansible-pull setup)
```
cd ansible
ansible-playbook -i inventory ansible_pull.yml --ask-become-pass
```

To enable healthchecks.io monitoring for the ansible-pull cronjob, run playbook with the extra vars specified below.
```
ansible-playbook -i inventory ansible_pull.yml --ask-become-pass -e healthchecks_enabled=true -e healthchecks_uuid=<checkUUID>
```

## Running services

Once the cronjob has been setup, there should be following available services provided by the server:
- Emby
- Pihole (+Unbound)
- Grafana
- Wireguard - [Coming soon](https://github.com/ahmedsajid/home-setup/issues/29)
- Webui Aria2
- NAS to external hdd backup - [Coming soon](https://github.com/ahmedsajid/home-setup/issues/32)
- HTTPs access to services (Nginx, LetsEncrypt, NoIP) - [Coming soon](https://github.com/ahmedsajid/home-setup/issues/33)

## Integrations

The whole work flow and repo is integrated with:
- Github Actions to perform some actions that I'm too lazy to perform, linting and checks
- healthchecks.io to monitor ansible-pull cronjob status
