#!/bin/sh

set -e

flask db upgrade
exec python main.py