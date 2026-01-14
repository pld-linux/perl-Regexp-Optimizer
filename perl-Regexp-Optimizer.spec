#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Regexp
%define		pnam	Optimizer
Summary:	Regexp::Optimizer - builds regular expressions out of a list of words
Summary(pl.UTF-8):	Regexp::Optimizer - tworzenie wyrażeń regularnych z listy słów
Name:		perl-Regexp-Optimizer
Version:	0.15
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f44212198ae95f33a836002a0123007f
URL:		http://search.cpan.org/dist/Regexp-Optimizer/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module offers "list2re" method that turns a list of words into an
optimized regular expression which matches all words therein. The
optimized regular expression is much more efficient than a
simple-minded '|'-concatenation thereof.

%description -l pl.UTF-8
Ten moduł udostępnia metodę list2re, która zamienia listę słów na
zoptymalizowane wyrażenie regularne, które pasuje do podanych słów.
Wyrażenie zoptymalizowane jest bardziej wydajne niż proste połączenie
słów znakami '|'.

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
cp -p eg/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Regexp/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
