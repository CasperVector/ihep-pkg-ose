%define repo ADPandABlocks
%define commit 20220422
%{meta name license=EPICS version=4_15,2.commit}

Summary:        EPICS - Driver for streaming data from PandABlocks-server
URL:            https://github.com/PandABlocks/%{repo}
Source0:        %{github_archive_ver CasperVector %{repo} %{commit} v}

%{inherit ad + global deps}
%description

%{inherit ad - prep}

%{inherit ad + prep}
rm %{repo}/configure/CONFIG_SITE.%{epics_arch}.Common

