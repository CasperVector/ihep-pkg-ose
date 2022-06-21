%define repo motorMotorSim
%define commit R1-1
%{meta name license=EPICS github=epics-motor version=commit,1}

Summary:        EPICS - Module for a simulated motor
Patch0:         %{name}-1_1-config-bugs.patch

%{inherit motor + deps}
%description

%{inherit motor}

