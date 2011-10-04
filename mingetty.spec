#specfile originally created for Fedora, modified for Moblin Linux
Summary: A compact getty program for virtual consoles only
Name: mingetty
Version: 1.08
License: GPLv2+
Release: 2
Group: System/Base
URL: http://sourceforge.net/projects/mingetty/
Source: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch: mingetty-1.00-opt.patch
BuildRoot: %{_tmppath}/%{name}-root

%description
The mingetty program is a lightweight, minimalist getty program for
use only on virtual consoles.  Mingetty is not suitable for serial
lines (you should use the mgetty program in that case).

%prep
%setup -q
%patch -p1

%build
make "RPM_OPTS=$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{sbin,%{_mandir}/man8}

install -m 0755 mingetty $RPM_BUILD_ROOT/sbin/
install -m 0644 mingetty.8 $RPM_BUILD_ROOT/%{_mandir}/man8/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING
/sbin/mingetty
%doc %{_mandir}/man8/mingetty.*

