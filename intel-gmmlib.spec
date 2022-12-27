#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : intel-gmmlib
Version  : 22.3.2
Release  : 42
URL      : https://github.com/intel/gmmlib/archive/intel-gmmlib-22.3.2/gmmlib-22.3.2.tar.gz
Source0  : https://github.com/intel/gmmlib/archive/intel-gmmlib-22.3.2/gmmlib-22.3.2.tar.gz
Summary  : Intel(R) Graphics Memory Management Library
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: intel-gmmlib-lib = %{version}-%{release}
Requires: intel-gmmlib-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : llvm-dev

%description
Intel(R) Graphics Memory Management Library
*******************************************

%package dev
Summary: dev components for the intel-gmmlib package.
Group: Development
Requires: intel-gmmlib-lib = %{version}-%{release}
Provides: intel-gmmlib-devel = %{version}-%{release}
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
%setup -q -n gmmlib-intel-gmmlib-22.3.2
cd %{_builddir}/gmmlib-intel-gmmlib-22.3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672177714
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1672177714
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/intel-gmmlib
cp %{_builddir}/gmmlib-intel-gmmlib-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/intel-gmmlib/d20436278232615063a7e8362183ec1b307addc9
cp %{_builddir}/gmmlib-intel-gmmlib-%{version}/third_party/sse2neon/LICENSE %{buildroot}/usr/share/package-licenses/intel-gmmlib/218fc8c15534e8840cbff5801582c450c97869ab
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/include/igdgmm/GmmLib/CachePolicy/GmmGen12dGPUCachePolicy.h
/usr/include/igdgmm/GmmLib/CachePolicy/GmmGen8CachePolicy.h
/usr/include/igdgmm/GmmLib/CachePolicy/GmmGen9CachePolicy.h
/usr/include/igdgmm/GmmLib/CachePolicy/GmmXe_LPGCachePolicy.h
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
/usr/include/igdgmm/GmmLib/inc/External/Common/CachePolicy/GmmCachePolicyGen12dGPU.h
/usr/include/igdgmm/GmmLib/inc/External/Common/CachePolicy/GmmCachePolicyGen8.h
/usr/include/igdgmm/GmmLib/inc/External/Common/CachePolicy/GmmCachePolicyGen9.h
/usr/include/igdgmm/GmmLib/inc/External/Common/CachePolicy/GmmCachePolicyXe_LPG.h
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
/usr/lib64/glibc-hwcaps/x86-64-v3/libigdgmm.so
/usr/lib64/libigdgmm.so
/usr/lib64/pkgconfig/igdgmm.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libigdgmm.so.12
/usr/lib64/glibc-hwcaps/x86-64-v3/libigdgmm.so.12.3.0
/usr/lib64/libigdgmm.so.12
/usr/lib64/libigdgmm.so.12.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/intel-gmmlib/218fc8c15534e8840cbff5801582c450c97869ab
/usr/share/package-licenses/intel-gmmlib/d20436278232615063a7e8362183ec1b307addc9
