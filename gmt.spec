%global completion_dir %(pkg-config --variable=completionsdir bash-completion)
%if "%{completion_dir}" == ""
%global completion_dir /etc/bash_completion.d
%endif

Name:           gmt
Version:        6.0.0rc4
Release:        1%{?dist}
Summary:        Generic Mapping Tools

License:        LGPLv3+
URL:            https://www.generic-mapping-tools.org/
Source0:        https://github.com/GenericMappingTools/gmt/releases/download/%{version}/%{name}-%{version}-src.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  bash-completion
BuildRequires:  libcurl-devel
BuildRequires:  netcdf-devel
BuildRequires:  gdal-devel
BuildRequires:  pcre-devel
%if 0%{?rhel} != 6
BuildRequires:  glib2-devel
%endif
BuildRequires:  fftw-devel
BuildRequires:  lapack-devel
BuildRequires:  blas-devel
BuildRequires:  zlib-devel
BuildRequires:  dcw-gmt
BuildRequires:  gshhg-gmt

Requires:       ghostscript
Requires:       xdg-utils
Requires:       dcw-gmt
Requires:       gshhg-gmt
Requires:       blas

# gmt conflicts with GMT provided by Fedora/EPEL
Conflicts:      GMT
Conflicts:      GMT-common
Conflicts:      GMT-devel
Conflicts:      GMT-doc


%description
GMT is an open source collection of ~130 tools for manipulating geographic and
Cartesian data sets and producing PostScript illustrations ranging from simple
x-y plots via contour maps to artificially illuminated surfaces and 3D perspective views.


%prep
%autosetup


%build
mkdir build
pushd build
%{cmake} \
  -DGSHHG_ROOT=%{_datadir}/gshhg-gmt \
  -DDCW_ROOT=%{_datadir}/dcw-gmt \
  -DGMT_INSTALL_MODULE_LINKS=off \
  -DGMT_INSTALL_TRADITIONAL_FOLDERNAMES=off \
  -DLICENSE_RESTRICTED=LGPL \
  -DGMT_OPENMP=on \
%if 0%{?rhel} != 6
  -DGMT_USE_THREADS=on \
%endif
  -DBASH_COMPLETION_DIR=%{completion_dir} \
  ..
%make_build


%install
%make_install -C build


%check
gmt --version
gmt defaults -Vd
gmt pscoast -R0/10/0/10 -JM6i -Ba -Ggray -ENG+p1p,blue -P -Vd > test.ps
gmt begin && gmt coast -R0/10/0/10 -JM6i -Ba -Ggray -ENG+p1p,blue -Vd && gmt end
export GMT_END_SHOW=off && gmt grdimage @earth_relief_60m -JH10c -Baf -pdf map


%ldconfig_scriptlets


%files
%doc COPYING.LESSERv3 COPYINGv3 LICENSE.TXT README.md
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*
%{_datadir}/gmt/*
%{_docdir}/gmt/*
%{completion_dir}/*


%changelog
* Fri Oct 11 2019 seisman <seisman.info@gmail.com> 6.0.0rc4-1
- Initial package
