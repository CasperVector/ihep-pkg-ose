%define repo ADLambda
%define commit b2ebf7d8
%{meta name license=EPICS github=areaDetector version=20250823,1.commit}

Summary:        EPICS - X-Spectrum Lambda pixel-array detectors
Patch0:         %{name}-05a47195-gitver.patch
Patch1:         %{name}-05a47195-assert.patch
BuildRequires:  libxsp
Requires:       libxsp

%{inherit ad + global deps}
%description

%{inherit ad}

