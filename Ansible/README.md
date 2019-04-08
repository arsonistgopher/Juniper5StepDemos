## Ansible

Some knowledge of Ansible is required for this demonstration. You're also required to have the Ansible module `Juniper.junos` installed from Ansible Galaxy. You're also required to install "JSNAPy" in order to run the pre and post tests.

Ensure your host settings are correct along with the SSH keys. I've left them in this directory for placeholder reasons. This will work on a vQFX and a phsyical QFX.

The `pre` playbook runs the collision tests and generates the configuration to push.
The `post` playbook merges the changes and then runs the post checks.

`ansible-playbook pb.pre.yml --extra-vars target="demo01"`
`ansible-playbook pb.post.yml --extra-vars target="demo01"`


