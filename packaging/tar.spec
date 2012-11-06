#
# Please submit bugfixes or comments via http://bugs.tizen.org/
#

Name:           tar
Version:        1.17
Release:        1
License:        GPL-2.0+
Summary:        A GNU file archiving program
Url:            http://www.gnu.org/software/tar/
Group:          Applications/Archiving
Source0:        ftp://ftp.gnu.org/pub/gnu/tar/tar-%{version}.tar.gz
Source1:        tar.1
Patch0:         tar-1.14-loneZeroWarning.patch
Patch1:         tar-1.15.1-vfatTruncate.patch
Patch2:         tar-1.17-testsuite.patch
Patch3:         tar-1.17-xattrs.patch
Patch4:         tar-1.17-wildcards.patch
Patch5:         tar-1.17-dot_dot_vuln.patch
Patch6:         gcc43.patch
Patch7:         tar-1.17-gcc4.patch
Patch8:         BMC6647-CVE-2010-0624.patch
Patch9:         BMC6661-CVE-2007-4476.patch
BuildRequires:  libacl-devel

%description
The GNU tar program saves many files together in one archive and can
restore individual files (or all of the files) from that archive. Tar
can also be used to add supplemental files to an archive and to update
or list files in the archive. Tar includes multivolume support,
automatic archive compression/decompression, the ability to perform
remote archives, and the ability to perform incremental and full
backups.

If you want to use tar for remote backups, you also need to install
the rmt package.

%prep
%setup -q

# tar-1.14-loneZeroWarning.patch
%patch0 -p1
# tar-1.15.1-vfatTruncate.patch
%patch1 -p1
# tar-1.17-testsuite.patch
%patch2 -p1
# tar-1.17-xattrs.patch
%patch3 -p1
# tar-1.17-wildcards.patch
%patch4 -p1
# tar-1.17-dot_dot_vuln.patch
%patch5 -p1
# gcc43.patch
%patch6 -p1
# tar-1.17-gcc4.patch
%patch7 -p1
# BMC6647-CVE-2010-0624.patch
%patch8 -p1
# BMC6661-CVE-2007-4476.patch
%patch9 -p1

%build

%configure \
    --disable-nls

make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_mandir}/man1
cp -a %{SOURCE1} %{buildroot}%{_mandir}/man1

rm -rf %{buildroot}%{_prefix}/libexec/rmt

%docs_package

%files
%defattr(-,root,root,-)
%{_bindir}/tar


