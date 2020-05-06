import subprocess
subprocess.Popen(["/usr/bin/amixer", "-D", "pulse", "sset", "Master", "10%+"])
