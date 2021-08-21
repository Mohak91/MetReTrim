#syntax=docker/dockerfile:1

#Stage1
FROM python:3.7-slim AS compile-image

RUN adduser --disabled-password --gecos '' metretrim_user && \
    apt-get update && \
    apt-get install -y --no-install-recommends build-essential gcc && \
    python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

USER metretrim_user

#Stage2
FROM python:3.7-alpine AS build-image

LABEL maintainer="sharda.mohak@gmail.com"

# MetReTrimruntime distribution filename.
ARG BUILD_DATE

# Labels.
LABEL org.label-schema.schema-version="1.0"
LABEL org.label-schema.build-date=$BUILD_DATE
LABEL org.label-schema.name="mohaksharda/metretrim"
LABEL org.label-schema.description="MetReTrim: Command line tool for trimming heterogenous \"N\" spacers"
LABEL org.label-schema.url="https://github.com/Mohak91/MetReTrim"
LABEL org.label-schema.vcs-url="https://github.com/Mohak91/MetReTrim"
#LABEL org.label-schema.vcs-ref=$VCS_REF
LABEL org.label-schema.vendor="Mohak Sharda"
LABEL org.label-schema.version="1.0"
LABEL org.label-schema.docker.cmd="sudo docker run --rm -d \
-v <working_dir_on_hostOS>:<working_dir_inside_container> -ti \
--name <container_name> \
<image_name> \
-i <path_to_work_dir_inside_container_w_input_folder_name> \
-o <path_to_work_dir_inside_container_w_output_folder_name> \
-f <forward_primer> \
-r <reverse_primer> \
-m <number_of_mismatch> \
-k <keep_or_unkeep_primer_sequence>"

RUN adduser --disabled-password --gecos '' metretrim_user

WORKDIR /usr/src/app

COPY --from=compile-image /opt/venv /opt/venv
COPY MetReTrim .

ENV PATH="/opt/venv/bin:$PATH"

USER metretrim_user

ENTRYPOINT ["python","/usr/src/app/MetReTrim"]
