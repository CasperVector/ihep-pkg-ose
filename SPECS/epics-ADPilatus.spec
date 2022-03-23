%define repo ADPilatus
%define commit R2-9

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        7
Summary:        EPICS - Dectris Pilatus pixel-array detectors

License:        EPICS Open License
URL:            https://github.com/areaDetector/%{repo}
Source0:        %{github_archive areaDetector %{repo} %{commit}}

BuildRequires:  epics-ADCore, gcc-c++, make, libXext-devel
Requires:       epics-ADCore, libXext

%description

%{inherit ad}

