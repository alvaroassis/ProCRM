FROM ubuntu:jammy
MAINTAINER Alvaro de Assis <alvaro.assis@prodemge.gov.br>

SHELL ["/bin/bash", "-xo", "pipefail", "-c"]

# Generate locale C.UTF-8 for postgres and general locale data
# ENV LANG en_US.UTF-8
ENV TZ America/Sao_Paulo
ENV LANG pt_BR.UTF-8
RUN \
  apt-get clean && \
  apt-get update && \
  apt-get install -y locales tzdata && \
  rm -rf /var/lib/apt/lists/* && \
  ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
  locale-gen pt_BR.UTF-8 && \
  dpkg-reconfigure -f noninteractive locales && \
  dpkg-reconfigure -f noninteractive tzdata
ENV LC_ALL pt_BR.UTF-8

# Retrieve the target architecture to install the correct wkhtmltopdf package
ARG TARGETARCH

# Install some deps, lessc and less-plugin-clean-css, and wkhtmltopdf

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        dirmngr \
        fonts-noto-cjk \
        gnupg \
        libssl-dev \
        node-less \
        npm \
        python3-magic \
        python3-num2words \
        python3-odf \
        python3-pdfminer \
        python3-pip \
        python3-phonenumbers \
        python3-pyldap \
        python3-qrcode \
        python3-renderpm \
        python3-setuptools \
        python3-slugify \
        python3-vobject \
        python3-watchdog \
        python3-xlrd \
        python3-xlwt \
        python3-wheel \
        build-essential \
        autoconf \
        libtool \
        pkg-config \
        python3-dev \
        libldap2-dev \
        libsasl2-dev \
        xz-utils && \
    if [ -z "${TARGETARCH}" ]; then \
        TARGETARCH="$(dpkg --print-architecture)"; \
    fi; \
    WKHTMLTOPDF_ARCH=${TARGETARCH} && \
    case ${TARGETARCH} in \
    "amd64") WKHTMLTOPDF_ARCH=amd64 && WKHTMLTOPDF_SHA=967390a759707337b46d1c02452e2bb6b2dc6d59  ;; \
    "arm64")  WKHTMLTOPDF_SHA=90f6e69896d51ef77339d3f3a20f8582bdf496cc  ;; \
    "ppc64le" | "ppc64el") WKHTMLTOPDF_ARCH=ppc64el && WKHTMLTOPDF_SHA=5312d7d34a25b321282929df82e3574319aed25c  ;; \
    esac \
    && curl -o wkhtmltox.deb -sSL https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-3/wkhtmltox_0.12.6.1-3.jammy_${WKHTMLTOPDF_ARCH}.deb \
    && echo ${WKHTMLTOPDF_SHA} wkhtmltox.deb | sha1sum -c - \
    && apt-get install -y --no-install-recommends ./wkhtmltox.deb \
    && rm -rf /var/lib/apt/lists/* wkhtmltox.deb

# install latest postgresql-client
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ jammy-pgdg main' > /etc/apt/sources.list.d/pgdg.list \
    && GNUPGHOME="$(mktemp -d)" \
    && export GNUPGHOME \
    && repokey='B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8' \
    && gpg --batch --keyserver keyserver.ubuntu.com --recv-keys "${repokey}" \
    && gpg --batch --armor --export "${repokey}" > /etc/apt/trusted.gpg.d/pgdg.gpg.asc \
    && gpgconf --kill all \
    && rm -rf "$GNUPGHOME" \
    && apt-get update  \
    && apt-get install --no-install-recommends -y postgresql-client \
    && rm -f /etc/apt/sources.list.d/pgdg.list \
    && rm -rf /var/lib/apt/lists/*

# Install rtlcss (on Debian buster)
RUN npm install -g rtlcss

# Install Odoo
#ENV ODOO_VERSION 17.0
#ARG ODOO_RELEASE=20240312
#ARG ODOO_SHA=467f514f90cf8cdc36dddd84129adefc4624be36
#RUN curl -o odoo.deb -sSL http://nightly.odoo.com/${ODOO_VERSION}/nightly/deb/odoo_${ODOO_VERSION}.${ODOO_RELEASE}_all.deb \
#    && echo "${ODOO_SHA} odoo.deb" | sha1sum -c - \
#    && apt-get update \
#    && apt-get -y install --no-install-recommends ./odoo.deb \
#    && rm -rf /var/lib/apt/lists/* odoo.deb

COPY ./addons /opt/odoo/addons
COPY ./debian /opt/odoo/debian
COPY ./doc /opt/odoo/doc
COPY ./odoo /opt/odoo/odoo
COPY ./setup /opt/odoo/setup
COPY ./.tx /opt/odoo/.tx

RUN useradd -m odoo && echo odoo:odoo | chpasswd

RUN pip3 install wheel psycopg2-binary
RUN pip3 install -r /opt/odoo/requirements.txt

RUN cp /opt/odoo/setup/odoo /opt/odoo/odoo-bin && chmod +x /opt/odoo/odoo-bin
# Copy entrypoint script and Odoo configuration file
COPY ./entrypoint.sh /
COPY ./config/odoo.conf /etc/odoo/

# Set permissions and Mount /var/lib/odoo to allow restoring filestore and /mnt/extra-addons for users addons
RUN chown odoo /etc/odoo/odoo.conf \
    && mkdir -p /mnt/extra-addons \
    && chown -R odoo /mnt/extra-addons \
    && mkdir -p /var/lib/odoo \
    && chown -R odoo /var/lib/odoo 
VOLUME ["/var/lib/odoo", "/mnt/extra-addons"]

# Expose Odoo services
EXPOSE 8069 8071 8072

# Set the default config file
ENV ODOO_RC /etc/odoo/odoo.conf

COPY wait-for-psql.py /usr/local/bin/wait-for-psql.py

RUN pip3 install simplejson

# Set default user when running the container
USER odoo

ENTRYPOINT ["/entrypoint.sh"]
CMD ["odoo"]
