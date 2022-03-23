%define repo softGlue
%define commit R2-8-3

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - Construct small, simple, digital electronic circuits

License:        EPICS Open License
URL:            https://github.com/epics-modules/%{repo}
Source0:        %{github_archive epics-modules %{repo} %{commit}}

BuildRequires:  epics-asyn, epics-ipac, gcc-c++, make
Requires:       epics-asyn, epics-ipac

%description

%{inherit synapps}

