%define repo ADPICam
%define commit 674983bc
%{meta name license=EPICS github=areaDetector version=commit,2}
%if %{rhel} == 7
%define cmd_flags GNU_DIR=/opt/rh/devtoolset-8/root/usr \\\
	CMD_CFLAGS='%{optflags}' CMD_CXXFLAGS='%{optflags}'
%endif

Summary:        EPICS - Princeton Instruments cameras using the PICam library
Patch0:         %{name}-674983bc-support.patch
Patch1:         %{name}-674983bc-readout.patch
Patch2:         %{name}-674983bc-printf.patch
BuildRequires:  picam-sdk
Requires:       picam-sdk
%if %{rhel} == 7
BuildRequires:  devtoolset-8
%endif

%{inherit ad + global deps}
%description

%{inherit ad - prep build}

%{inherit ad + prep}
rm -rf %{repo}/*Support

%build
%if %{rhel} == 7
. /opt/rh/devtoolset-8/enable
%endif
%_mtr_ad_build

