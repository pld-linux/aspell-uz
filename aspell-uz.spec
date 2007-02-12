Summary:	Uzbek dictionary for aspell
Summary(pl.UTF-8):	Słownik uzbecki dla aspella
Name:		aspell-uz
Version:	0.6
%define	subv	0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/uz/aspell6-uz-%{version}-%{subv}.tar.bz2
# Source0-md5:	e0d72a8250bba1a1f40dfb2a163eed65
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Uzbek dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik uzbecki (lista słów) dla aspella.

%prep
%setup -q -n aspell6-uz-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright doc/{ChangeLog,README}
%{_libdir}/aspell/*
%{_datadir}/aspell/*
