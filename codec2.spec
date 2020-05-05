#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : codec2
Version  : 0.9.2
Release  : 5
URL      : https://github.com/drowe67/codec2/archive/v0.9.2/codec2-0.9.2.tar.gz
Source0  : https://github.com/drowe67/codec2/archive/v0.9.2/codec2-0.9.2.tar.gz
Summary  : A speech codec for 2400 bit/s and below
Group    : Development/Tools
License  : LGPL-2.1
Requires: codec2-bin = %{version}-%{release}
Requires: codec2-lib = %{version}-%{release}
Requires: codec2-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : pkgconfig(samplerate)
BuildRequires : pkgconfig(speexdsp)
Patch1: fsk_fft_api.patch
Patch2: modern-cmake-targets.patch

%description
David Rowe
Created Mar 2018
Introduction
------------
An Orthogonal Frequency Division Multiplexed (OFDM) modem designed for
digital voice over HF SSB.  Typical configuration for FreeDV 700D is
700 bit/s voice, a rate 0.5 LDPC code, and 1400 bit/s raw data rate
over the channel.

%package bin
Summary: bin components for the codec2 package.
Group: Binaries
Requires: codec2-license = %{version}-%{release}

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
%setup -q -n codec2-0.9.2
cd %{_builddir}/codec2-0.9.2
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588718134
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :

%install
export SOURCE_DATE_EPOCH=1588718134
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/codec2
cp %{_builddir}/codec2-0.9.2/COPYING %{buildroot}/usr/share/package-licenses/codec2/af54222a16839088fb1ffd5da88c1713472babc4
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/c2dec
/usr/bin/c2enc
/usr/bin/drs232
/usr/bin/drs232_ldpc
/usr/bin/fdmdv_demod
/usr/bin/fdmdv_get_test_bits
/usr/bin/fdmdv_mod
/usr/bin/fdmdv_put_test_bits
/usr/bin/fm_demod
/usr/bin/fsk_mod
/usr/bin/insert_errors

%files dev
%defattr(-,root,root,-)
/usr/include/codec2/codec2.h
/usr/include/codec2/codec2_cohpsk.h
/usr/include/codec2/codec2_fdmdv.h
/usr/include/codec2/codec2_fifo.h
/usr/include/codec2/codec2_fm.h
/usr/include/codec2/codec2_ofdm.h
/usr/include/codec2/comp.h
/usr/include/codec2/comp_prim.h
/usr/include/codec2/filter.h
/usr/include/codec2/fmfsk.h
/usr/include/codec2/freedv_api.h
/usr/include/codec2/freedv_api_internal.h
/usr/include/codec2/fsk.h
/usr/include/codec2/golay23.h
/usr/include/codec2/horus_api.h
/usr/include/codec2/kiss_fft.h
/usr/include/codec2/modem_stats.h
/usr/include/codec2/varicode.h
/usr/include/codec2/version.h
/usr/lib64/cmake/codec2/Codec2Config.cmake
/usr/lib64/cmake/codec2/Codec2Targets-relwithdebinfo.cmake
/usr/lib64/cmake/codec2/Codec2Targets.cmake
/usr/lib64/cmake/codec2/codec2-config-relwithdebinfo.cmake
/usr/lib64/cmake/codec2/codec2-config.cmake
/usr/lib64/libcodec2.so
/usr/lib64/pkgconfig/codec2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcodec2.so.0.9

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/codec2/af54222a16839088fb1ffd5da88c1713472babc4
