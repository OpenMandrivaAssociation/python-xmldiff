%define module	xmldiff

Summary:	Python classes to diff XML files
Name:		python-%{module}
Version:	0.6.10
Release:	7
License:	GPLv2
Group:		File tools
Url:		http://www.logilab.org/projects/xmldiff
Source0:	ftp://ftp.logilab.org/pub/xmldiff/%{module}-%{version}.tar.gz
BuildRequires:	pkgconfig(python)

%description
XMLdiff is a python tool that figures out the differences between two similar
XML files, in the same way the diff utility does it for text files. It was
developed for the Narval project and could also be used as a library or as a
command line tool. It can work either with XML files or DOM trees

%prep
%setup -qn %{module}-%{version}

%build
export CFLAGS="%{optflags}"
python setup.py build

%install
python setup.py install --root=%{buildroot} --record=INSTALLED_FILES
rm -rf %{buildroot}%{_libdir}/python%{pyver}/site-packages/%{module}/test
chmod 755 %{buildroot}%{_bindir}/*

%files
%doc ChangeLog DEPENDS README README.xmlrev TODO
%{_bindir}/*
%{_datadir}/sgml/stylesheet/%{module}
%{py_platsitedir}/%{module}
%{py_platsitedir}/%{module}-*.egg-info

