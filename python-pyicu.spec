%define 	module	pyicu
Summary:	PyICU is a python extension wrapping IBM's ICU C++ API
Name:		python-%{module}
Version:	1.2
Release:	1
License:	BSD-like
Group:		Development/Languages/Python
URL:		http://pyicu.osafoundation.org/
Source0:	http://pypi.python.org/packages/source/P/PyICU/PyICU-%{version}.tar.gz
# Source0-md5:	d2d20ab5b233f1d6d2d7e69ba8b5f959
BuildRequires:	libicu-devel >= 3.6
BuildRequires:	libstdc++-devel
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
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
%{py_sitedir}/PyICU.py[co]
%{py_sitedir}/docs.py[co]
%{py_sitedir}/icu.py[co]
%attr(755,root,root) %{py_sitedir}/_icu.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/PyICU-%{version}*.egg-info
%endif
