%define repo ADAndor
%define commit f4f28bdb
%{meta name license=EPICS github=areaDetector version=2_8,3.commit}

Summary:        EPICS - CCD area detectors using Andor SDK2
Patch0:         %{name}-2_8-support.patch
Patch1:         %{name}-2_8-default.patch
BuildRequires:  andor-sdk2
Requires:       andor-sdk2

%{inherit ad + global deps}
%description

%{inherit ad - prep}

%{inherit ad + prep}
mv %{repo}/*Support/ShamrockCIF.h %{repo}/*App/src
rm -rf %{repo}/*Support

