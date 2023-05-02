%define repo ADAndor3
%define commit bd1f92c2
%{meta name license=EPICS github=areaDetector version=2_2,10.commit}

Summary:        EPICS - sCMOS area detectors using Andor SDK3

%{inherit ad + global deps}
%description

%{inherit ad}

