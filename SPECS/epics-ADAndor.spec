%define repo ADAndor
%define commit f4f28bdb
%{meta name license=EPICS github=areaDetector version=2_8,2.commit}

Summary:        EPICS - CCD area detectors using Andor SDK2

%{inherit ad + global deps}
%description

%{inherit ad}

