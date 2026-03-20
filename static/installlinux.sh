#!/usr/bin/env bash
set -e

echo "[+] I2P Linux Installer"
echo "[+] Detecting distribution..."

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
    sudo systemctl enable --now i2p

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
    sudo systemctl enable --now i2p

elif grep -qi "fedora" /etc/os-release; then
    echo "[+] Fedora detected – using COPR repository"

    sudo dnf copr enable -y i2porg/i2p
    sudo dnf install -y i2p
    sudo systemctl enable --now i2p

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
    sudo systemctl enable --now i2p

else
    echo "[!] Unsupported distribution detected."
    echo "[?] Would you like to install I2P using Docker instead?"
    read -p "    Install via Docker? (y/N): " answer

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
fi

echo "[+] I2P installation complete. Router console: http://127.0.0.1:7657"
