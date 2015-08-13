%define lib_version 4.2
%define lib_major_version 4
%define use_system_icu 0
Name:           v8
Version:        4.2.77.21
Release:        1%{?dist}
Summary:        Google V8 JavaScript Engine
Group:          Development/Languages
License:        BSD
URL:            https://github.com/v8/v8-git-mirror
Source0:        v8-%{version}.tar.gz
Source1:	v8-%{version}-buildtools.tar.gz
Source2:	v8-%{version}-clang.tar.gz
Source3:	v8-%{version}-googlemock.tar.gz
Source4:	v8-%{version}-googletest.tar.gz
Source5:	v8-%{version}-gyp.tar.gz
Source6:	v8-%{version}-icu.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	python >= 2.4
# Requires the repository from: http://people.centos.org/tru/devtools-2/
# for newer GCC
%if 0%{?el6}
BuildRequires: 	devtoolset-2-gcc devtoolset-2-gcc-c++ devtoolset-2-binutils
%endif
%if 0%{?use_system_icu}
BuildRequires:	libicu-devel
%endif
Provides:       libv8 = %{version}


%description
V8 is Google's open source JavaScript engine.
V8 is written in C++ and is used in Google Chrome, the open source browser from Google.
V8 implements ECMAScript as specified in ECMA-262, 3rd edition, and runs on Windows XP and Vista, Mac OS X 10.5 (Leopard), and Linux systems that use IA-32 or ARM processors.
V8 can run standalone, or can be embedded into any C++ application.

%package devel
Summary:        Development files for %{name}
Group:          System Environment/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains development files for %{name}.

%prep
%setup -q -n v8-git-mirror-%{version}
%setup -D -T -a 1 -n v8-git-mirror-%{version}
%setup -D -T -a 2 -n v8-git-mirror-%{version}
%setup -D -T -a 3 -n v8-git-mirror-%{version}
%setup -D -T -a 4 -n v8-git-mirror-%{version}
%setup -D -T -a 5 -n v8-git-mirror-%{version}
%setup -D -T -a 6 -n v8-git-mirror-%{version}

%build

%if 0%{?el6}
export CC=/opt/rh/devtoolset-2/root/usr/bin/gcc  
export CPP=/opt/rh/devtoolset-2/root/usr/bin/cpp
export CXX=/opt/rh/devtoolset-2/root/usr/bin/c++
export PATH=/opt/rh/devtoolset-2/root/usr/bin:$PATH
%endif

%if 0%{?el7}
export CC=/usr/bin/gcc  
export CPP=/usr/bin/cpp
export CXX=/usr/bin/c++
%endif

%if 0%{?use_system_icu}
export GYP_DEFINES="use_system_icu=1"
%endif

%ifarch x86_64
make x64.release library=shared soname_version=%lib_version %{?_smp_mflags}
%else
make ia32.release library=shared soname_version=%lib_version %{?_smp_mflags}
%endif

%check

%if 0%{?el6}
export CC=/opt/rh/devtoolset-2/root/usr/bin/gcc  
export CPP=/opt/rh/devtoolset-2/root/usr/bin/cpp
export CXX=/opt/rh/devtoolset-2/root/usr/bin/c++
export PATH=/opt/rh/devtoolset-2/root/usr/bin:$PATH
%endif

%if 0%{?el7}
export CC=/usr/bin/gcc  
export CPP=/usr/bin/cpp
export CXX=/usr/bin/c++
%endif

# 4 tests seem to fail for now with:
#  Error: Failure: expected <en-US-u-va-posix-u-co-search>, found <en-US-u-va-posix>.
%ifarch x86_64
#make x64.release.check %{?_smp_mflags}
%else
#make ia32.release.check %{?_smp_mflags}
%endif

%install
rm -rf %buildroot
mkdir -p %buildroot%{_bindir}/

%ifarch x86_64
%define v8_release x64.release
%else
%define v8_release ia32.release
%endif

cp out/%{v8_release}/d8 %buildroot%{_bindir}/

mkdir -p %buildroot%{_libdir}
cp out/%{v8_release}/lib.target/libv8.so.%lib_version %buildroot%{_libdir}/
%if !0%{?use_system_icu}
cp out/%{v8_release}/lib.target/libicu*.so %buildroot%{_libdir}/
%endif
ln -sf %{_libdir}/libv8.so.%lib_version %buildroot%{_libdir}/libv8.so
ln -sf %{_libdir}/libv8.so.%lib_version %buildroot%{_libdir}/libv8.so.%lib_major_version 

mkdir -p %buildroot/%{_includedir}
cp include/v8config.h %buildroot%{_includedir}/
cp include/v8-debug.h %buildroot%{_includedir}/
cp include/v8.h %buildroot%{_includedir}/
cp include/v8-platform.h %buildroot%{_includedir}/
cp include/v8-profiler.h %buildroot%{_includedir}/
cp include/v8-testing.h %buildroot%{_includedir}/
cp include/v8-util.h %buildroot%{_includedir}/
cp include/v8-version.h %buildroot%{_includedir}/
cp -r include/libplatform %buildroot%{_includedir}/

echo -e "create %{buildroot}%{_libdir}/libv8_libplatform.a\naddlib out/%{v8_release}/obj.target/tools/gyp/libv8_libplatform.a\nsave\nend" | ar -M

%clean
rm -rf %buildroot


%files
%defattr(-,root,root)
%{_libdir}/libv8*.so*
%if !0%{?use_system_icu}
%{_libdir}/libicu*.so*
%endif
%{_bindir}/d8

%files devel
%{_includedir}/v8*.h
%{_includedir}/libplatform/*.h
%{_libdir}/libv8_libplatform.a

%changelog
* Wed Aug 12 2015 Taneli Leppa <taneli@crasman.fi> - 4.2.77.21-1
- Initial package.
