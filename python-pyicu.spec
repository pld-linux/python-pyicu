%define 	module	pyicu
Summary:	PyICU is a python extension wrapping IBM's ICU C++ API
Name:		python-%{module}
Version:	0.8.1
Release:	1
License:	GPL
Group:		Base
URL:		http://pyicu.osafoundation.org/
Source0:	http://pypi.python.org/packages/source/P/PyICU/PyICU-%{version}.tar.gz
# Source0-md5:	789092993f84ccd6ba21d7346d6e093d
BuildRequires:	libicu-devel >= 3.6
BuildRequires:	libstdc++-devel
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	libicu >= 3.6
Requires:	libstdc++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyICU is a python extension wrapping IBM's ICU C++ API.

%prep
%setup -q -n PyICU-%{version}

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS LICENSE README
%{py_sitedir}/PyICU.py
%{py_sitedir}/PyICU.py[co]
%{py_sitedir}/_PyICU.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/PyICU-%{version}*.egg-info
%endif
