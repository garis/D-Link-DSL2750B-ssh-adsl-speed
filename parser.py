import subprocess
import os.path
import time

"""requires: sudo apt-get install expect python3    """

TMP_FILE="/tmp/gaspaHomeSpeed"
SCRIPT_SH="/etc/mrtg/SSHGaspa/scriptSSH.sh"
MUTLIPLIER=1000 #show kilobytes/s

def write_file(time_millisec,down,up):
    """write file with the last info"""
    f = open(TMP_FILE, 'w')
    f.write(str(int(round(time.time() * 1000))))
    f.write("\n")
    f.write(str(down))
    f.write("\n")
    f.write(str(up))
    f.close()
    return;

process = subprocess.Popen([SCRIPT_SH], stdout=subprocess.PIPE)
out, err = process.communicate()

result=str(out).split(":")
down=float((str(result[1]).split("("))[0])/ 1000000
up=float((str(result[2]).split("("))[0])/ 1000000

if os.path.exists(TMP_FILE):
    f = open(TMP_FILE, 'r')
    time_old=int(str(f.readline()))
    delta_time=(int(round(time.time() * 1000))-time_old)/1000
    old_down=float(str(f.readline()))
    old_up=float(str(f.readline()))
    f.close()
    write_file(str(int(round(time.time() * 1000))),str(down),str(up))
    if(old_down<down):
        print (((down-old_down)/delta_time)*MUTLIPLIER)
    else:
        print (0)
    if(old_up<up):
        print (((up-old_up)/delta_time)*MUTLIPLIER)
    else:
        print (0)
else:
    write_file(str(int(round(time.time() * 1000))),str(down),str(up))
    print (0)
    print (0)
print (0)
print (0)
