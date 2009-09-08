Name: 		shake
Version: 	0.29
Release: 	%mkrel 5
License: 	GPL
Summary: 	Userspace filesystem defragmenter
Group:		System/Configuration/Hardware
URL:		http://vleu.net/shake/
Source: 	%name-%version.tar.bz2
BuildRequires: attr-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}-build

%description
Shake is a defragmenter that runs in userspace and works on a live system.
It just works by rewriting fragmented files. But it has some heuristics that
could make it more efficient than other tools, including defrag and, maybe,
xfs_fsr.

%prep
%setup -q


%build
%make

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%_bindir,%_mandir/man8}
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_bindir}/*
%_mandir/man8/*

