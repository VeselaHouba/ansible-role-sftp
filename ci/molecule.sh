#!/usr/bin/env bash
docker \
  run \
  --rm \
  -it \
  -v "$(pwd):/tmp/veselahouba.sftp" \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -w "/tmp/veselahouba.sftp" \
  -e MOLECULE_DISTRO \
  -e MOLECULE_NO_LOG=false \
  veselahouba/molecule:v3 \
  molecule "${@}"
