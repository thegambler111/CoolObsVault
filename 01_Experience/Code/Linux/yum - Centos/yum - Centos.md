# View list of installed packages
- [Source](https://linuxhint.com/uninstall_yum_package/)

```shell
yum list installed
```

# Remove package
```shell
yum remove <package_name>
```

# Install package with a specific version

## View all available version of a package
```shell
yum --showduplicates list <package_name> | expand
```

## Install a specific version
```shell
yum install <package_name>-<package_version>
```

#
---
- Status: #done
- Tags:
- References:
	- Source
- Related:
