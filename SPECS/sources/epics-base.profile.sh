EPICS_BASE=@etop_base@
export EPICS_BASE
EPICS_HOST_ARCH=@epics_arch@
export EPICS_HOST_ARCH
PATH="$PATH":"$EPICS_BASE"/bin/"$EPICS_HOST_ARCH"
export PATH
EPICS_CA_ADDR_LIST=127.255.255.255
export EPICS_CA_ADDR_LIST
EPICS_CA_AUTO_ADDR_LIST=NO
export EPICS_CA_AUTO_ADDR_LIST

