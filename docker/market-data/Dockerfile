# -------------------------------------------------------------------
# ? Copywright (c) 2022 NeuralNOD Inc.
#
#   Mnemonic:   Dockerfile
#   Abstract:   Extends from the base image, this file is designed
#               for ETL tools for IEX data.
#               TODO create a `docker-compose.yml` for configuration.
#               ! Currently this is not fully configured, need help.
#               The file is kept as simple as possible, just build
#               the image using:
#                 docker build --tag baseimage:latest .
#
#   Date:       22 December 2022
#   Author:     Debmalya Pramanik
# -------------------------------------------------------------------

FROM baseimage:latest

# configure and install `chromedriver` and supported libraries
# https://stackoverflow.com/a/32139981/6623589
RUN \
  apt update && apt -y upgrade \
  && apt install -y unzip xvfb libxi6 libgconf-2-4 \
  && apt install -y default-jdk \
  && curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add \
  && bash -c "echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list.d/google-chrome.list" \
  && apt update && apt -y upgrade \
  && apt -y install chromium-chromedriver \
  && echo "$(date) : Chromium Driver is now Installed." >> ${INIT_FILE} \
  && find / -type f -name chromedriver  >> ${INIT_FILE}
