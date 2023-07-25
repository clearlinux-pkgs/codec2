#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
Name     : codec2
Version  : 1.2.0
Release  : 30
URL      : https://github.com/drowe67/codec2/archive/1.2.0/codec2-1.2.0.tar.gz
Source0  : https://github.com/drowe67/codec2/archive/1.2.0/codec2-1.2.0.tar.gz
Summary  : A speech codec for 2400 bit/s and below
Group    : Development/Tools
License  : LGPL-2.1
Requires: codec2-lib = %{version}-%{release}
Requires: codec2-license = %{version}-%{release}
BuildRequires : LPCNet-dev
BuildRequires : buildreq-cmake
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : octave
BuildRequires : pkgconfig(samplerate)
BuildRequires : pkgconfig(speexdsp)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: fsk_fft_api.patch

%description
An Orthogonal Frequency Division Multiplexed (OFDM) modem designed for digital voice over HF SSB.  Typical configuration for FreeDV 700D is 700 bit/s voice, a rate 0.5 LDPC code, and 1400 bit/s raw data rate over the channel.

%package dev
Summary: dev components for the codec2 package.
Group: Development
Requires: codec2-lib = %{version}-%{release}
Provides: codec2-devel = %{version}-%{release}
Requires: codec2 = %{version}-%{release}

%description dev
dev components for the codec2 package.


%package lib
Summary: lib components for the codec2 package.
Group: Libraries
Requires: codec2-license = %{version}-%{release}

%description lib
lib components for the codec2 package.


%package license
Summary: license components for the codec2 package.
Group: Default

%description license
license components for the codec2 package.


%prep
%setup -q -n codec2-1.2.0
cd %{_builddir}/codec2-1.2.0
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1690298596
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx512
pushd clr-build-avx512
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v4 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86_64-v4 -mprefer-vector-width=512 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v4 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86_64-v4 -mprefer-vector-width=512 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v4 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86_64-v4 -mprefer-vector-width=512 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v4 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86_64-v4 -mprefer-vector-width=512 "
export CFLAGS="$CFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 -mprefer-vector-width=512"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 -mprefer-vector-width=512"
export FFLAGS="$FFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 -mprefer-vector-width=512"
export FCFLAGS="$FCFLAGS -march=x86-64-v4 -m64 "
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :
cd ../clr-build-avx2;
make test || : || :
cd ../clr-build-avx512;
make test || : || :

%install
export SOURCE_DATE_EPOCH=1690298596
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/codec2
cp %{_builddir}/codec2-%{version}/COPYING %{buildroot}/usr/share/package-licenses/codec2/af54222a16839088fb1ffd5da88c1713472babc4 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build-avx512
%make_install_v4  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/codec2/codec2.h
/usr/include/codec2/codec2_cohpsk.h
/usr/include/codec2/codec2_fdmdv.h
/usr/include/codec2/codec2_fifo.h
/usr/include/codec2/codec2_fm.h
/usr/include/codec2/codec2_math.h
/usr/include/codec2/codec2_ofdm.h
/usr/include/codec2/comp.h
/usr/include/codec2/fmfsk.h
/usr/include/codec2/freedv_api.h
/usr/include/codec2/fsk.h
/usr/include/codec2/modem_stats.h
/usr/include/codec2/reliable_text.h
/usr/include/codec2/version.h
/usr/lib64/cmake/codec2/codec2-config-relwithdebinfo.cmake
/usr/lib64/cmake/codec2/codec2-config.cmake
/usr/lib64/libcodec2.so
/usr/lib64/pkgconfig/codec2.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libcodec2.so.1.2
/V4/usr/lib64/libcodec2.so.1.2
/usr/lib64/libcodec2.so.1.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/codec2/af54222a16839088fb1ffd5da88c1713472babc4
