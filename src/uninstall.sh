# prompt colors
GREEN='\033[1;32m'
RED='\033[1;31m'
NC='\033[0m'

# remove
echo -e "${RED}[1] Removing files...${NC}"
sudo rm -rf /usr/share/world-flags-guesser /bin/{base_library.zip,certifi,ld-linux-x86-64.so.2,libbz2.so.1.0,libcrypto.so.3,lib-dynload,libffi.so.8,liblzma.so.5,libmpdec.so.3,libssl.so.3,libz.so.1,wfg}
sleep 1s

echo -e "${GREEN}[!] World Flags Guesser has been removed from your system! ${NC}"