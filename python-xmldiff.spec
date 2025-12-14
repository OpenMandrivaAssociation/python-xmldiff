%define module xmldiff

Name:		python-%{module}
Version:	2.7.0
Release:	1
Summary:	Python classes to diff XML files
License:	GPL
Group:		Development/Python
URL:		https://github.com/Shoobx/xmldiff
Source0:	https://files.pythonhosted.org/packages/source/x/%{module}/%{module}-%{version}.tar.gz
BuildSystem:	python
BuildArch:		noarch

BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(lxml)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
XMLdiff is a python tool that figures out the differences between two similar
XML files, in the same way the diff utility does it for text files. It was
developed for the Narval project and could also be used as a library or as a
command line tool. It can work either with XML files or DOM trees

%prep
%autosetup -n %{module}-%{version} -p1
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
export CFLAGS="%{optflags}"
%py_build

%install
%py_install

%files
%doc README.rst
%license LICENSE.txt
%{_bindir}/xmlpatch
%{_bindir}/%{module}
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}*.*-info
