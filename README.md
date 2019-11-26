# Ansible-VMs-Provisioning-Setup

## requirements
- python 3
- KVM
- pip

for install the resto fo the requirements.txt run 

## Install Ansible


create a python virtual env

create a directory
```
mkdir Ansible
python3 -m venv Ansible
```
quindi per abilitarlo: 
```
source Ansible/bin/activate
```

```
$ pip3 install --user ansible
```



$ ansible-playbook -i Inventory/localVars.inv check-vm.yml -vvvv --user=daniel --ask-become-pass
$ ansible-playbook -i Inventory/localVars.inv create-vm.yml -vvvv --user=daniel --ask-become-pass
