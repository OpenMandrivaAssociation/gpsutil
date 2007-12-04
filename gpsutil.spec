%define name	gpsutil
%define version	0.10
%define release  %mkrel 2

Name: 	 	%{name}
Summary: 	Transfers data to/from a Magellan or NMEA-compliant GPS
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://www.cs.uakron.edu/~hennings/gpsutil/
License:	GPL
Group:		Communications
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
GPSUTIL is a program to communicate with a GPS unit. It supports several NMEA
(National Marine Electronics Association) v2.1 messages. GPSUTIL also supports
downloading, uploading, and deleting waypoints from a Magellan GPS.

Currently supported NMEA messages:
GLL - Current latitude and longitude
RMB - Information about current waypoint destination
RMC - Speed (in knots) and current heading

%prep
%setup -q -n %name
rm -f %name

%build
%make CC="gcc $RPM_OPT_FLAGS"
										
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir
cp %name $RPM_BUILD_ROOT/%_bindir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc readme todo changelog example.wpts license.txt
%{_bindir}/%name

