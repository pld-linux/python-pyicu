Summary:	PyICU - Python extension wrapping IBM's ICU C++ API
Summary(pl.UTF-8):	PyICU - rozszerzenie Pythona obudowujące API C++ biblioteki ICU firmy IBM
Name:		python-pyicu
Version:	1.3
Release:	1
License:	MIT-like
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/P/PyICU/PyICU-%{version}.tar.gz
# Source0-md5:	c1d1b8ec79d0f6c670a8f093792c180f
URL:		http://pyicu.osafoundation.org/
BuildRequires:	libicu-devel >= 3.6
BuildRequires:	libstdc++-devel
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyICU is a Python extension wrapping IBM's ICU C++ API.

%description -l pl.UTF-8
PyICU to rozszerzenie Pythona obudowujące API C++ biblioteki ICU firmy
IBM.

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
%{py_sitedir}/PyICU-%{version}-py*.egg-info
%endif
