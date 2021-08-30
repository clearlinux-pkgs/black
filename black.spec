#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : black
Version  : 21.8b0
Release  : 21
URL      : https://files.pythonhosted.org/packages/09/b0/045f72ac95cd8e2a0e457fb383022e032dc86c040f9b6eaba67968b001e3/black-21.8b0.tar.gz
Source0  : https://files.pythonhosted.org/packages/09/b0/045f72ac95cd8e2a0e457fb383022e032dc86c040f9b6eaba67968b001e3/black-21.8b0.tar.gz
Summary  : The uncompromising code formatter.
Group    : Development/Tools
License  : MIT Python-2.0
Requires: black-bin = %{version}-%{release}
Requires: black-license = %{version}-%{release}
Requires: black-python = %{version}-%{release}
Requires: black-python3 = %{version}-%{release}
Requires: aiohttp
Requires: aiohttp-cors
Requires: click
Requires: colorama
Requires: dataclasses
Requires: ipython
Requires: mypy_extensions
Requires: pathspec
Requires: platformdirs
Requires: regex
Requires: tomli
Requires: typed_ast
Requires: typing_extensions
BuildRequires : aiohttp
BuildRequires : aiohttp-cors
BuildRequires : buildreq-distutils3
BuildRequires : click
BuildRequires : colorama
BuildRequires : dataclasses
BuildRequires : ipython
BuildRequires : mypy_extensions
BuildRequires : pathspec
BuildRequires : platformdirs
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : regex
BuildRequires : tomli
BuildRequires : tox
BuildRequires : typed_ast
BuildRequires : typing_extensions
BuildRequires : virtualenv

%description
A subset of lib2to3 taken from Python 3.7.0b2.
Commit hash: 9c17e3a1987004b8bcfbe423953aad84493a7984

%package bin
Summary: bin components for the black package.
Group: Binaries
Requires: black-license = %{version}-%{release}

%description bin
bin components for the black package.


%package license
Summary: license components for the black package.
Group: Default

%description license
license components for the black package.


%package python
Summary: python components for the black package.
Group: Default
Requires: black-python3 = %{version}-%{release}

%description python
python components for the black package.


%package python3
Summary: python3 components for the black package.
Group: Default
Requires: python3-core
Provides: pypi(black)
Requires: pypi(aiohttp)
Requires: pypi(aiohttp_cors)
Requires: pypi(click)
Requires: pypi(mypy_extensions)
Requires: pypi(pathspec)
Requires: pypi(platformdirs)
Requires: pypi(regex)
Requires: pypi(tomli)
Requires: pypi(typing_extensions)

%description python3
python3 components for the black package.


%prep
%setup -q -n black-21.8b0
cd %{_builddir}/black-21.8b0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1630339505
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/black
cp %{_builddir}/black-21.8b0/LICENSE %{buildroot}/usr/share/package-licenses/black/edd079e7a759fe1fcf1d089e28b9c7df2080b42c
cp %{_builddir}/black-21.8b0/docs/_static/license.svg %{buildroot}/usr/share/package-licenses/black/e71d25df55070a88d192a9ecf3a7ad755e44e8ee
cp %{_builddir}/black-21.8b0/src/blib2to3/LICENSE %{buildroot}/usr/share/package-licenses/black/8482348f12824b36fba59883f9dd7fe03c1f86ca
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/black
/usr/bin/black-primer
/usr/bin/blackd

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/black/8482348f12824b36fba59883f9dd7fe03c1f86ca
/usr/share/package-licenses/black/e71d25df55070a88d192a9ecf3a7ad755e44e8ee
/usr/share/package-licenses/black/edd079e7a759fe1fcf1d089e28b9c7df2080b42c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
