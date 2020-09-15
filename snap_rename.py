import re
from infinisdk import InfiniBox
import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Resizing replica for Active/Active")
    parser.add_argument('-v', '--volume', nargs=1, required=True, help='Name of the volume')
    parser.add_argument('-r', '--rename', nargs=1, required=True, help='Previous volume name')
    parser.add_argument('-i', '--ibox', nargs=1, required=True, help='Ibox Name')
    parser.add_argument('-u', '--user', nargs=1, required=True, help='Ibox user')
    parser.add_argument('-p', '--password', nargs=1, required=True, help='Ibox password')
    args = parser.parse_args()
    return args
args=get_args()
auth=(args.user[0],args.password[0])
system=InfiniBox(args.ibox[0],auth)
try:
     system.login()
     volume=system.volumes.find(name=args.volume[0])
     if (volume.to_list()):
     	volume=volume.to_list()[0]
     print (volume.get_name())
     for snap in volume.get_snapshots().to_list():
         sp="^"+args.rename[0]
         if re.search(sp,snap.get_name()):
              new_name=(re.sub(sp,volume.get_name(),snap.get_name()))
              snap.update_name(new_name)
except Exception as E:
    print ("Cannot run",E)