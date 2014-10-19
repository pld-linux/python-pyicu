#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
#
Summary:	PyICU - Python 2 extension wrapping IBM's ICU C++ API
Summary(pl.UTF-8):	PyICU - rozszerzenie Pythona 2 obudowujące API C++ biblioteki ICU firmy IBM
Name:		python-pyicu
Version:	1.8
Release:	3
License:	MIT-like
Group:		Development/Languages/Python
Source0:	https://pypi.python.org/packages/source/P/PyICU/PyICU-%{version}.tar.gz
# Source0-md5:	00c8d40e5400f52c8474aa9480e8dbc1
URL:		http://pyicu.osafoundation.org/
BuildRequires:	libicu-devel >= 3.6
BuildRequires:	libstdc++-devel
%if %{with python2}
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules >= 1:2.3
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 3.2
BuildRequires:	python3-modules >= 3.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.612
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
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python} setup.py build \
	--build-base build-2
%endif

%if %{with python3}
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python3} setup.py build \
	--build-base build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py build \
		--build-base build-2 \
	install \
		--skip-build \
		--optimize=2 \
		--root=$RPM_BUILD_ROOT

%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py build \
		--build-base build-3 \
	install \
		--skip-build \
		--optimize=2 \
		--root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS LICENSE README
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
%doc CHANGES CREDITS LICENSE README
%{py3_sitedir}/PyICU.py
%{py3_sitedir}/docs.py
%{py3_sitedir}/icu.py
%{py3_sitedir}/__pycache__/PyICU.*.py[co]
%{py3_sitedir}/__pycache__/docs.*.py[co]
%{py3_sitedir}/__pycache__/icu.*.py[co]
%attr(755,root,root) %{py3_sitedir}/_icu.cpython-*.so
%{py3_sitedir}/PyICU-%{version}-py*.egg-info
%endif
