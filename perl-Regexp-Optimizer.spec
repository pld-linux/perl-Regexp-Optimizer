#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Regexp
%define	pnam	Optimizer
Summary:	Regexp::Optimizer - builds regular expressions out of a list of words
Summary(pl):	Regexp::Optimizer - tworzenie wyra¿eñ regularnych z listy s³ów
Name:		perl-Regexp-Optimizer
Version:	0.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f0caefd96e2c3a836c4ad6b5b76e967b
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module offers "list2re" method that turns a list of words into an
optimized regular expression which matches all words therein. The
optimized regular expression is much more efficient than a
simple-minded '|'-concatenation thereof.

%description -l pl
Ten modu³ udostêpnia metodê list2re, która zamienia listê s³ów na
zoptymalizowane wyra¿enie regularne, które pasuje do podanych s³ów.
Wyra¿enie zoptymalizowane jest bardziej wydajne ni¿ proste po³±czenie
s³ów znakami '|'.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"Regexp")' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install eg/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Regexp/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
