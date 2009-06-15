#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CPAN
Summary:	CPAN Perl module - query, download and build Perl modules from CPAN sites
Summary(pl.UTF-8):	Moduł Perla CPAN - odpytywanie, ściąganie i budowanie modułów Perla z serwisów CPAN
Name:		perl-CPAN
Version:	1.9304
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CPAN/%{pdir}-%{version}.tar.gz
# Source0-md5:	32d0caf8c1344e5268fbe8b5ae800236
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
%{perl_vendorlib}/*.pm
%dir %{perl_vendorlib}/CPAN
%{perl_vendorlib}/CPAN/*.pm
%{_mandir}/man1/*
%{_mandir}/man3/C*
