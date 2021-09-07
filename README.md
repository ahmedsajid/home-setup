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

## TODO List
- Nginx
- PiHole + Unbound
- Emby
- Wireguard
- Grafana
- LetsEncrypt (certbot)
- Web Aria2
- NAS to External HDD backup

