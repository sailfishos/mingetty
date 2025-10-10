# Spec file originally created for Fedora,
# modified for Moblin Linux and Sailfish OS
Summary:   A compact getty program for virtual consoles only
Name:      mingetty
Version:   1.08
License:   GPLv2+
Release:   2
URL:       http://sourceforge.net/projects/mingetty/
Source:    http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch1:    mingetty-1.00-opt.patch

%description
The mingetty program is a lightweight, minimalist getty program for
use only on virtual consoles.  Mingetty is not suitable for serial
lines (you should use the mgetty program in that case).

%prep
%autosetup -p1

%build
%make_build

%install
mkdir -p $RPM_BUILD_ROOT/sbin
install -m 0755 mingetty $RPM_BUILD_ROOT/sbin/

%files
%license COPYING
/sbin/mingetty
