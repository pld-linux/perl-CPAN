#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	CPAN
Summary:	CPAN - query, download and build perl modules from CPAN sites
#Summary(pl):	
Name:		perl-CPAN
Version:	1.63
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl(File::Spec)
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The CPAN module is designed to automate the make and install of perl
modules and extensions. It includes some searching capabilities and
knows how to use Net::FTP or LWP (or lynx or an external ftp client)
to fetch the raw data from the net.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog Todo
%attr(755,root,root) %{_bindir}/cpan
%{perl_privlib}/*.pm
%{perl_privlib}/%{pdir}/*.pm
%{_mandir}/man1/*
%{_mandir}/man3/C*
