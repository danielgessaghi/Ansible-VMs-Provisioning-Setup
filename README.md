# Provisioning VM With KVM using Ansible
  
## requirements

- python 3
- KVM

to install the python requirements run
```
$ pip install requirements.txt -y
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
now that you have the venv enabled, i'ts time to install Ansible (Note: Ansible will be available only in the virtual environment): 
```
$ pip3 install ansible
```

## Use the playbooks 

Now that everything is ready you can run the playbook  

##### create VMs  
```
$ ansible-playbook -i Inventory/localVars.inv create-vm.yml -vvvv --user=daniel --ask-become-pass
``` 
##### setup VM and install docker
```
$ ansible-playbook -i Inventory/localVars.inv check-vm.yml -vvvv --user=daniel --ask-become-pass
```
