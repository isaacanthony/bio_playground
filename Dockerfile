FROM jupyter/scipy-notebook:latest

ENV JUPYTER_ENABLE_LAB yes

# Install os dependencies
USER root
RUN apt-get update && apt-get install -y \
  iqtree \
  mafft \
  muscle

# Install python dependencies
USER $NB_UID
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Set up package
COPY . .
RUN pip install -e .
