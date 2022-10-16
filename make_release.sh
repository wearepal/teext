#!/bin/bash

# fail on error
set -e

# confirm the supplied version bump is valid
version_bump=$1

case $version_bump in
  "patch" | "minor" | "major" | "rc" | "dev" | "alpha" | "beta" | "release" | "post")
    echo "valid version bump: $version_bump"
    ;;
  *)
    echo "invalid version bump: \"$version_bump\""
    echo "Usage:"
    echo ""
    echo "    bash make_release.sh <version bump>"
    echo ""
    echo "List of valid version bumps: patch, minor, major, prepatch, preminor, premajor, prerelease"
    exit 1
    ;;
esac

if [ -n "$(git status --untracked-files=no --porcelain)" ]; then
  echo "The repository has uncommitted changes."
  echo "This will lead to problems with git checkout."
  exit 2
fi

if [ $(git symbolic-ref --short -q HEAD) != "main" ]; then
  echo "not on main branch"
  exit 3
fi

echo ""
echo "######################################"
echo "# ensure main branch is up-to-date  #"
echo "######################################"
git pull

echo ""
echo "######################################"
echo "#       checkout release branch      #"
echo "######################################"
git checkout release

echo ""
echo "#######################################"
echo "# ensure release branch is up-to-date #"
echo "#######################################"
git pull

echo ""
echo "#######################################"
echo "#   merge main into release branch  #"
echo "#######################################"
git merge --no-ff main --no-edit

bump_build_publish() {
  echo "#######################################"
  echo "#          switching to $1            #"
  echo "#######################################"
  pushd $1

  echo "#######################################"
  echo "#            bump version             #"
  echo "#######################################"
  hatch version $version_bump
  git add teext/__init__.py

  # clean previous build and build
  echo "#######################################"
  echo "#        clean up old builds          #"
  echo "#######################################"
  rm -rf build dist

  echo "#######################################"
  echo "#            do new build             #"
  echo "#######################################"
  # one without mypyc
  HATCH_BUILD_NO_HOOKS=true hatch build
  # one with mypyc
  hatch build

  echo ""
  echo "#######################################"
  echo "#          publish package            #"
  echo "#######################################"
  hatch publish

  popd  # switch back to previous directory
}

# go through all project directories
bump_build_publish "."
# (it's currently only one)

# commit changes
git commit -m "Bump version"

# get the version
new_tag=v$(hatch version)

# create tag and push
echo "#######################################"
echo "#          new tag: $new_tag          #"
echo "#######################################"
git tag $new_tag
git push origin release $new_tag

# clean up
echo "#######################################"
echo "#      go back to main branch         #"
echo "#######################################"
git checkout main

echo "#######################################"
echo "#           create release            #"
echo "#######################################"
gh release create $new_tag --generate-notes
