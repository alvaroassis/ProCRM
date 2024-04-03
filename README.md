# ProCRM

Este projeto visa ser um fork do projeto da Plataforma ERP Odoo (https://github.com/odoo/odoo) customizado para atender as necessidades internas de CRM da Companhia de Tecnologia da Informação do Estado de Minas Gerais - Prodemge (www.prodemge.gov.br). Mais informações sobre o Odoo no final deste documento.

Instalação do Ambiente
----------------------

Tomando como base uma VM Ubuntu Server 22.04.4 LTS seguimos os seguintes passos para preparação:

Instalação do Docker
--------------------

1. Remoção de versões antigas:
  ```
  for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
  ```
Para uma instalação limpa pode ser necessária a exclusão de todo conteúdo existente na pasta `/var/lib/docker`.

2. Configurar o repositório `apt` do Docker:

Add Docker's official GPG key:
```
sudo apt-get update
```
```
sudo apt-get install ca-certificates curl
```
```
sudo install -m 0755 -d /etc/apt/keyrings
```
```
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
```
```
sudo chmod a+r /etc/apt/keyrings/docker.asc
```
Add the repository to Apt sources:
```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
```
sudo apt-get update
```  

> NOTA
> 
> Caso utilize uma distro devivada do Ubuntu, como por exemplo o Linux Mint, será necessário utilizar `UBUNTU_CODENAME` no lugar de `VERSION_CODENAME`.

3. Instalação dos pacotes do Docker:
```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
```

Instalando o Docker-Compose:
---------------
1. baixando o docker-compose:

```
sudo curl -SL https://github.com/docker/compose/releases/download/v2.26.0/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
```

2. Alterando permissão de execução para o comando:

```
sudo chmod +x /usr/local/bin/docker-compose
```

3. Criando link simbólico para o comando:

```
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

Instalação do Portainer Community Edition:
------------------------

1. Primeiro vamos criar o volume que o Portainer Server utilizará para armazenar sua database:

```
sudo docker volume create portainer_data
```

2. Baixando e instalando o Portainer:
>NOTA
>
>Desabilite o SELinux no servidor que está rodando o Docker. Caso contrário se necessário passar o argumento `--privileged` para o Docker quando fizer o deploy do Portainer.
>
>Caso for utilizar certificado SSL você deve passar a porta 9443 como parâmetro `-p 9443:9443` no lugar da porta 9000.

```
sudo docker run -d -p 8000:8000 -p 9000:9000 --name portainer --privileged --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
```

3. Primeiro acesso ao Portainer:

   Acesse pelo navegador a interface `http://localhost:9000` e cadastre o usuário de administração do Portainer.

Copiando o repositório do ProCRM para o Servidor do Docker:
--------------------
1. Dentro da pasta de destino no Servidor Docker, utilize o comando abaixo para baixa uma cópia do repositório do ProCRM:

```
sudo git clone https://github.com/alvaroassis/ProCRM.git
```

Criando o build da imagem do ProCRM:
----------------------------
1. Dentro da pasta do projeto, onde está o arquivo Dockerfile, execute o seguinte comando:
```
sudo docker build -t prodemge/procrm:1.0
```

Executando os containers através do docker-compose:
--------------------
1. Na pasta onde está o arquivo docker-compose.yml, execute o seguinte comando:

```
sudo docker-compose up -d
```

Iniciando o Docker do Servidor do PostgreSQL:
-----------------

1. Utilize o comando abaixo para iniciar fazer o deploy do docker do banco de dados postgreSQL:
```
sudo docker run -d -v procrm-db-data:/var/lib/postgresql/data -e POSTGRES_USER=procrm -e POSTGRES_PASSWORD=procrm -e POSTGRES_DB=procrmdb --name db postgres:15
```

Executando o container de aplicação do ProCRM:
------------
1. Utilize o comando abaixo para subir o container passando o volume onde serão armazenados os dados da aplicação:

```
sudo docker run -d -v procrm-data:/var/lib/odoo --link db:db prodemge/procrm:1.0
```
-------------------------------------------------
[![Build Status](https://runbot.odoo.com/runbot/badge/flat/1/master.svg)](https://runbot.odoo.com/runbot)
[![Tech Doc](https://img.shields.io/badge/master-docs-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/documentation/17.0)
[![Help](https://img.shields.io/badge/master-help-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/forum/help-1)
[![Nightly Builds](https://img.shields.io/badge/master-nightly-875A7B.svg?style=flat&colorA=8F8F8F)](https://nightly.odoo.com/)

## Odoo
----

Odoo is a suite of web based open source business apps.

The main Odoo Apps include an <a href="https://www.odoo.com/page/crm">Open Source CRM</a>,
<a href="https://www.odoo.com/app/website">Website Builder</a>,
<a href="https://www.odoo.com/app/ecommerce">eCommerce</a>,
<a href="https://www.odoo.com/app/inventory">Warehouse Management</a>,
<a href="https://www.odoo.com/app/project">Project Management</a>,
<a href="https://www.odoo.com/app/accounting">Billing &amp; Accounting</a>,
<a href="https://www.odoo.com/app/point-of-sale-shop">Point of Sale</a>,
<a href="https://www.odoo.com/app/employees">Human Resources</a>,
<a href="https://www.odoo.com/app/social-marketing">Marketing</a>,
<a href="https://www.odoo.com/app/manufacturing">Manufacturing</a>,
<a href="https://www.odoo.com/">...</a>

Odoo Apps can be used as stand-alone applications, but they also integrate seamlessly so you get
a full-featured <a href="https://www.odoo.com">Open Source ERP</a> when you install several Apps.

Getting started with Odoo
-------------------------

For a standard installation please follow the <a href="https://www.odoo.com/documentation/17.0/administration/install/install.html">Setup instructions</a>
from the documentation.

To learn the software, we recommend the <a href="https://www.odoo.com/slides">Odoo eLearning</a>, or <a href="https://www.odoo.com/page/scale-up-business-game">Scale-up</a>, the <a href="https://www.odoo.com/page/scale-up-business-game">business game</a>. Developers can start with <a href="https://www.odoo.com/documentation/17.0/developer/howtos.html">the developer tutorials</a>
