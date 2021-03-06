#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	CPAN
Summary:	CPAN Perl module - query, download and build Perl modules from CPAN sites
Summary(pl.UTF-8):	Moduł Perla CPAN - odpytywanie, ściąganie i budowanie modułów Perla z serwisów CPAN
Name:		perl-CPAN
Version:	2.26
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CPAN/%{pdir}-%{version}.tar.gz
# Source0-md5:	f8b88baa35bd6ae582d3dd9b6c5e4771
URL:		http://search.cpan.org/dist/CPAN/
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The CPAN module is designed to automate the make and install of perl
modules and extensions. It includes some searching capabilities and
knows how to use Net::FTP or LWP (or lynx or an external FTP client)
to fetch the raw data from the net.

%description -l pl.UTF-8
Moduł CPAN służy do automatyzacji procesu budowania i instalowania
modułów i rozszerzeń Perla. Ma możliwość wyszukiwania i używania
Net::FTP lub LWP (albo lynksa czy zewnętrznego klienta FTP) do
ściągania danych z sieci.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Todo
%attr(755,root,root) %{_bindir}/cpan
%attr(755,root,root) %{_bindir}/cpan-mirrors
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/App/Cpan.pm
%dir %{perl_vendorlib}/CPAN
%{perl_vendorlib}/CPAN/*.pm
%dir %{perl_vendorlib}/CPAN/API
%{perl_vendorlib}/CPAN/API/HOWTO.pod
%dir %{perl_vendorlib}/CPAN/Exception
%{perl_vendorlib}/CPAN/Exception/*.pm
%dir %{perl_vendorlib}/CPAN/FTP
%{perl_vendorlib}/CPAN/FTP/netrc.pm
%dir %{perl_vendorlib}/CPAN/HTTP
%{perl_vendorlib}/CPAN/HTTP/*.pm
%dir %{perl_vendorlib}/CPAN/Kwalify
%{perl_vendorlib}/CPAN/Kwalify/distroprefs*
%dir %{perl_vendorlib}/CPAN/LWP
%{perl_vendorlib}/CPAN/LWP/UserAgent.pm
%dir %{perl_vendorlib}/CPAN/Plugin
%{perl_vendorlib}/CPAN/Plugin/*.pm
%{_mandir}/man1/*
%{_mandir}/man3/App::Cpan.3pm*
%{_mandir}/man3/C*
