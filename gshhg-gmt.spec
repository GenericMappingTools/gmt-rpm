Name:           gshhg-gmt
Version:        2.3.7
Release:        1%{?dist}
Summary:        Global Self-consistent Hierarchical High-resolution Geography (GSHHG)

License:        LGPLv3+
URL:            https://www.soest.hawaii.edu/pwessel/gshhg/
Source0:        https://www.soest.hawaii.edu/pwessel/gshhg/%{name}-%{version}.tar.gz
BuildArch:      noarch
# gshhg-gmt conflicts with gshhg-gmt-nc4* provided by Fedora/EPEL
Conflicts:      gshhg-gmt-nc4
Conflicts:      gshhg-gmt-nc4-full
Conflicts:      gshhg-gmt-nc4-high

%description
GSHHG is a high-resolution shoreline data set amalgamated from two databases:
Global Self-consistent Hierarchical High-resolution Shorelines (GSHHS) and
CIA World Data Bank II (WDBII). GSHHG contains vector descriptions at five
different resolutions of land outlines, lakes, rivers, and political
boundaries. This data is for use by GMT, the Generic Mapping Tools.

%prep
%setup -q

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -a *.nc %{buildroot}/%{_datadir}/%{name}


%files
%doc COPYING.LESSERv3 COPYINGv3 LICENSE.TXT README.TXT
%{_datadir}/%{name}/*.nc

%changelog
* Fri Oct 11 2019 seisman <seisman.info@gmail.com> 2.3.7-1
- Initail package
