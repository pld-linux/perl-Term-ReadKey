#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# requires terminal
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Term
%define		pnam	ReadKey
Summary:	Term::ReadKey Perl module
Summary(cs.UTF-8):	Modul Term::ReadKey pro Perl
Summary(da.UTF-8):	Perlmodul Term::ReadKey
Summary(de.UTF-8):	Term::ReadKey Perl Modul
Summary(es.UTF-8):	Módulo de Perl Term::ReadKey
Summary(fr.UTF-8):	Module Perl Term::ReadKey
Summary(it.UTF-8):	Modulo di Perl Term::ReadKey
Summary(ja.UTF-8):	Term::ReadKey Perl モジュール
Summary(ko.UTF-8):	Term::ReadKey 펄 모줄
Summary(nb.UTF-8):	Perlmodul Term::ReadKey
Summary(pl.UTF-8):	Moduł Perla Term::ReadKey
Summary(pt.UTF-8):	Módulo de Perl Term::ReadKey
Summary(pt_BR.UTF-8):	Módulo Perl Term::ReadKey
Summary(ru.UTF-8):	Модуль для Perl Term::ReadKey
Summary(sv.UTF-8):	Term::ReadKey Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Term::ReadKey
Summary(zh_CN.UTF-8):	Term::ReadKey Perl 模块
Name:		perl-Term-ReadKey
Version:	2.30
Release:	4
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	f0ef2cea8acfbcc58d865c05b0c7e1ff
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-%{pdir}%{pnam}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module, ReadKey, provides ioctl control for terminals so the
input modes can be changed (thus allowing reads of a single character
at a time), and also provides non-blocking reads of stdin, as well as
several other terminal related features, including
retrieval/modification of the screen size, and retrieval/modification
of the control characters.

%description -l pl.UTF-8
Moduł Perla Term::ReadKey. Moduł ten daje obsługę ioctl dla terminali,
umożliwiając zmianę trybu wejścia (co pozwala na czytanie po jednym
znaku) oraz nieblokujący odczyt z wejścia, a także inne funkcje
związane z terminalem, w tym odczytywanie i modyfikowanie rozmiaru
ekranu oraz odczytywanie i modyfikowanie znaków kontrolnych.

%description -l pt_BR.UTF-8
Este módulo fornece controle via ioctl para terminais, de tal forma
que seus modos de entrada possam ser modificados (desta forma
permitindo a leitura de um caracter somente por vez) e também fornece
leitura não bloqueantes da entrada padrão (stdin), bem como várias
outras características relacionadas a terminais, entre elas a
recuperação/modificação do tamanho da tela e dos caracteres de
controle.

%prep
%setup -q -n TermReadKey-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/Term/ReadKey.pm
%dir %{perl_vendorarch}/auto/Term/ReadKey
# empty autosplit.ix
#%%{perl_vendorarch}/auto/Term/ReadKey/autosplit.ix
%{perl_vendorarch}/auto/Term/ReadKey/ReadKey.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Term/ReadKey/ReadKey.so
%{_mandir}/man3/*
