# -------------------------------------------------------------------
# ? Copywright (c) 2022 NeuralNOD Inc.
#
#   Mnemonic:   Dockerfile
#   Abstract:   The dockerfile for creating the base environment
#               image as required by the organization. This image can
#               be imported by other images by directly using `FROM`
#               command.
#               TODO create a `docker-compose.yml` for configuration.
#               ! Currently this is not fully configured, need help.
#               The file is kept as simple as possible, just build
#               the image using:
#                 docker build --tag baseimage:latest .
#
#   Date:       22 December 2022
#   Author:     Debmalya Pramanik
# -------------------------------------------------------------------

FROM ubuntu:22.04

# add maintainer and other label environment tags,
# ? LABEL tag is also beneficial while creating github packages
LABEL maintainer="nxLogics <neuralnod@outlook.com>"

# TODO create a list of environment variables as required

# ? (OPTIONAL): Let's track the image create and other information
# using a `INIT_FILE` created as below. save other information.
ENV INIT_FILE /root/INIT_FILE
RUN touch ${INIT_FILE} \
  && echo "$(date) : Image Created." >> ${INIT_FILE}

# TODO expose a list of ports from the base environment

# ! (CONFIGURE): get and install basic command line tools and library
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list \
  && apt update && apt -y upgrade \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    nano \
    net-tools \
    build-essential \
    software-properties-common \
  && apt install -y curl git htop man wget neofetch \
  && apt clean \
  && rm -rf /var/lib/apt/lists/* \
  && echo "$(date) : Additional Tools Installed." >> ${INIT_FILE}

# ! (CONFIGURE) (OPTIONAL): setup bash aliases and git aliases
# * also configure the git username and email address
ADD root/.gitconfig ~/.gitconfig
ADD root/.bash_aliases ~/.bash_aliases

# ? set working directory to /root/ folder
WORKDIR /root/
RUN echo "$(date) : All setup from base image is complete." >> ${INIT_FILE}
