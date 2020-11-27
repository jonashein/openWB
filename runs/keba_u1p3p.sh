#!/bin/bash
kebaip=$1
phases=$2

if [[ "$phases" -eq "1" ]]; then
  echo -n "output 0" | socat - UDP-DATAGRAM:$kebaip:7090
  echo -n "display 1 10 10 0 1-Ph" | socat - UDP-DATAGRAM:$kebaip:7090
elif [[ "$phases" -eq "3" ]]; then
  echo -n "output 1" | socat - UDP-DATAGRAM:$kebaip:7090
  echo -n "display 1 10 10 0 3-Ph" | socat - UDP-DATAGRAM:$kebaip:7090
fi
