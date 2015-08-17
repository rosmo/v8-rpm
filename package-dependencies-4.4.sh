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

version=4.4.63.31

# Match dependency versions from https://github.com/v8/v8-git-mirror/blob/${version}/DEPS
# eg. https://github.com/v8/v8-git-mirror/blob/4.2.77/DEPS

download_dependency "external/gyp.git" "0bb67471bca068996e15b56738fa4824dfa19de0" "build/gyp" "v8-${version}-gyp.tar.gz"

download_dependency "chromium/deps/icu.git" "f8c0e585b0a046d83d72b5d37356cb50d5b2031a" "third_party/icu" "v8-${version}-icu.tar.gz"

download_dependency "chromium/buildtools.git" "b0ede9c89f9d5fbe5387d961ad4c0ec665b6c821" "buildtools" "v8-${version}-buildtools.tar.gz"

download_dependency "external/googletest.git" "be1868139ffe0ccd0e8e3b37292b84c821d9c8ad" "testing/gtest" "v8-${version}-googletest.tar.gz"

download_dependency "external/googlemock.git" "29763965ab52f24565299976b936d1265cb6a271" "testing/gmock" "v8-${version}-googlemock.tar.gz"

download_dependency "chromium/src/tools/clang.git" "5bab78c6ced45a71a8e095a09697ca80492e57e1" "tools/clang" "v8-${version}-clang.tar.gz"


