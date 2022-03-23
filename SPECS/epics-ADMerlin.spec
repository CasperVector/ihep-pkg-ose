%define repo ADMerlin
%define commit R4-1

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        5
Summary:        EPICS - Merlin Medipix3-based pixel-array detector

License:        GPLv3
URL:            https://github.com/areaDetector/%{repo}
Source0:        %{github_archive areaDetector %{repo} %{commit}}

BuildRequires:  epics-ADCore, gcc-c++, make, libXext-devel
Requires:       epics-ADCore, libXext

%description

%{inherit ad}

