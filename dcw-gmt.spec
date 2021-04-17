Name:           dcw-gmt
Version:		2.0.0
Release:        1%{?dist}
Summary:        Digital Chart of the World (DCW) for GMT

License:        LGPLv3+
URL:            https://github.com/GenericMappingTools/dcw-gmt
Source0:        https://github.com/GenericMappingTools/dcw-gmt/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
DCW-GMT is an enhancement to the original 1:1,000,000 scale vector basemap of the world,
available from the Princeton University Digital Map and Geospatial Information Center.
It contains more state boundaries (the largest 8 countries are now represented) than
the original data source. Information about DCW can be found on
Wikipedia (https://en.wikipedia.org/wiki/Digital_Chart_of_the_World).
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
* Sat Apr 17 2021 seisman <seisman.info@gmail.com> 2.0.0-1
- Update to 2.0.0
* Fri Oct 11 2019 seisman <seisman.info@gmail.com> 1.1.4-1
- Initial package
