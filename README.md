# Repo for home setup

[![Checks](https://github.com/ahmedsajid/home-setup/workflows/checks/badge.svg)](https://github.com/ahmedsajid/home-setup/actions?query=workflow%3A%22checks%22)
[![License](https://img.shields.io/github/license/ahmedsajid/home-setup)](LICENSE)


I have chosen to use ansible pull mechanism as it doesn't require a controller.
Also ensures that my setup is always up to date.
And, my home setup can run on unreliable hardware with a small RTO (cattle NOT pet).

## First install (ansible-pull setup)
```
cd ansible
ansible-playbook -i inventory ansible_pull.yml --ask-become-pass
```

## Running services

Once the cronjob has been setup, there should be following available services provided by the server:
- Emby
- Pihole (+Unbound) - [Coming soon](https://github.com/ahmedsajid/home-setup/issues/28)
- Grafana - [Coming soon](https://github.com/ahmedsajid/home-setup/issues/30)
- Wireguard - [Coming soon](https://github.com/ahmedsajid/home-setup/issues/29)
- Web Aria2 - [Coming soon](https://github.com/ahmedsajid/home-setup/issues/31)
- NAS to external hdd backup - [Coming soon](https://github.com/ahmedsajid/home-setup/issues/32)
- HTTPs access to services (Nginx, LetsEncrypt, NoIP) - [Coming soon](https://github.com/ahmedsajid/home-setup/issues/33)