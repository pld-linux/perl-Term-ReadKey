%include	/usr/lib/rpm/macros.perl
Summary:	Term::ReadKey perl module
Summary(pl):	Modu� perla Term::ReadKey
Name:		perl-Term-ReadKey
Version:	2.20
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Term/TermReadKey-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	perl-TermReadKey

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
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitearch}/Term/ReadKey.pm
%dir %{perl_sitearch}/auto/Term/ReadKey
%{perl_sitearch}/auto/Term/ReadKey/autosplit.ix
%{perl_sitearch}/auto/Term/ReadKey/ReadKey.bs
%attr(755,root,root) %{perl_sitearch}/auto/Term/ReadKey/ReadKey.so
%{_mandir}/man3/*
