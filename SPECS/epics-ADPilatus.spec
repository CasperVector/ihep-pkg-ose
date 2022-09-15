%define repo ADPilatus
%define commit 35d95b63
%{meta name license=EPICS github=areaDetector version=2_9,10.commit}

Summary:        EPICS - Dectris Pilatus pixel-array detectors
Patch0:         %{name}-35d95b63-escape.patch

%{inherit ad + deps}
%description

%{inherit ad}

