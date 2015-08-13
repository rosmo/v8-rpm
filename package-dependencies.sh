#!/bin/sh

cwd=$(pwd)

function download_dependency {
    git_source="https://chromium.googlesource.com/${1}"
    temp_dir=$(mktemp -d)

    git clone $git_source $temp_dir

    cd $temp_dir
    git archive --prefix="${3}/" "${2}" | gzip -c - > "$cwd/${4}"
    rm -rf *
    cd $cwd
}

version=4.2.77.21

# Match dependency versions from https://github.com/v8/v8-git-mirror/blob/${version}/DEPS
# eg. https://github.com/v8/v8-git-mirror/blob/4.2.77/DEPS

download_dependency "external/gyp.git" "34640080d08ab2a37665512e52142947def3056d" "build/gyp" "v8-${version}-gyp.tar.gz"

download_dependency "chromium/deps/icu.git" "4e3266f32c62d30a3f9e2232a753c60129d1e670" "third_party/icu" "v8-${version}-icu.tar.gz"

download_dependency "chromium/buildtools.git" "5c5e924788fe40f7d6e0a3841ac572de2475e689" "buildtools" "v8-${version}-buildtools.tar.gz"

download_dependency "external/googletest.git" "be1868139ffe0ccd0e8e3b37292b84c821d9c8ad" "testing/gtest" "v8-${version}-googletest.tar.gz"

download_dependency "external/googlemock.git" "29763965ab52f24565299976b936d1265cb6a271" "testing/gmock" "v8-${version}-googlemock.tar.gz"

download_dependency "chromium/src/tools/clang.git" "f6daa55d03995e82201a3278203e7c0421a59546" "tools/clang" "v8-${version}-clang.tar.gz"


