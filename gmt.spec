%global completion_dir %(pkg-config --variable=completionsdir bash-completion)
%if "%{completion_dir}" == ""
%global completion_dir /etc/bash_completion.d
%endif

Name:           gmt
Version:        6.1.1
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
GMT is an open-source collection of command-line tools for manipulating geographic
and Cartesian data sets (including filtering, trend fitting, gridding, projecting, etc.)
and producing PostScript illustrations ranging from simple x–y plots via contour maps
to artificially illuminated surfaces and 3D perspective views.
It supports many map projections and transformations and includes supporting data
such as coastlines, rivers, and political boundaries and optionally country polygons.


%prep
%autosetup


%build
mkdir build
pushd build
%{cmake} \
  -DGSHHG_ROOT=%{_datadir}/gshhg-gmt \
  -DCOPY_GSHHG=off \
  -DDCW_ROOT=%{_datadir}/dcw-gmt \
  -DCOPY_DCW=off \
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
* Wed Sep 2 2020 seisman <seisman.info@gmail.com> 6.1.1-1
- Update to 6.1.1
* Sun Jul 5 2020 seisman <seisman.info@gmail.com> 6.1.0-1
- Update to 6.1.0
- Add GDAL support for CentOS 8
* Sun Jun 7 2020 seisman <seisman.info@gmail.com> 6.0.0-2
- Add GDAL support for CentOS 8
* Fri Nov 1 2019 seisman <seisman.info@gmail.com> 6.0.0-1
- Update to 6.0.0
* Wed Oct 23 2019 seisman <seisman.info@gmail.com> 6.0.0rc5-1
- Update to 6.0.0rc5
* Fri Oct 11 2019 seisman <seisman.info@gmail.com> 6.0.0rc4-1
- Initial package
