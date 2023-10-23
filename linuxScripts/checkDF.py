import subprocess
import re
import sys

def get_disk_space_usage():
    try:
        df_output = subprocess.check_output(['df', '-h'])
        lines = df_output.decode('utf-8').split('\n')
        for line in lines[1:]:
            fields = line.split()
            if len(fields) >= 6 and fields[5] == '/':  # Assuming you want to check the root file system '/'
                used_percentage = int(re.sub('[%]', '', fields[4]))
                return used_percentage
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

disk_space_usage = get_disk_space_usage()

if disk_space_usage is not None:
    if disk_space_usage < 50:
        print("Success: {} disk space is {}%, Normal usage on Disk".format(sys.argv[1],str(disk_space_usage)))
        sys.exit(0)
    elif 50 <= disk_space_usage <= 75:
        print("Warn: {} disk space is {}%, Starting to fill up Disk".format(sys.argv[1],str(disk_space_usage)))
        sys.exit(1)
    else:
        print("Error: {} disk space is {}%, Almost out of space on Disk".format(sys.argv[1],str(disk_space_usage)))
        sys.exit(2)
else:
    print("Error: Failed to retrieve {} space usage on Disk".format(sys.argv[1]))
    sys.exit(3)
