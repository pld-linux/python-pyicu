#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	tests	# unit tests
#
Summary:	PyICU - Python 2 extension wrapping IBM's ICU C++ API
Summary(pl.UTF-8):	PyICU - rozszerzenie Pythona 2 obudowujące API C++ biblioteki ICU firmy IBM
Name:		python-pyicu
Version:	1.9.5
Release:	1
License:	MIT-like
Group:		Development/Languages/Python
Source0:	https://pypi.python.org/packages/a2/9f/1947f288143191b903e58633ee597cb98bc284de28dafb1231b6f8b67b99/PyICU-%{version}.tar.gz
# Source0-md5:	30f85b7272f15b26c110c9f3e3a9e7a0
URL:		http://site.icu-project.org/
BuildRequires:	libicu-devel >= 3.6
BuildRequires:	libstdc++-devel
%if %{with python2}
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules >= 1:2.3
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
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
%setup -q -n PyICU-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build

# tests are 2to3'ed after setup()
%{?with_tests:%py3_build test}
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
%{py_sitedir}/PyICU.py[co]
%{py_sitedir}/docs.py[co]
%{py_sitedir}/icu.py[co]
%attr(755,root,root) %{py_sitedir}/_icu.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/PyICU-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-pyicu
%defattr(644,root,root,755)
%doc CHANGES CREDITS LICENSE README.md
%{py3_sitedir}/PyICU.py
%{py3_sitedir}/docs.py
%{py3_sitedir}/icu.py
%{py3_sitedir}/__pycache__/PyICU.*.py[co]
%{py3_sitedir}/__pycache__/docs.*.py[co]
%{py3_sitedir}/__pycache__/icu.*.py[co]
%attr(755,root,root) %{py3_sitedir}/_icu.cpython-*.so
%{py3_sitedir}/PyICU-%{version}-py*.egg-info
%endif
