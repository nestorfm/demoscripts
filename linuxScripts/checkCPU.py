import subprocess
import re
import sys

def get_cpu_usage():
    try:
        top_output = subprocess.check_output(['top', '-n', '1', '-b'])
        cpu_usage = re.search(r'%Cpu\(s\):[^\d]+(\d+\.\d)', top_output.decode('utf-8'))
        if cpu_usage:
            return float(cpu_usage.group(1))
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

cpu_usage = get_cpu_usage()

if cpu_usage is not None:
    if cpu_usage < 60:
        print("Success: Script {}: within normal usage range {}% CPU".format(sys.argv[2],str(cpu_usage)))
        sys.exit(0)
    elif 60 <= cpu_usage <= 75:
        print("Warning: Script {}: above normal usage range {}% CPU".format(sys.argv[2],str(cpu_usage)))
        sys.exit(1)
    else:
        print("Error: Script {}: is {}% high and almost out of CPU".format(sys.argv[2],str(cpu_usage)))
        sys.exit(2)
else:
    print("Error: Script {}: Failed to retrieve usage for CPU".format(sys.argv[2]))
    sys.exit(3)
