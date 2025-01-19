#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	tests	# unit tests
#
Summary:	PyICU - Python 2 extension wrapping IBM's ICU C++ API
Summary(pl.UTF-8):	PyICU - rozszerzenie Pythona 2 obudowujące API C++ biblioteki ICU firmy IBM
Name:		python-pyicu
Version:	2.14
Release:	1
License:	MIT-like
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/PyICU/
Source0:	https://files.pythonhosted.org/packages/source/P/PyICU/PyICU-%{version}.tar.gz
# Source0-md5:	7ec5ad0d62a2a27f919ca8a775352a71
Patch0:		0001-disable-failing-test.patch
URL:		https://pypi.org/project/PyICU/
BuildRequires:	libicu-devel >= 59
BuildRequires:	libstdc++-devel >= 6:4.7
%if %{with python2}
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules >= 1:2.3
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-2to3 >= 1:3.2
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-six
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyICU is a Python extension wrapping IBM's ICU C++ API.

This package contains Python 2 module.

%description -l pl.UTF-8
PyICU to rozszerzenie Pythona obudowujące API C++ biblioteki ICU firmy
IBM.

Ten pakiet zawiera moduł Pythona 2.

%package -n python3-pyicu
Summary:	PyICU - Python 3 extension wrapping IBM's ICU C++ API
Summary(pl.UTF-8):	PyICU - rozszerzenie Pythona 3 obudowujące API C++ biblioteki ICU firmy IBM
Group:		Development/Languages/Python

%description -n python3-pyicu
PyICU is a Python extension wrapping IBM's ICU C++ API.

This package contains Python 3 module.

%description -n python3-pyicu -l pl.UTF-8
PyICU to rozszerzenie Pythona obudowujące API C++ biblioteki ICU firmy
IBM.

Ten pakiet zawiera moduł Pythona 3.

%prep
%setup -q -n pyicu-%{version}
%patch0 -p1

%build
# uses ICU C++ API, which (in case if icu 59+) needs char16_t as distinct type, i.e. C++ 11
CFLAGS="%{rpmcxxflags} %{rpmcppflags} -std=c++11"

%if %{with python2}
%py_build

# tests need module already built
%{?with_tests:PYTHONPATH=$(pwd)/$(echo build-2/lib.*) %{__python} -m unittest discover -s test}
%endif

%if %{with python3}
%py3_build

# tests to be 2to3'ed (by setup) and module already built
%{?with_tests:PYTHONPATH=$(pwd)/$(echo build-3/lib.*) %{__python3} -m unittest discover -s test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS LICENSE README.md
%dir %{py_sitedir}/icu
%{py_sitedir}/icu/__init__.py[co]
%attr(755,root,root) %{py_sitedir}/icu/_icu_.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/PyICU-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-pyicu
%defattr(644,root,root,755)
%doc CHANGES CREDITS LICENSE README.md
%dir %{py3_sitedir}/icu
%{py3_sitedir}/icu/__init__.py
%{py3_sitedir}/icu/__pycache__
%attr(755,root,root) %{py3_sitedir}/icu/_icu_.cpython-*.so
%{py3_sitedir}/PyICU-%{version}-py*.egg-info
%endif
