# V8 4.x RPM for RHEL 6 and 7

This is a RPM spec file for Red Hat Enterprise Linux 6 and 7 (el6 and el7),
CentOS 6 and 7 and other compatible distributions. It does not use gclient
sync or any git shenanigans and downloads the dependencies using a simple
script and git-archive.

## Steps:

Download a release from Github:

```
wget -Ov8-4.2.77.21.tar.gz https://github.com/v8/v8-git-mirror/archive/4.2.77.21.tar.gz
```

Download and package dependencies:

```
sh package-dependencies.sh
```

Build source RPM:

```
rpmbuild --bs --nodeps --define "_sourcedir `pwd`" v8-4.2.spec
```

Use mock or rpmbuild to build yourself a binary RPM.

** You will need the newer GCC repo from: http://people.centos.org/tru/devtools-2/ **
(This goes into your mock configuration or you'll need to install the
build requires package from there)

If you need to update to a newer release, first download the release and then
unpack it. Discover dependencies by looking at the DEPS file(s) and update
package-dependencies.sh with the new commit IDs and/or dependencies.