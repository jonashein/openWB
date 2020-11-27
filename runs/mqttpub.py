import paho.mqtt.client as mqtt
from subprocess import Popen
import re
import sys
import time
import fileinput
import argparse
import os

def main():

  parser = argparse.ArgumentParser(description='openWB MQTT Publisher')
  parser.add_argument('--qos', '-q', metavar='qos', type=int, help='The QOS setting', default=0)
  parser.add_argument('--retain', '-r', dest='retain', action='store_true', help='If true, retain this publish')
  parser.set_defaults(retain=False)

  args = parser.parse_args()

  client = mqtt.Client("openWB-python-bulkpublisher-" + str(os.getpid()))
  connected_flag=False
  while not connected_flag: #wait in loop
    try:
      client.connect("localhost")
      connected_flag=True
    except:
      print("Warten auf MQTT Broker")
      time.sleep(5)
  for line in sys.stdin:
    m = re.match('(.*)=(.*)', line)
    if m:
      #print("Publishing '%s' :: '%s'" % (m.group(1), m.group(2)))
      client.publish(m.group(1), payload=m.group(2), qos=args.qos, retain=args.retain)

  client.loop(timeout=2.0)
  client.disconnect()
if __name__ == "__main__":
    main()
