%define repo ADPICam
%define commit 0d86faec
%{meta name license=EPICS github=areaDetector version=commit,3}
%if %{rhel} == 7
%define cmd_flags GNU_DIR=/opt/rh/devtoolset-8/root/usr \\\
	CMD_CFLAGS='%{optflags}' CMD_CXXFLAGS='%{optflags}'
%endif

Summary:        EPICS - Princeton Instruments cameras using the PICam library
Patch0:         %{name}-0d86faec-support.patch
Patch1:         %{name}-0d86faec-bugs.patch
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

