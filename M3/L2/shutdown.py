import platform
import subprocess
import shlex
def shutdown_now(dry_run: bool = False):
    os_name = platform.system().lower()

    if 'windows' in os_name:
        cmd = 'shutdown /s /t 0'
    elif 'linux' in os_name:
        cmd = 'systemctl poweroff'
    elif 'darwin' in os_name:
        cmd = 'sudo shutdown -h now'
    else:
        raise RuntimeError(f"Unsupported operating system: {os_name}")
    if dry_run:
        print(f"[dry_run] Command to run: {cmd}")
        return        
    try:
        if 'windows' in os_name:
            subprocess.run(cmd, shell=True, check=True)
        else:
            parts = shlex.split(cmd)
            subprocess.run(parts, check=True)
    except subprocess.CalledProcessError as e:
        print("Error while shutting down:", e)   
    except Exception as e:
        print("Unexpected error:", e)

if __name__ == '__main__':
    shutdown_now(dry_run=False)
            