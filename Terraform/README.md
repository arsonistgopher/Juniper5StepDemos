## Terraform

You are required to have Terraform installed and this currently is available on MacOSX. The reason for this is the Terraform code is still under-development and you have a limited capability binary in this directory which is the Junos module.

Terraform is being exercised in a simple manner and we're not doing anything fancy here like bringing in variables externally or through data sources.

`jsnapy --snapcheck pre -f pre.yml`
`terraform init`
`terraform plan`
`terraform apply -auto-approve`
`jsnapy --snapcheck post -f post.yml`

You could also run `terraform destroy` if you want to remove the Terraform configured aspects from the test node.



