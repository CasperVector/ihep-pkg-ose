%define repo ADIRay
%define commit v20240908
%{meta name license=EPICS codeberg=CasperVector version=commit,1}

Summary:        EPICS - iRay Mercu detectors
Requires:       xdma-driver

%{inherit ad + global deps}
%description

%{inherit ad}
