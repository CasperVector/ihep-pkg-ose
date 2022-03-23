%define repo ADSimDetector
%define commit e6c4a708

Name:           epics-%{repo}
Version:        2_10
Release:        1.%{commit}
Summary:        EPICS - A simulation driver for areaDetector

License:        MIT
URL:            https://github.com/areaDetector/%{repo}
Source0:        %{github_archive areaDetector %{repo} %{commit}}

BuildRequires:  epics-ADCore, gcc-c++, make, libXext-devel
Requires:       epics-ADCore, libXext

%description

%{inherit ad}

