%define repo ADAndor3
%define commit bd1f92c2
%define __elf_requires true
%undefine _missing_build_ids_terminate_build
%{meta name license=EPICS github=areaDetector version=2_2,7.commit}

Summary:        EPICS - sCMOS area detectors using Andor SDK3

%{inherit ad + deps}
%description

%{inherit ad - prep}

%{inherit ad + prep}
%_fix_arch *IOC/iocBoot/ioc*/Makefile

