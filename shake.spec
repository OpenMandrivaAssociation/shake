
Name: 		shake
Version: 	0.999
Release: 	2
License: 	GPLv3
Summary: 	User-space file-system defragmenter
Group:		System/Configuration/Hardware
URL:		https://vleu.net/shake/
Source: 	http://download.savannah.nongnu.org/releases/%name/%name-%version.tar.bz2
BuildRequires: attr-devel
BuildRequires: help2man
BuildRequires: kdelibs4-devel

%description
Shake is a defragmenter that runs in user space and works on a live system.
It just works by rewriting fragmented files. But it has some heuristics that
could make it more efficient than other tools, including defrag and, maybe,
xfs_fsr.

%prep
%setup -q -n %name-fs-%version
chmod 755 COPYING GPL.txt

%build
%cmake_kde4
%make
#debug fix
cd ..
chmod 644 {linux,judge,signals,executive,msg,unattr,main}.c
chmod 644 {signals,executive,msg,judge}.h

%install
cd build
DESTDIR=%{buildroot} make install
cd ..


%files
%doc COPYING GPL.txt
%{_bindir}/*
%_mandir/man8/*



