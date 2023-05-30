#!/usr/bin/env bash

wget "https://github.com/Nautilus-Institute/quals-2023/raw/main/artifact-bunker/src/archive_server-365ad9f1f4c4b8966448688fc0b3abd818fab3272d40538c032ac847815ed86e.tar.gz"
tar -xvf archive_server-365ad9f1f4c4b8966448688fc0b3abd818fab3272d40538c032ac847815ed86e.tar.gz
docker build dist --tag artifact_bunker
docker run -p 5555:5555 --rm -it artifact_bunker