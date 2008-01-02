%define module	xmldiff
%define name	python-%{module}
%define version 0.6.8
%define release %mkrel 1

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
Summary:	    Python classes to diff XML files
URL:		    http://www.logilab.org/projects/xmldiff
Source:		    ftp://ftp.logilab.org/pub/xmldiff/%{module}-%{version}.tar.gz
Patch:          %{module}-0.6.8-fix-build.patch
License:	    GPL
Group:		    File tools
BuildRequires:	python-devel
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
XMLdiff is a python tool that figures out the differences between two similar
XML files, in the same way the diff utility does it for text files. It was
developed for the Narval project and could also be used as a library or as a
command line tool. It can work either with XML files or DOM trees

%prep
%setup -q -n %{module}-%{version}
%patch -p 1

%build
export CFLAGS="%{optflags}"
python setup.py build

%install
python setup.py install --root=%{buildroot} --record=INSTALLED_FILES
rm -rf %{buildroot}%{_libdir}/python%{pyver}/site-packages/%{module}/test
chmod 755 %{buildroot}%{_bindir}/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog DEPENDS README README.xmlrev TODO
%{_bindir}/*
%{_datadir}/sgml/stylesheet/%{module}
%{py_platsitedir}/%{module}
%{py_platsitedir}/%{module}-*.egg-info
