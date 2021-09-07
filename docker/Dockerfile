ARG BASE_VERSION=21.04
FROM nvcr.io/nvidia/tensorflow:${BASE_VERSION}-tf2-py3
WORKDIR rachetnet
RUN python -m pip install --upgrade pip
RUN apt update
RUN apt install ffmpeg libsm6 libxext6  -y

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install --extra-index-url https://developer.download.nvidia.com/compute/redist --upgrade nvidia-dali-cuda110
RUN pip install --extra-index-url https://developer.download.nvidia.com/compute/redist --upgrade nvidia-dali-tf-plugin-cuda110

COPY . .

