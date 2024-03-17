FROM ubuntu:20.04
LABEL maintainer="marmot0814 <s1357andy871207@gmail.com>"

ARG TEXLIVE_VERSION=2024

ENV DEBIAN_FRONTEND=noninteractive
ENV DEBCONF_NOWARNINGS=yes
ENV PATH="/usr/local/texlive/bin:$PATH"

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        make \
        wget \
        libfontconfig1-dev \
        libfreetype6-dev \
        ghostscript \
        perl && \
    apt-get clean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        python3-pip \
        python3-dev && \
    pip3 install --no-cache-dir pygments && \
    mkdir /tmp/install-tl-unx && \
    wget -O - https://ctan.mirror.twds.com.tw/tex-archive/systems/texlive/tlnet/install-tl-unx.tar.gz \
        | tar -xzv -C /tmp/install-tl-unx --strip-components=1 && \
    /bin/echo -e 'selected_scheme scheme-basic\ntlpdbopt_install_docfiles 0\ntlpdbopt_install_srcfiles 0' \
        > /tmp/install-tl-unx/texlive.profile && \
    /tmp/install-tl-unx/install-tl \
        --profile /tmp/install-tl-unx/texlive.profile \
        -repository https://ctan.mirror.twds.com.tw/tex-archive/systems/texlive/tlnet/ && \
    rm -r /tmp/install-tl-unx && \
    ln -sf /usr/local/texlive/${TEXLIVE_VERSION}/bin/$(uname -m)-linux /usr/local/texlive/bin && \
    apt-get remove -y --purge \
        build-essential \
        python3 && \
    apt-get clean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y \
      wget unzip python perl \
      ttf-mscorefonts-installer \
      fontconfig && \
    apt-get clean

# install NotoSansCJK font
RUN mkdir /tmp/noto && \
    cd /tmp/noto && \
    wget -O NotoSansCJKtc-hinted.zip https://noto-website-2.storage.googleapis.com/pkgs/NotoSansCJKtc-hinted.zip && \
    unzip NotoSansCJKtc-hinted.zip && \
    mkdir /usr/share/fonts/noto && \
    mv -t /usr/share/fonts/noto *.otf && \
    rm -r /tmp/noto && \
    fc-cache -fv

# update tlmgr
RUN tlmgr update --self && \
    tlmgr install texliveonfly \
                  latexmk \
                  xetex

VOLUME ["/storage"]
WORKDIR /storage
CMD [ "bash" ]
