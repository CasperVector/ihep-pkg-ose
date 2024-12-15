%define repo ADAndor3
%define commit bd1f92c2
%{meta name license=EPICS github=areaDetector version=2_2,11.commit}

Summary:        EPICS - sCMOS area detectors using Andor SDK3
Patch0:         %{name}-2_2-support.patch
BuildRequires:  andor-sdk3
Requires:       andor-sdk3

%{inherit ad + global deps}
%description

%{inherit ad - prep}

%{inherit ad + prep}
rm -rf %{repo}/*Support

