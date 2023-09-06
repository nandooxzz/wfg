# prompt colors
GREEN='\033[1;32m'
BLUE='\033[1;34m'
NC='\033[0m'

# install packages
echo -e "${GREEN}[1] Installing packages...${NC}"
sleep 2s
yay -S lolcat jp2a python3 python-colorama python-requests 
sleep 1s

# copy src
clear
echo -e "${BLUE}[2] Copying files...${NC}"
sudo mkdir -p /usr/share/world-flags-guesser
sudo cp -r {src/title.txt,src/uninstall.sh} /usr/share/world-flags-guesser
sleep 1s

# bin
echo -e "${BLUE}[3] Installing WFG...${NC}"
sudo cp -r ./src/dist/wfg/* /bin/
cd /bin
sudo chmod +x ./wfg
sleep 2s

# done
echo -e "${GREEN}[!] World Flags Guesser has been installed! You're ready to go, run wfg on console${NC}"