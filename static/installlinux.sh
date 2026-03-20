#!/usr/bin/env bash
set -e

# Helper: set a key=value in a config file (update if exists, append if not)
set_config() {
    local key="$1" value="$2" file="$3"
    if grep -q "^${key}=" "$file" 2>/dev/null; then
        sed -i "s|^${key}=.*|${key}=${value}|" "$file"
    else
        echo "${key}=${value}" >> "$file"
    fi
}

# ─── Collect all user input upfront ──────────────────────────────────────────

echo "[+] I2P Linux Installer"
echo ""
echo "[?] Choose setup mode:"
echo "    1) Basic    - Install I2P with default settings"
echo "    2) Advanced - Install I2P and configure bandwidth, ports, and network"
read -p "    Selection (1): " setup_mode < /dev/tty

ADVANCED=false
ADV_DL_SPEED=""
ADV_UL_SPEED=""
ADV_PORT=""
ADV_UPNP="true"

if [ "$setup_mode" = "2" ]; then
    ADVANCED=true

    # ── Speed test ───────────────────────────────────────────────────────
    echo ""
    echo "[?] Run a speed test to auto-configure bandwidth? (Y/n)"
    read -p "    " run_speedtest < /dev/tty

    if [[ ! "$run_speedtest" =~ ^[Nn] ]]; then
        echo "[+] Installing Ookla Speedtest CLI..."
        SPEEDTEST_TMP=$(mktemp -d)
        ARCH=$(uname -m)
        case "$ARCH" in
            x86_64)  ST_ARCH="x86_64" ;;
            aarch64) ST_ARCH="aarch64" ;;
            armv7l)  ST_ARCH="armhf" ;;
            i686)    ST_ARCH="i386" ;;
            *)       ST_ARCH="" ;;
        esac

        if [ -n "$ST_ARCH" ]; then
            ST_URL="https://install.speedtest.net/app/cli/ookla-speedtest-1.2.0-linux-${ST_ARCH}.tgz"
            if curl -fsSL -o "$SPEEDTEST_TMP/speedtest.tgz" "$ST_URL"; then
                tar -xzf "$SPEEDTEST_TMP/speedtest.tgz" -C "$SPEEDTEST_TMP"
                echo "[+] Running speed test (this may take 30-60 seconds)..."
                # Accept license automatically, output JSON
                ST_OUTPUT=$("$SPEEDTEST_TMP/speedtest" --accept-license --accept-gdpr -f json 2>/dev/null || echo "")

                if [ -n "$ST_OUTPUT" ]; then
                    # Parse bandwidth in bytes/sec from JSON, convert to KBps
                    DL_BPS=$(echo "$ST_OUTPUT" | sed -n 's/.*"download":{[^}]*"bandwidth":\([0-9]*\).*/\1/p')
                    UL_BPS=$(echo "$ST_OUTPUT" | sed -n 's/.*"upload":{[^}]*"bandwidth":\([0-9]*\).*/\1/p')

                    if [ -n "$DL_BPS" ] && [ -n "$UL_BPS" ]; then
                        # bandwidth is in bytes/sec, convert to KBps then 80%
                        DL_KBPS=$(( DL_BPS / 1024 ))
                        UL_KBPS=$(( UL_BPS / 1024 ))
                        DL_MBPS=$(( DL_BPS * 8 / 1000000 ))
                        UL_MBPS=$(( UL_BPS * 8 / 1000000 ))
                        ADV_DL_SPEED=$(( DL_KBPS * 80 / 100 ))
                        ADV_UL_SPEED=$(( UL_KBPS * 80 / 100 ))

                        echo "[+] Speed test results: ~${DL_MBPS} Mbps down / ~${UL_MBPS} Mbps up"
                        echo "[+] I2P bandwidth will be set to: ${ADV_DL_SPEED} KBps in / ${ADV_UL_SPEED} KBps out (80%)"
                        echo ""
                        read -p "[?] Accept these values? (Y/n): " accept_speed < /dev/tty
                        if [[ "$accept_speed" =~ ^[Nn] ]]; then
                            ADV_DL_SPEED=""
                            ADV_UL_SPEED=""
                        fi
                    else
                        echo "[!] Could not parse speed test results."
                    fi
                else
                    echo "[!] Speed test failed to run."
                fi
            else
                echo "[!] Could not download Speedtest CLI. Skipping speed test."
            fi
        else
            echo "[!] Unsupported architecture ($ARCH) for speed test. Skipping."
        fi
        rm -rf "$SPEEDTEST_TMP"
    fi

    # Manual bandwidth entry if speed test was skipped or rejected
    if [ -z "$ADV_DL_SPEED" ] || [ -z "$ADV_UL_SPEED" ]; then
        echo ""
        echo "[?] Enter bandwidth manually (speeds will be set to 80% of values entered)"
        read -p "    Download speed in KBps (e.g., 12500 for ~100 Mbps, blank to skip): " ADV_DL_SPEED < /dev/tty
        read -p "    Upload speed in KBps (e.g., 6250 for ~50 Mbps, blank to skip): " ADV_UL_SPEED < /dev/tty
    fi

    # Generate a random default port in the 9151–30777 range
    DEFAULT_PORT=$(( RANDOM % 21627 + 9151 ))

    echo ""
    read -p "[?] TCP/UDP port for I2P (${DEFAULT_PORT}): " ADV_PORT < /dev/tty
    if [ -z "$ADV_PORT" ]; then
        ADV_PORT="$DEFAULT_PORT"
    fi

    # Validate port is in range
    while [ "$ADV_PORT" -lt 9151 ] || [ "$ADV_PORT" -gt 30777 ] 2>/dev/null; do
        echo "[!] Port must be between 9151 and 30777."
        read -p "[?] TCP/UDP port for I2P (${DEFAULT_PORT}): " ADV_PORT < /dev/tty
        if [ -z "$ADV_PORT" ]; then
            ADV_PORT="$DEFAULT_PORT"
            break
        fi
    done

    echo ""
    read -p "[?] Enable UPnP? (Y/n): " upnp_answer < /dev/tty
    if [[ "$upnp_answer" =~ ^[Nn] ]]; then
        ADV_UPNP="false"
    fi

    echo ""
    echo "[+] Settings captured. Starting installation..."
fi

# ─── Detect and install ─────────────────────────────────────────────────────

echo "[+] Detecting distribution..."

DOCKER_INSTALL=false

if grep -qi "ubuntu" /etc/os-release; then
    echo "[+] Ubuntu detected – using PPA method"

    export DEBIAN_FRONTEND=noninteractive
    echo "i2p i2p/daemon boolean true" | sudo debconf-set-selections

    sudo apt-get update
    sudo apt-get install -y software-properties-common apt-transport-https curl

    sudo add-apt-repository -y ppa:i2p-maintainers/i2p
    sudo apt-get update
    sudo apt-get install -y i2p

    sudo dpkg-reconfigure -f noninteractive i2p

elif grep -qi "debian" /etc/os-release; then
    echo "[+] Debian detected – using official Debian repository"

    export DEBIAN_FRONTEND=noninteractive
    echo "i2p i2p/daemon boolean true" | sudo debconf-set-selections

    sudo apt-get update
    sudo apt-get install -y apt-transport-https lsb-release curl gnupg2

    CODENAME=$(lsb_release -sc)
    KEYRING="/usr/share/keyrings/i2p-archive-keyring.gpg"

    sudo curl -o "$KEYRING" https://i2p.net/i2p-archive-keyring.gpg
    echo "deb [signed-by=$KEYRING] https://deb.i2p.net/ $CODENAME main" \
        | sudo tee /etc/apt/sources.list.d/i2p.list

    sudo apt-get update
    sudo apt-get install -y i2p i2p-keyring

    sudo dpkg-reconfigure -f noninteractive i2p

elif grep -qi "fedora" /etc/os-release; then
    echo "[+] Fedora detected – using COPR repository"

    sudo dnf copr enable -y i2porg/i2p
    sudo dnf install -y i2p

elif grep -qi "opensuse" /etc/os-release; then
    if grep -qi "tumbleweed" /etc/os-release; then
        echo "[+] openSUSE Tumbleweed detected"
        REPO_URL="https://download.opensuse.org/repositories/home:i2p/openSUSE_Tumbleweed/home:i2p.repo"
    else
        echo "[+] openSUSE Leap detected"
        REPO_URL="https://download.opensuse.org/repositories/home:i2p/openSUSE_Leap_15.6/home:i2p.repo"
    fi

    sudo zypper addrepo -f "$REPO_URL"
    sudo zypper --gpg-auto-import-keys refresh
    sudo zypper install -y i2p

else
    echo "[!] Unsupported distribution detected."
    echo "[?] Would you like to install I2P using Docker instead?"
    read -p "    Install via Docker? (y/N): " answer < /dev/tty

    if [[ ! "$answer" =~ ^[Yy] ]]; then
        echo "[!] Exiting. Visit https://geti2p.net for manual installation options."
        exit 1
    fi

    if ! command -v docker &> /dev/null; then
        echo "[+] Docker not found – installing Docker..."
        curl -fsSL https://get.docker.com | sh
        sudo systemctl enable --now docker
        echo "[+] Docker installed successfully."
    else
        echo "[+] Docker is already installed."
    fi

    echo "[+] Setting up I2P Docker container..."
    sudo docker pull geti2p/i2p
    sudo docker volume create i2p-data
    sudo docker run -d \
        --name i2p \
        --restart unless-stopped \
        -v i2p-data:/i2p/.i2p \
        -p 7657:7657 \
        -p 4444:4444 \
        -p 4445:4445 \
        geti2p/i2p

    echo "[+] I2P Docker container is running."
    DOCKER_INSTALL=true
fi

# ─── Apply advanced configuration ───────────────────────────────────────────

if [ "$ADVANCED" = true ] && [ "$DOCKER_INSTALL" = false ]; then
    echo ""
    echo "[+] Applying advanced configuration..."

    # Detect config path
    if [ -d "/var/lib/i2p/i2p-config" ]; then
        I2P_CONFIG="/var/lib/i2p/i2p-config"
    elif [ -d "$HOME/.i2p" ]; then
        I2P_CONFIG="$HOME/.i2p"
    else
        I2P_CONFIG="/var/lib/i2p/i2p-config"
        sudo mkdir -p "$I2P_CONFIG"
    fi

    ROUTER_CONFIG="$I2P_CONFIG/router.config"
    echo "[+] Config path: $I2P_CONFIG"

    if [ ! -f "$ROUTER_CONFIG" ]; then
        sudo touch "$ROUTER_CONFIG"
    fi

    # ── Bandwidth ────────────────────────────────────────────────────────
    if [ -n "$ADV_DL_SPEED" ] && [ -n "$ADV_UL_SPEED" ]; then
        in_kbps=$(( ADV_DL_SPEED * 80 / 100 ))
        out_kbps=$(( ADV_UL_SPEED * 80 / 100 ))
        in_burst_kb=$(( in_kbps * 20 ))
        out_burst_kb=$(( out_kbps * 20 ))

        sudo bash -c "$(declare -f set_config); \
            set_config 'i2np.bandwidth.inboundKBytesPerSecond' '$in_kbps' '$ROUTER_CONFIG'; \
            set_config 'i2np.bandwidth.inboundBurstKBytesPerSecond' '$in_kbps' '$ROUTER_CONFIG'; \
            set_config 'i2np.bandwidth.inboundBurstKBytes' '$in_burst_kb' '$ROUTER_CONFIG'; \
            set_config 'i2np.bandwidth.outboundKBytesPerSecond' '$out_kbps' '$ROUTER_CONFIG'; \
            set_config 'i2np.bandwidth.outboundBurstKBytesPerSecond' '$out_kbps' '$ROUTER_CONFIG'; \
            set_config 'i2np.bandwidth.outboundBurstKBytes' '$out_burst_kb' '$ROUTER_CONFIG'"

        echo "[+] Bandwidth: ${in_kbps} KBps in / ${out_kbps} KBps out (80% of entered values)"
    fi

    # ── Port ─────────────────────────────────────────────────────────────
    if [ -n "$ADV_PORT" ]; then
        sudo bash -c "$(declare -f set_config); \
            set_config 'i2np.ntcp.port' '$ADV_PORT' '$ROUTER_CONFIG'; \
            set_config 'i2np.udp.port' '$ADV_PORT' '$ROUTER_CONFIG'; \
            set_config 'i2np.udp.internalPort' '$ADV_PORT' '$ROUTER_CONFIG'; \
            set_config 'i2np.udp.enable' 'true' '$ROUTER_CONFIG'"

        echo "[+] Port: $ADV_PORT (TCP and UDP)"
    fi

    # ── UPnP ─────────────────────────────────────────────────────────────
    sudo bash -c "$(declare -f set_config); \
        set_config 'i2np.upnp.enable' '$ADV_UPNP' '$ROUTER_CONFIG'"
    echo "[+] UPnP: $ADV_UPNP"

    # ── Welcome wizard ───────────────────────────────────────────────────
    sudo bash -c "$(declare -f set_config); \
        set_config 'routerconsole.welcomeWizardComplete' 'true' '$ROUTER_CONFIG'"

    # ── Addressbook subscription ─────────────────────────────────────────
    SUBS_DIR="$I2P_CONFIG/addressbook"
    SUBS_FILE="$SUBS_DIR/subscriptions.txt"
    NOTBOB_URL="http://notbob.i2p/hosts.txt"

    sudo mkdir -p "$SUBS_DIR"
    if [ ! -f "$SUBS_FILE" ]; then
        sudo touch "$SUBS_FILE"
    fi
    if ! grep -qF "$NOTBOB_URL" "$SUBS_FILE" 2>/dev/null; then
        echo "$NOTBOB_URL" | sudo tee -a "$SUBS_FILE" > /dev/null
        echo "[+] Added notbob.i2p to addressbook subscriptions."
    fi

    echo "[+] Advanced configuration complete."
fi

# ─── Start service ───────────────────────────────────────────────────────────

if [ "$DOCKER_INSTALL" = false ]; then
    sudo systemctl enable --now i2p

    # Port check
    if [ -n "$ADV_PORT" ]; then
        echo "[+] Waiting for I2P to start..."
        sleep 5
        if command -v ss &>/dev/null; then
            if ss -tuln | grep -q ":${ADV_PORT} "; then
                echo "[+] Port $ADV_PORT is listening."
            else
                echo "[!] Port $ADV_PORT is not listening yet – it may take a moment."
            fi
        fi
        echo "[i] To verify external reachability, check http://127.0.0.1:7657/confignet after I2P integrates."
    fi
fi

echo "[+] I2P installation complete. Router console: http://127.0.0.1:7657"
