# Provisioning VM With KVM using Ansible
  
## requirements

- python 3
- KVM

to install the python requirements run
```
$ pip install -r requirements.txt
```
## Install and setup Ansible

For a simpler and cleaner Ansible install use a python virtual-env. In order to do so create a directory: 

```
$ mkdir Ansible
$ python3 -m venv Ansible
```

So enable the virtual environment using :
```
$ source Ansible/bin/activate
```
now that you have the venv enabled, it's time to install Ansible (Note: Ansible will be available only in the virtual environment): 
```
$ pip3 install -r venv-requirements.txt
```
## Use the playbooks 

Now that everything is ready you can run the playbook `create-vm.yml`

##### create VMs  
```
$ ansible-playbook -i Inventory/localVars.inv create-vm.yml --ask-become-pass
```
##### setup VM and install docker

Check the IPs taken by the VMs and put them in `/etc/ansible/hosts`
```
virsh net-dhcp-leases default
```

`/etc/ansible/hosts` example:
```
[nodes]
<YOUR_IP_ADDRESS> ansible_user=docker
```

run the `check-vm.yml` to check the VMs status and install docker
```
$ ansible-playbook -i Inventory/localVars.inv check-vm.yml --ask-become-pass
```
