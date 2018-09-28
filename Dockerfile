FROM alpine:latest

RUN apk add --no-cache \
    libpng \
    freetype \
    libstdc++ \
    python3

RUN python3 -m ensurepip
RUN pip3 install --upgrade pip

RUN apk add --no-cache --virtual .build-deps \
        gcc \
        build-base \
        python3-dev \
        libpng-dev \
        musl-dev \
        freetype-dev \
    && pip3 install numpy \
    && pip3 install matplotlib \
    && apk del .build-deps

COPY generate_graph.py /

CMD ["python3", "generate_graph.py"]
