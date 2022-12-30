#!/usr/bin/env python3
import os, random, sys


OUT_PATH = "/tmp/.cpu_core_manager" + str(random.randrange(0, 999999999))
def simple_exec(cmd:str):
	os.system(cmd + " >  \"" + OUT_PATH + "\"")
	f = open(OUT_PATH, "r")
	r = f.read()
	f.close()

	os.system("rm \"" + OUT_PATH + "\"")
	return r

if simple_exec("whoami").strip() != "root":
	print("Error: please run as root")
	exit(1)

cpus = [f.strip() for f in simple_exec("ls /sys/devices/system/cpu/cpu*/online -B -Z").split("?") if len(f) != 0]

if len(sys.argv) == 1:
	print("""   _____                                                                                      
  / ____|                                                                                   _ 
 | |     _ __  _   _    ___ ___  _ __ ___   _ __ ___   __ _ _ __   __ _  __ _  ___ _ __    (_)
 | |    | '_ \| | | |  / __/ _ \| '__/ _ \ | '_ ` _ \ / _` | '_ \ / _` |/ _` |/ _ \ '__|
 | |____| |_) | |_| | | (_| (_) | | |  __/ | | | | | | (_| | | | | (_| | (_| |  __/ |       _ 
  \_____| .__/ \__,_|  \___\___/|_|  \___| |_| |_| |_|\__,_|_| |_|\__,_|\__, |\___|_|      (_)
        | |                                                              __/ |                
        |_|                                                             |___/ 
        """)
	print(f"""       

How to use:

[] list                 - Displays cpu cores
[] maxPower             - Enables all cpu cores
[] minPower             - Only sets one core enabled
[] setActive (number)   - Sets how many cores to be enabled
[] setNotActive (number) - Sets how many cores to be disabled
		""")
	exit(0)
if sys.argv[1] == "list":
	print("Cpu core status:")
	for c in cpus:
		f = open(c, "r")
		print(c.split("/")[-2], "on" if f.read(1)== '1' else "off")
		f.close()

	print("\nPs: cpu0 is hidden but always enabled")

	exit(0)
if sys.argv[1] == "maxPower":
	for c in cpus:
		f = open(c, "w")
		f.write("1")
		f.close()
	print("All cpu cores enabled")

if sys.argv[1] == "minPower":
	for c in cpus:
		f = open(c, "w")
		f.write("0")
		f.close()
	print("All cpu cores disabled but one")
if sys.argv[1] == "setActive":
	act = int(sys.argv[2])-1 # minus one for the default cpu0 
	for c in cpus:
		f = open(c, "w")
		f.write("1" if act > 0 else "0")
		f.close()
		act-=1
	print(sys.argv[2] + " cpu cores enabled")
if sys.argv[1] == "setNotActive":
	act = int(sys.argv[2])
	for c in cpus:
		f = open(c, "w")
		f.write("0" if act > 0 else "1")
		f.close()
		act-=1
	print(sys.argv[2] + " cpu cores enabled")





