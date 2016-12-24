#!/bin/bash
result=$(expect /etc/mrtg/SSHGaspa/scriptSSH|tr -d " "|grep RXbytes:)
echo "$result"
