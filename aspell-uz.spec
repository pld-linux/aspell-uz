Summary:	Uzbek dictionary for aspell
Summary(pl):	S³ownik uzbecki dla aspella
Name:		aspell-uz
Version:	0.02
%define	subv	1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/uz/aspell6-uz-%{version}-%{subv}.tar.bz2
# Source0-md5:	02145328b6839d62d8f2e62e6a620a69
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 0.60.0
Requires:	aspell >= 0.60.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Uzbek dictionary (i.e. word list) for aspell.

%description -l pl
S³ownik uzbecki (lista s³ów) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

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
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
