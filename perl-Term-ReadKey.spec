#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# requires terminal
#
%define		pdir	Term
%define		pnam	ReadKey
Summary:	Term::ReadKey - Perl module for simple terminal control
Summary(pl.UTF-8):	Term::ReadKey - moduł Perla do prostego sterowania terminalem
Name:		perl-Term-ReadKey
Version:	2.38
Release:	8
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Term/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	b2b4aab7a0e6bddb7ac3b21ba637482c
URL:		https://metacpan.org/dist/TermReadKey
BuildRequires:	perl-ExtUtils-MakeMaker >= 3.5
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Obsoletes:	perl-TermReadKey < 2.38
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module, Term::ReadKey, provides ioctl control for terminals so
the input modes can be changed (thus allowing reads of a single
character at a time), and also provides non-blocking reads of stdin,
as well as several other terminal related features, including
retrieval/modification of the screen size, and retrieval/modification
of the control characters.

%description -l pl.UTF-8
Moduł Perla Term::ReadKey udostępnia obsługę ioctl dla terminali,
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
%attr(755,root,root) %{perl_vendorarch}/auto/Term/ReadKey/ReadKey.so
%{_mandir}/man3/Term::ReadKey.3pm*
