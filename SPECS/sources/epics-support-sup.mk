TOP = ..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

INC += $(patsubst ../%, %, $(wildcard ../*.h))

ifeq (linux-x86_64, $(findstring linux-x86_64, $(T_A)))
LIB_INSTALLS += $(wildcard ../os/linux-x86_64/*.a)
LIB_INSTALLS += $(wildcard ../os/linux-x86_64/*.so*)
else ifeq (windows-x64, $(findstring windows-x64, $(T_A)))
LIB_INSTALLS += $(wildcard ../os/windows-x64/*.lib)
BIN_INSTALLS += $(wildcard ../os/windows-x64/*.dll)
endif

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

