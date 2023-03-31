# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

%define module xmldiff

Name:		python-%{module}
Version:	2.4
Release:	4
Summary:	Python classes to diff XML files
URL:		http://www.logilab.org/projects/xmldiff
Source0:	https://files.pythonhosted.org/packages/76/36/a3e41bf7c01f1110d7b5589ca74d2927d3736a5b43ee63053faf3483b991/xmldiff-2.4.tar.gz
License:	GPL
Group:		File tools
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)

%description
XMLdiff is a python tool that figures out the differences between two similar
XML files, in the same way the diff utility does it for text files. It was
developed for the Narval project and could also be used as a library or as a
command line tool. It can work either with XML files or DOM trees

%files
%{_bindir}/*
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-*.egg-info

#--------------------------------------------------------------------

%prep
%autosetup -n %{module}-%{version} -p1

%build
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install --skip-build --root=%{buildroot}
rm -rf %{buildroot}%{_libdir}/python%{python2_version}/site-packages/%{module}/test
chmod 755 %{buildroot}%{_bindir}/*
