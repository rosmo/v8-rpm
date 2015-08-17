#!/bin/sh

cwd=$(pwd)

function download_dependency {
    git_source="https://chromium.googlesource.com/${1}"
    temp_dir=$(mktemp -d)

    git clone $git_source $temp_dir

    cd $temp_dir
    git archive --prefix="${3}/" "${2}" | gzip -c - > "$cwd/sources/${4}"
    rm -rf *
    echo $cwd
    cd $cwd
}

version=4.5.103.22

# Match dependency versions from https://github.com/v8/v8-git-mirror/blob/${version}/DEPS
# eg. https://github.com/v8/v8-git-mirror/blob/4.2.77/DEPS

download_dependency "external/gyp.git" "5122240c5e5c4d8da12c543d82b03d6089eb77c5" "build/gyp" "v8-${version}-gyp.tar.gz"

download_dependency "chromium/deps/icu.git" "c81a1a3989c3b66fa323e9a6ee7418d7c08297af" "third_party/icu" "v8-${version}-icu.tar.gz"

download_dependency "chromium/buildtools.git" "ecc8e253abac3b6186a97573871a084f4c0ca3ae" "buildtools" "v8-${version}-buildtools.tar.gz"

download_dependency "external/googletest.git" "23574bf2333f834ff665f894c97bef8a5b33a0a9" "testing/gtest" "v8-${version}-googletest.tar.gz"

download_dependency "external/googlemock.git" "29763965ab52f24565299976b936d1265cb6a271" "testing/gmock" "v8-${version}-googlemock.tar.gz"

download_dependency "chromium/src/tools/clang.git" "73ec8804ed395b0886d6edf82a9f33583f4a7902" "tools/clang" "v8-${version}-clang.tar.gz"


