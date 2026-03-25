%define repo ADSimDetector
%define commit R2-11
%{meta name license=MIT github=areaDetector version=commit,1}

Summary:        EPICS - A simulation driver for areaDetector

%{inherit ad + global deps}
%description

%{inherit ad}

