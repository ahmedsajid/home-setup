# Repo for home setup
I have choosen to use ansible pull mechanism as it doesn't require a controller.
Also ensures that my setup is always up to date.
And, my home setup can run on unrealiable hardware with a small RTO.

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
