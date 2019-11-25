# Ansible-VMs-Provisioning-Setup

## Install Ansible

```
$ pip3 install --user ansible
```

pip3 install --upgrade ansible 
ansible-galaxy collection install crivetimihai.virtualization

$ ansible-playbook -vvv -i Inventory/localVars.inv playbook.yml