#!/usr/bin/env bash

echo "Sike, nothing here yet"

# Generate unique UUID for marc1
# TODO: Move to generateidentity.py (syncs to server)
# Print uuid as qr code (use a png generator?)
uuidgen > uuid

echo "Succesfully generated new marc1 UUID!:\n"
cat uuid