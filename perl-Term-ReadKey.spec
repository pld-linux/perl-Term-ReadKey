#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# requires terminal
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Term
%define		pnam	ReadKey
Summary:	Term::ReadKey Perl module
Summary(cs):	Modul Term::ReadKey pro Perl
Summary(da):	Perlmodul Term::ReadKey
Summary(de):	Term::ReadKey Perl Modul
Summary(es):	M�dulo de Perl Term::ReadKey
Summary(fr):	Module Perl Term::ReadKey
Summary(it):	Modulo di Perl Term::ReadKey
Summary(ja):	Term::ReadKey Perl �⥸�塼��
Summary(ko):	Term::ReadKey �� ����
Summary(nb):	Perlmodul Term::ReadKey
Summary(pl):	Modu� Perla Term::ReadKey
Summary(pt):	M�dulo de Perl Term::ReadKey
Summary(pt_BR):	M�dulo Perl Term::ReadKey
Summary(ru):	������ ��� Perl Term::ReadKey
Summary(sv):	Term::ReadKey Perlmodul
Summary(uk):	������ ��� Perl Term::ReadKey
Summary(zh_CN):	Term::ReadKey Perl ģ��
Name:		perl-Term-ReadKey
Version:	2.21
Release:	3
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	888aabb723b8c21e35c55e979655f08e
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

%description -l pl
Modu� perla Term::ReadKey. Modu� ten daje obs�ug� ioctl dla terminali,
umo�liwiaj�c zmian� trybu wej�cia (co pozwala na czytanie po jednym
znaku) oraz nieblokuj�cy odczyt z wej�cia, a tak�e inne funkcje
zwi�zane z terminalem, w tym odczytywanie i modyfikowanie rozmiaru
ekranu oraz odczytywanie i modyfikowanie znak�w kontrolnych.

%description -l pt_BR
Este m�dulo fornece controle via ioctl para terminais, de tal forma
que seus modos de entrada possam ser modificados (desta forma
permitindo a leitura de um caracter somente por vez) e tamb�m fornece
leitura n�o bloqueantes da entrada padr�o (stdin), bem como v�rias
outras caracter�sticas relacionadas a terminais, entre elas a
recupera��o/modifica��o do tamanho da tela e dos caracteres de
controle.

%prep
%setup -q -n TermReadKey-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
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
