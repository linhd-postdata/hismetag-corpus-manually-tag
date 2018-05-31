#!/usr/bin/env bash

# rename geogName as placeName

indir="$1"

echo -e "\nReplacing in $1\n"

sed -i -e 's/geogName/placeName/g' "$1"/*
