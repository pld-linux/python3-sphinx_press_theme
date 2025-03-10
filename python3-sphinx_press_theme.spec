#
# Conditional build:
%bcond_without	doc	# API documentation

%define		module	template
Summary:	Sphinx-doc theme based on Vuepress
Summary(pl.UTF-8):	Motyw Sphinksa oparty na Vuepress
Name:		python3-sphinx_press_theme
Version:	0.8.0
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-press-theme/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-press-theme/sphinx_press_theme-%{version}.tar.gz
# Source0-md5:	fb9bcb898c04a280ccc15ade8cf173de
URL:		https://pypi.org/project/sphinx-press-theme/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-3 >= 4.0.1
%endif
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A modern responsive theme for Python's Sphinx documentation generator.
This theme is based on VuePress <https://vuepress.vuejs.org/>.

%description -l pl.UTF-8
Nowoczesny, responsywny motyw dla pythonowego generatora dokumentacji
Sphinx. Motyw jest oparty na VuePress <https://vuepress.vuejs.org/>.

%package apidocs
Summary:	API documentation for Python sphinx_press_theme module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona sphinx_press_theme
Group:		Documentation

%description apidocs
API documentation for Python sphinx_press_theme module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona sphinx_press_theme.

%prep
%setup -q -n sphinx_press_theme-%{version}

%build
%py3_build

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE README.md
%{py3_sitescriptdir}/sphinx_press_theme
%{py3_sitescriptdir}/sphinx_press_theme-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_static,theme-demo,*.html,*.js}
%endif
