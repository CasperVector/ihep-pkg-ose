%define repo ADLambda
%define commit 05a47195
%{meta name license=EPICS github=areaDetector version=commit,2}

Summary:        EPICS - X-Spectrum Lambda pixel-array detectors
Patch0:         %{name}-05a47195-gitver.patch
Patch1:         %{name}-05a47195-assert.patch
BuildRequires:  libxsp
Requires:       libxsp

%{inherit ad + global deps}
%description

%{inherit ad}

