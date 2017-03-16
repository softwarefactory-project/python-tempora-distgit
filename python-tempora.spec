%global sum     Objects and routines pertaining to date and time (tempora).

Name:           python-tempora
Version:        1.6.1
Release:        1%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/jaraco/tempora
Source0:        https://github.com/jaraco/tempora/archive/%{version}.tar.gz

BuildArch:      noarch


%description
Modules include:

tempora (top level package module) contains miscellaneous utilities and constants.
timing contains routines for measuring and profiling.
schedule contains an event scheduler.


%package -n python2-tempora
Summary:        %sum

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python2-setuptools_scm

Requires:       python-setuptools
Requires:       python-six
Requires:       pytz


%description -n python2-tempora
Modules include:

tempora (top level package module) contains miscellaneous utilities and constants.
timing contains routines for measuring and profiling.
schedule contains an event scheduler.


%prep
%autosetup -n tempora-%{version}

# Remove setuptools_scm min version requirements
sed -i "s|setuptools_scm>=.*|setuptools_scm',|" setup.py


%build
SETUPTOOLS_SCM_PRETEND_VERSION=%{version} %{__python2} setup.py build


%install
SETUPTOOLS_SCM_PRETEND_VERSION=%{version} %{__python2} setup.py install --skip-build --root %{buildroot}


%files
%doc CHANGES.rst


%files -n python2-tempora
%{_bindir}/calc-prorate
%{python2_sitelib}/tempora-%{version}-py*.egg-info
%{python2_sitelib}/tempora


%changelog
* Thu Mar 16 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 1.6.1-1
- Initial packaging
