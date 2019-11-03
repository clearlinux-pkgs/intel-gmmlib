#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : intel-gmmlib
Version  : 19.3.4
Release  : 15
URL      : https://github.com/intel/gmmlib/archive/intel-gmmlib-19.3.4/gmmlib-19.3.4.tar.gz
Source0  : https://github.com/intel/gmmlib/archive/intel-gmmlib-19.3.4/gmmlib-19.3.4.tar.gz
Summary  : Intel Graphics Memory Management Library
Group    : Development/Tools
License  : MIT
Requires: intel-gmmlib-lib = %{version}-%{release}
Requires: intel-gmmlib-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : util-linux

%description
Intel(R) Graphics Memory Management Library
*******************************************

%package dev
Summary: dev components for the intel-gmmlib package.
Group: Development
Requires: intel-gmmlib-lib = %{version}-%{release}
Provides: intel-gmmlib-devel = %{version}-%{release}
Requires: intel-gmmlib = %{version}-%{release}
Requires: intel-gmmlib = %{version}-%{release}

%description dev
dev components for the intel-gmmlib package.


%package lib
Summary: lib components for the intel-gmmlib package.
Group: Libraries
Requires: intel-gmmlib-license = %{version}-%{release}

%description lib
lib components for the intel-gmmlib package.


%package license
Summary: license components for the intel-gmmlib package.
Group: Default

%description license
license components for the intel-gmmlib package.


%prep
%setup -q -n gmmlib-intel-gmmlib-19.3.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1572795220
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1572795220
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/intel-gmmlib
cp %{_builddir}/gmmlib-intel-gmmlib-19.3.4/LICENSE.md %{buildroot}/usr/share/package-licenses/intel-gmmlib/8b0e9f012620e45a7426bb39ecc64a0cd2f876b1
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/igdgmm/GmmLib/CachePolicy/GmmCachePolicyConditionals.h
/usr/include/igdgmm/GmmLib/CachePolicy/GmmCachePolicyResourceUsageDefinitions.h
/usr/include/igdgmm/GmmLib/CachePolicy/GmmCachePolicyUndefineConditionals.h
/usr/include/igdgmm/GmmLib/CachePolicy/GmmGen10CachePolicy.h
/usr/include/igdgmm/GmmLib/CachePolicy/GmmGen11CachePolicy.h
/usr/include/igdgmm/GmmLib/CachePolicy/GmmGen12CachePolicy.h
/usr/include/igdgmm/GmmLib/CachePolicy/GmmGen8CachePolicy.h
/usr/include/igdgmm/GmmLib/CachePolicy/GmmGen9CachePolicy.h
/usr/include/igdgmm/GmmLib/Platform/GmmPlatforms.h
/usr/include/igdgmm/GmmLib/Texture/GmmTexture.h
/usr/include/igdgmm/GmmLib/TranslationTable/GmmUmdTranslationTable.h
/usr/include/igdgmm/GmmLib/Utility/CpuSwizzleBlt/CpuSwizzleBlt.c
/usr/include/igdgmm/GmmLib/Utility/CpuSwizzleBlt/assert.h
/usr/include/igdgmm/GmmLib/Utility/GmmLog/GmmLog.h
/usr/include/igdgmm/GmmLib/Utility/GmmUtility.h
/usr/include/igdgmm/GmmLib/inc/External/Common/CachePolicy/GmmCachePolicyGen10.h
/usr/include/igdgmm/GmmLib/inc/External/Common/CachePolicy/GmmCachePolicyGen11.h
/usr/include/igdgmm/GmmLib/inc/External/Common/CachePolicy/GmmCachePolicyGen12.h
/usr/include/igdgmm/GmmLib/inc/External/Common/CachePolicy/GmmCachePolicyGen8.h
/usr/include/igdgmm/GmmLib/inc/External/Common/CachePolicy/GmmCachePolicyGen9.h
/usr/include/igdgmm/GmmLib/inc/External/Common/GmmCachePolicy.h
/usr/include/igdgmm/GmmLib/inc/External/Common/GmmCachePolicyCommon.h
/usr/include/igdgmm/GmmLib/inc/External/Common/GmmCachePolicyExt.h
/usr/include/igdgmm/GmmLib/inc/External/Common/GmmClientContext.h
/usr/include/igdgmm/GmmLib/inc/External/Common/GmmCommonExt.h
/usr/include/igdgmm/GmmLib/inc/External/Common/GmmConst.h
/usr/include/igdgmm/GmmLib/inc/External/Common/GmmDebug.h
/usr/include/igdgmm/GmmLib/inc/External/Common/GmmFormatTable.h
/usr/include/igdgmm/GmmLib/inc/External/Common/GmmHw.h
/usr/include/igdgmm/GmmLib/inc/External/Common/GmmInfo.h
/usr/include/igdgmm/GmmLib/inc/External/Common/GmmInfoExt.h
/usr/include/igdgmm/GmmLib/inc/External/Common/GmmInternal.h
/usr/include/igdgmm/GmmLib/inc/External/Common/GmmLibDll.h
/usr/include/igdgmm/GmmLib/inc/External/Common/GmmLibDllName.h
/usr/include/igdgmm/GmmLib/inc/External/Common/GmmMemAllocator.hpp
/usr/include/igdgmm/GmmLib/inc/External/Common/GmmPageTableMgr.h
/usr/include/igdgmm/GmmLib/inc/External/Common/GmmPlatformExt.h
/usr/include/igdgmm/GmmLib/inc/External/Common/GmmProto.h
/usr/include/igdgmm/GmmLib/inc/External/Common/GmmResourceFlags.h
/usr/include/igdgmm/GmmLib/inc/External/Common/GmmResourceInfo.h
/usr/include/igdgmm/GmmLib/inc/External/Common/GmmResourceInfoCommon.h
/usr/include/igdgmm/GmmLib/inc/External/Common/GmmResourceInfoExt.h
/usr/include/igdgmm/GmmLib/inc/External/Common/GmmTextureExt.h
/usr/include/igdgmm/GmmLib/inc/External/Common/GmmUtil.h
/usr/include/igdgmm/GmmLib/inc/External/Linux/GmmResourceInfoLin.h
/usr/include/igdgmm/GmmLib/inc/External/Linux/GmmResourceInfoLinExt.h
/usr/include/igdgmm/GmmLib/inc/GmmLib.h
/usr/include/igdgmm/igdgmm.h
/usr/include/igdgmm/inc/common/gfxmacro.h
/usr/include/igdgmm/inc/common/gfxplatform.h
/usr/include/igdgmm/inc/common/gtsysinfo.h
/usr/include/igdgmm/inc/common/igfxfmid.h
/usr/include/igdgmm/inc/common/sku_wa.h
/usr/include/igdgmm/inc/portable_compiler.h
/usr/include/igdgmm/inc/umKmInc/UmKmDmaPerfTimer.h
/usr/include/igdgmm/inc/umKmInc/UmKmEnum.h
/usr/include/igdgmm/inc/umKmInc/sharedata.h
/usr/include/igdgmm/util/g_gfxDebug.h
/usr/include/igdgmm/util/gfxDebug.h
/usr/lib64/libigdgmm.so
/usr/lib64/pkgconfig/igdgmm.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libigdgmm.so.12
/usr/lib64/libigdgmm.so.12.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/intel-gmmlib/8b0e9f012620e45a7426bb39ecc64a0cd2f876b1
