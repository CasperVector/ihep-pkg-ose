%define repo ADAndor3
%define commit bd1f92c2
%define __elf_requires true
%{meta name license=EPICS github=areaDetector version=2_2,9.commit}

Summary:        EPICS - sCMOS area detectors using Andor SDK3

%{inherit ad + deps}
%description

%{inherit ad}

