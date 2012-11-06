Name:           tar
Version:        1.26
Release:        0
Summary:        GNU implementation of tar ((t)ape (ar)chiver)
License:        GPL-3.0+
Group:          System/Base
Url:            http://www.gnu.org/software/tar/
Source0:        %{name}-%{version}.tar.bz2
#
Patch3:         tar-wildcards.patch
Patch6:         tar-backup-spec-fix-paths.patch
Patch7:         tar-1.26-remove_O_NONBLOCK.patch
Patch8:         tar-1.26-stdio.in.patch
BuildRequires:  help2man
Recommends:     xz

%description
This package normally also includes the program "rmt", which provides
remote tape drive control. Since there are compatible versions of 'rmt'
in either the 'star' package or the 'dump' package, we didn't put 'rmt'
into this package. If you are planning to use the remote tape features
provided by tar you have to also install the 'dump' or the 'star'
package.

%{?lang_package}

%prep
%setup -q
%patch3 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
%define my_cflags -W -Wall -Wpointer-arith -Wstrict-prototypes -Wformat-security -Wno-unused-parameter
export CFLAGS="%{optflags} %my_cflags"
export RSH="/usr/bin/rsh"
export DEFAULT_ARCHIVE_FORMAT="POSIX"
%configure \
	gl_cv_func_linkat_follow="yes" \
	--disable-silent-rules \
	--disable-nls
make %{?_smp_mflags};

%check
%if !0%{?qemu_user_space_build:1}
# Checks disabled in qemu because of races happening when we emulate
# multi-threaded programs
make check
%endif

%install
%{?make_install} %{!?make_install:make install DESTDIR=%{buildroot}}
install -d -m 755 %{buildroot}/%{_mandir}/man1
help2man ./src/tar --name "The GNU version of the tar archiving utility" -p tar \
        | gzip -c > %{buildroot}/%{_mandir}/man1/tar.1.gz
rm -rf %{buildroot}%{_libexecdir}/rmt
rm -f %{buildroot}%{_infodir}/dir


%docs_package

%files
%endif
%defattr(-, root, root)
%{_bindir}/tar
%doc COPYING
%{_mandir}/man1/tar.1.gz

%changelog
