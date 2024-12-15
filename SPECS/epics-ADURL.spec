%define repo ADURL
%define commit R2-3
%{meta name license=EPICS github=areaDetector version=commit,2}

Summary:        EPICS - areaDetector driver for reading images from a URL

%{inherit ad + global deps}
%description

%{inherit ad}

