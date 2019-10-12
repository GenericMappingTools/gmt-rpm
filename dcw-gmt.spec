Name:           dcw-gmt
Version:        1.1.4
Release:        1%{?dist}
Summary:        Digital Chart of the World (DCW) for GMT

License:        LGPLv3+
URL:            https://www.soest.hawaii.edu/pwessel/dcw/
Source0:        https://www.soest.hawaii.edu/pwessel/dcw/%{name}-%{version}.tar.gz
BuildArch:      noarch


%description
DCW-GMT is an enhancement to the original 1:1,000,000 scale vector basemap of
the world available from the Princeton University Digital Map and Geospatial
Information Center and from GeoCommunity at
http://data.geocomm.com/readme/dcw/dcw.html.
This data is for use by GMT, the Generic Mapping Tools.


%prep
%autosetup


%install
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -a dcw-*.nc dcw-*.txt %{buildroot}/%{_datadir}/%{name}/


%files
%doc COPYING.LESSERv3 COPYINGv3 LICENSE.TXT README.TXT ChangeLog
%{_datadir}/%{name}/


%changelog
* Fri Oct 11 2019 seisman <seisman.info@gmail.com> 1.1.4-1
- Initial package
