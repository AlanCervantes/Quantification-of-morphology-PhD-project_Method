FROM ubuntu:22.04

LABEL maintainer='Ankita Roy'

COPY ./ /opt/morphology_analysis

RUN apt update
RUN DEBIAN_FRONTEND="noninteractive" TZ="America/New_York" apt install -y \
    build-essential \
    python3-setuptools \
    python3-pip \
    python3 \
    cmake-gui \
    libglu1-mesa-dev \
    freeglut3-dev \
    freeglut3 \
    software-properties-common \
    nano \
    python3-opencv \
    python3-numpy
    

RUN pip3 install \
    numpy \
    Pillow \
    scipy \
    scikit-image \
    scikit-learn \
    scikit-build \
    matplotlib \
    pandas \
    opencv-python-headless 

    
RUN python3 -m pip install --upgrade Pillow

RUN python3 -m pip install -U matplotlib

