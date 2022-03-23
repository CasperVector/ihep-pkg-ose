%define repo motorScriptMotor
%define commit R1-1

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - Module for a Lua-scripted motor

License:        EPICS Open License
URL:            https://github.com/epics-motor/%{repo}
Source0:        %{github_archive epics-motor %{repo} %{commit}}

BuildRequires:  epics-motor, epics-lua, gcc-c++, make
Requires:       epics-motor

%description

%{inherit motor - prep}

%{inherit motor + prep}
echo 'LUA=$(SUPPORT)/lua' > %{repo}/configure/RELEASE.local

