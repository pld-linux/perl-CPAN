#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CPAN
Summary:	CPAN Perl module - query, download and build Perl modules from CPAN sites
Summary(pl):	Modu³ Perla CPAN - odpytywanie, ¶ci±ganie i budowanie modu³ów Perla z serwisów CPAN
Name:		perl-CPAN
Version:	1.83
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	ee3e7f4385103339be28e03c9a2b655e
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

%description -l pl
Modu³ CPAN s³u¿y do automatyzacji procesu budowania i instalowania
modu³ów i rozszerzeñ Perla. Ma mo¿liwo¶æ wyszukiwania i u¿ywania
Net::FTP lub LWP (albo lynksa czy zewnêtrznego klienta FTP) do
¶ci±gania danych z sieci.

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
%doc ChangeLog Todo
%attr(755,root,root) %{_bindir}/cpan
%{perl_vendorlib}/*.pm
%dir %{perl_vendorlib}/CPAN
%{perl_vendorlib}/CPAN/*.pm
%{_mandir}/man1/*
%{_mandir}/man3/C*
