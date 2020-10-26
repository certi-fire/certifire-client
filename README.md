# CertiFire

## CertiFire scripts for Lemur

### usage:

`main.py [-h] {get,new} ...`

positional arguments:
  {get,new}

optional arguments:
  -h, --help  show this help message and exit

### get usage:

`main.py get [-h] key`

positional arguments:
  key         Certificate ID or Search string

optional arguments:
  -h, --help  show this help message and exit

### new usage:

`main.py new [-h] [-o OWNER] [-a AUTH] n`

positional arguments:
  n           Certificate name (fqdn)

optional arguments:
  -h, --help  show this help message and exit
  -o OWNER    Owner of certificate
  -a AUTH     Issuing Authority
