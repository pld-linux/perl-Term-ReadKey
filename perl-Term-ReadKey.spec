%include	/usr/lib/rpm/macros.perl
Summary:	Term-ReadKey perl module
Summary(pl):	Modu³ perla Term-ReadKey
Name:		perl-Term-ReadKey
Version:	2.14
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Term/TermReadKey-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Term-ReadKey perl module

%description -l pl
Modu³ perla Term-ReadKey

%prep
%setup -q -n TermReadKey-%{version}

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Term/ReadKey/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Term/ReadKey
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitearch}/Term/ReadKey.pm

%dir %{perl_sitearch}/auto/Term/ReadKey
%{perl_sitearch}/auto/Term/ReadKey/.packlist
%{perl_sitearch}/auto/Term/ReadKey/autosplit.ix
%{perl_sitearch}/auto/Term/ReadKey/ReadKey.bs
%attr(755,root,root) %{perl_sitearch}/auto/Term/ReadKey/ReadKey.so

%{_mandir}/man3/*
