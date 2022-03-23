%define repo autosave
%define commit R5-10-2

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - Automatic save/restore of PVs

License:        EPICS Open License
URL:            https://github.com/epics-modules/%{repo}
Source0:        %{github_archive epics-modules %{repo} %{commit}}
Patch0:         %{name}-5_10_2-files.patch

BuildRequires:  epics-support, gcc-c++, make
Requires:       epics-support

%description

%{inherit synapps}

