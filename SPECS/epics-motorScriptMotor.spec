%define repo motorScriptMotor
%define commit R1-1
%{meta name license=EPICS github=epics-motor version=commit,3}

Summary:        EPICS - Module for a Lua-scripted motor
BuildRequires:  epics-lua
Requires:       epics-lua

%{inherit motor + global deps}
%description

%{inherit motor - prep}

%{inherit motor + prep}
echo 'LUA=$(SUPPORT)/lua' > %{repo}/configure/RELEASE.local

