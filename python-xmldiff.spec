%define module	xmldiff
# we don't want to provide private python extension libs
%define _exclude_files_from_autoprov %{python_sitearch}/.*\\.so\\|%{python3_sitearch}/.*\\.so

Name:          python-%{module}
Version:       0.6.10
Release:       1
Summary:       Python classes to diff XML files
URL:           http://www.logilab.org/projects/xmldiff
Source0:        http://download.logilab.org/pub/xmldiff/%{module}-%{version}.tar.gz
License:       GPL
Group:         File tools
BuildRequires:	pkgconfig(python)
BuildRequires:  python3dist(setuptools)

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
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{optflags}" %__python setup.py build

%install
%__python setup.py install --root=%{buildroot}
rm -rf %{buildroot}%{_libdir}/python%{python2_version}/site-packages/%{module}/test
chmod 755 %{buildroot}%{_bindir}/*
