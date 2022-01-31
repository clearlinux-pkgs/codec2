#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : codec2
Version  : 1.03
Release  : 14
URL      : https://github.com/drowe67/codec2/archive/v1.03/codec2-1.03.tar.gz
Source0  : https://github.com/drowe67/codec2/archive/v1.03/codec2-1.03.tar.gz
Summary  : A speech codec for 2400 bit/s and below
Group    : Development/Tools
License  : LGPL-2.1
Requires: codec2-bin = %{version}-%{release}
Requires: codec2-filemap = %{version}-%{release}
Requires: codec2-lib = %{version}-%{release}
Requires: codec2-license = %{version}-%{release}
BuildRequires : LPCNet-dev
BuildRequires : buildreq-cmake
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : octave
BuildRequires : pkgconfig(samplerate)
BuildRequires : pkgconfig(speexdsp)
Patch1: fsk_fft_api.patch
Patch2: modern-cmake-targets.patch

%description
An Orthogonal Frequency Division Multiplexed (OFDM) modem designed for digital voice over HF SSB.  Typical configuration for FreeDV 700D is 700 bit/s voice, a rate 0.5 LDPC code, and 1400 bit/s raw data rate over the channel.

%package bin
Summary: bin components for the codec2 package.
Group: Binaries
Requires: codec2-license = %{version}-%{release}
Requires: codec2-filemap = %{version}-%{release}

%description bin
bin components for the codec2 package.


%package dev
Summary: dev components for the codec2 package.
Group: Development
Requires: codec2-lib = %{version}-%{release}
Requires: codec2-bin = %{version}-%{release}
Provides: codec2-devel = %{version}-%{release}
Requires: codec2 = %{version}-%{release}

%description dev
dev components for the codec2 package.


%package filemap
Summary: filemap components for the codec2 package.
Group: Default

%description filemap
filemap components for the codec2 package.


%package lib
Summary: lib components for the codec2 package.
Group: Libraries
Requires: codec2-license = %{version}-%{release}
Requires: codec2-filemap = %{version}-%{release}

%description lib
lib components for the codec2 package.


%package license
Summary: license components for the codec2 package.
Group: Default

%description license
license components for the codec2 package.


%prep
%setup -q -n codec2-1.03
cd %{_builddir}/codec2-1.03
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640723540
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fno-lto -march=x86-64-v3 -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fno-lto -march=x86-64-v3 -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fno-lto -march=x86-64-v3 -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fno-lto -march=x86-64-v3 -mtune=skylake "
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
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v4 -fno-lto -march=x86_64-v4 -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v4 -fno-lto -march=x86_64-v4 -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v4 -fno-lto -march=x86_64-v4 -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v4 -fno-lto -march=x86_64-v4 -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 "
export CXXFLAGS="$CXXFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 "
export FFLAGS="$FFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 "
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
export SOURCE_DATE_EPOCH=1640723540
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/codec2
cp %{_builddir}/codec2-1.03/COPYING %{buildroot}/usr/share/package-licenses/codec2/af54222a16839088fb1ffd5da88c1713472babc4
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build-avx512
%make_install_v4  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/c2dec
/usr/bin/c2enc
/usr/bin/fdmdv_demod
/usr/bin/fdmdv_get_test_bits
/usr/bin/fdmdv_mod
/usr/bin/fdmdv_put_test_bits
/usr/bin/fm_demod
/usr/bin/fsk_mod
/usr/bin/insert_errors
/usr/share/clear/optimized-elf/bin*

%files dev
%defattr(-,root,root,-)
/usr/include/codec2/codec2.h
/usr/include/codec2/codec2_cohpsk.h
/usr/include/codec2/codec2_fdmdv.h
/usr/include/codec2/codec2_fifo.h
/usr/include/codec2/codec2_fm.h
/usr/include/codec2/codec2_ofdm.h
/usr/include/codec2/comp.h
/usr/include/codec2/fmfsk.h
/usr/include/codec2/freedv_api.h
/usr/include/codec2/fsk.h
/usr/include/codec2/modem_stats.h
/usr/include/codec2/reliable_text.h
/usr/include/codec2/version.h
/usr/lib64/cmake/codec2/Codec2Config.cmake
/usr/lib64/cmake/codec2/Codec2Targets-relwithdebinfo.cmake
/usr/lib64/cmake/codec2/Codec2Targets.cmake
/usr/lib64/libcodec2.so
/usr/lib64/pkgconfig/codec2.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-codec2

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcodec2.so.1.0
/usr/share/clear/optimized-elf/lib*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/codec2/af54222a16839088fb1ffd5da88c1713472babc4
