import subprocess

host = "www.google.com"

ping = subprocess.Popen(
    ["ping", "-n", "1", host],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)

out, error = ping.communicate()
print(out)