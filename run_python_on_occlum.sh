#!/bin/bash
set -e

BLUE='\033[1;34m'
NC='\033[0m'

cd occlum_instance
echo -e "${BLUE}occlum run /bin/main.py${NC}"
HF_DATASETS_CACHE=/root/cache \
       occlum run /bin/python3 main.py