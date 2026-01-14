#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	URI
%define	pnam	Fetch
Summary:	URI::Fetch - Smart URI fetching/caching
Summary(pl.UTF-8):	URI::Fetch - inteligentne pobieranie/cache'owanie URI
Name:		perl-URI-Fetch
Version:	0.09
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/URI/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cfc746bb7f142f0f5b82ea80a4416f2b
URL:		http://search.cpan.org/dist/URI-Fetch/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-ErrorHandler
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
URI::Fetch is a smart client for fetching HTTP pages, notably
syndication feeds (RSS, Atom, and others), in an intelligent,
bandwidth- and time-saving way.

%description -l pl.UTF-8
URI::Fetch to sprytny klient do pobierania stron HTTP, w szczególności
feedów zespolonych (RSS, Atom i innych) w sposób inteligentny,
oszczędzający pasmo i czas.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc Changes README
%{perl_vendorlib}/URI/*.pm
%{perl_vendorlib}/URI/Fetch
%{_mandir}/man3/*
