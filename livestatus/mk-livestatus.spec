Name:		mk-livestatus
Version:	1.2.12p7
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
Ze cool

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/unixcat
%{_libdir}/mk-livestatus/livestatus.o

%doc



%changelog

