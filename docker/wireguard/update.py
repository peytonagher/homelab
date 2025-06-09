import subprocess

def run_command(command):
    """Execute a shell command and print the output."""
    try:
        print(f"Running command: {command}")
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

def main():
    run_command("docker stop wireguard")
    run_command("docker rm wireguard")
    run_command("docker pull ghcr.io/wg-easy/wg-easy")
    
    run_command("""
        docker run -d \
        --name=wireguard \
        -e WG_HOST=REDACTED \
        -e PASSWORD_HASH='REDACTED' \
        -v ~/.wg-easy:/etc/wireguard \
        -p 51820:51820/udp \
        -p 51821:51821/tcp \
        --cap-add=NET_ADMIN \
        --cap-add=SYS_MODULE \
        --sysctl="net.ipv4.conf.all.src_valid_mark=1" \
        --sysctl="net.ipv4.ip_forward=1" \
        --restart unless-stopped \
        ghcr.io/wg-easy/wg-easy
    """)

if __name__ == "__main__":
    main()
