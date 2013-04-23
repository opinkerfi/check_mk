Name:		mk-livestatus
Version:	1.3.12p7
Release:	1%{?dist}
Summary:	Fetches status data live from the Nagios process via NEB

Group:		Applications/System
License:	GPLv2
URL:		http://mathias-kettner.de/checkmk_livestatus.html
Source0:	http://www.mathias-kettner.de/download/%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
Requires:	nagios

%description
mk-livestatus offers a new approach for accessing Nagios status and also
historic data. Just as NDO, Livestatus make use of the Nagios Event Broker API
and loads a binary module into your Nagios process. But other then NDO,
Livestatus does not actively write out data. Instead, it opens a socket by
which data can be retrieved on demand.

The socket allows you to send a request for hosts, services or other pieces of
data and get an immediate answer. The data is directly read from Nagios'
internal data structures. Livestatus does not create its own copy of that data.
Beginning from version 1.1.2 you are also be able retrieve historic data from
the Nagios log files via Livestatus.

%prep
%setup -q

aclocal
autoconf
autoheader
automake -a


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/nagios/plugins
mv $RPM_BUILD_ROOT/%{_libdir}/mk-livestatus/livecheck $RPM_BUILD_ROOT/%{_libdir}/nagios/plugins/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/unixcat
%{_libdir}/mk-livestatus/livestatus.o
%{_libdir}/nagios/plugins/livecheck

%doc



%changelog
* Tue Apr 23 2013 Tomas Edwardsson <tommi@tommi.org> 1.3.12p7-1
- new package built with tito


