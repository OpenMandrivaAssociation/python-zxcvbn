Name:		python-zxcvbn
Version:	4.5.0
Release:	1
Summary:	zxcvbn
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/zxcvbn/
Source0:	zxcvbn-4.5.0.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch
%description
zxcvbn.

%files
%{py_sitedir}/*
%{_bindir}/*
