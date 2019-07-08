[![Build Status](https://travis-ci.org/akretion/import-export.svg?branch=10.0)](https://travis-ci.org/akretion/import-export)
[![Coverage Status](https://coveralls.io/repos/github/akretion/import-export/badge.svg?branch=10.0)](https://coveralls.io/github/akretion/import-export?branch=10.0)
[![Code Climate](https://codeclimate.com/github/akretion/import-export/badges/gpa.svg)](https://codeclimate.com/github/akretion/import-export)


# Akretion Import Export

## Branch management from v10 version

This repository is used by Akretion for sharing R&D module regarding import and export.
Most of module are used in production so you can use it, but be carreful that we can make breaking change between version
When module will be enought generic and stabilized we will propose them to the OCA

# Dev tips

This project use black and pre-commit.
Please install precommit if you want to contribute

```
pipx install pre-commit
```

After cloning just run
```
pre-commit install
```

So the git hook will be installed and every check can be perform automatically
