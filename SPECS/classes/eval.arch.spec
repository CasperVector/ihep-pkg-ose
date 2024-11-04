%if %{_arch} == x86
%%global _bits 32
%else
%%global _bits 64
%endif
%if %{rhel} == 7
%%global _linux 3
%%global _py3 3.6
%else
%%global _linux 4
%%global _py3 3.9
%endif

