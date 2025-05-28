#!/bin/bash
set -e

BLUE='\033[1;34m'
NC='\033[0m'

# 运行Python示例程序
cd occlum_instance
echo -e "${BLUE}occlum run /bin/python3 main.py${NC}"
occlum run /bin/python3 main.py