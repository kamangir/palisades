# 🌀 blue-plugin

🌀 `blue-plugin` is a git template for an 🪄 [`awesome-bash-cli`](https://github.com/kamangir/awesome-bash-cli) (`abcli`) plugin, to build [things like these](https://github.com/kamangir?tab=repositories), that out-of-the-box support,

- a [github repo](https://github.com/) with [actions](https://github.com/features/actions).
- [pylint](https://pypi.org/project/pylint/).
- [pytest](https://docs.pytest.org/).
- a pip-installable python + bash package published to [pypi](https://pypi.org/).
- a bash [command interface](./blue_plugin/.abcli/blue_plugin.sh).
- [bash testing](./.github/workflows/bashtest.yml).
- secret management through [ssm](https://docs.aws.amazon.com/secretsmanager/).
- in-repo [compiled](./blue_plugin/README.py) READMEs based on [templates](./template.md).
- [object management](https://github.com/kamangir/blue-objects) on [Amazon S3](https://aws.amazon.com/s3/) with metadata tracking by [MLflow](https://mlflow.org/).
- [workflow management](https://github.com/kamangir/notebooks-and-scripts/tree/main/blueflow/workflow) on [AWS Batch](https://aws.amazon.com/batch/).
- [docker](https://github.com/kamangir/notebooks-and-scripts/blob/main/blueflow/.abcli/docker.sh) and [SageMaker](https://github.com/kamangir/notebooks-and-scripts/blob/main/blueflow/.abcli/sagemaker.sh) enabled.

## installation

```bash
pip install blue-plugin
```

## creating a blue-plugin

1️⃣ create a new repository from [this template](https://github.com/kamangir/blue-plugin),

2️⃣ complete `<repo-name>` and `<plugin-name>` and run,

```bash
@git clone <repo-name> cd

@plugins transform <repo-name>

@init
<plugin-name> help
```

## features

|   |   |   |
| --- | --- | --- |
| 🌀[`feature 1`](#) [![image](https://github.com/kamangir/assets/raw/main/blue-plugin/marquee.png?raw=true)](#) description of feature 1 ... | 🌀[`feature 2`](#) [![image](https://github.com/kamangir/assets/raw/main/blue-plugin/marquee.png?raw=true)](#) description of feature 2 ... | 🌀[`feature 3`](#) [![image](https://github.com/kamangir/assets/raw/main/blue-plugin/marquee.png?raw=true)](#) description of feature 3 ... |

---


[![pylint](https://github.com/kamangir/blue-plugin/actions/workflows/pylint.yml/badge.svg)](https://github.com/kamangir/blue-plugin/actions/workflows/pylint.yml) [![pytest](https://github.com/kamangir/blue-plugin/actions/workflows/pytest.yml/badge.svg)](https://github.com/kamangir/blue-plugin/actions/workflows/pytest.yml) [![bashtest](https://github.com/kamangir/blue-plugin/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/blue-plugin/actions/workflows/bashtest.yml) [![PyPI version](https://img.shields.io/pypi/v/blue-plugin.svg)](https://pypi.org/project/blue-plugin/) [![PyPI - Downloads](https://img.shields.io/pypi/dd/blue-plugin)](https://pypistats.org/packages/blue-plugin)

built by 🌀 [`blue_options-4.192.1`](https://github.com/kamangir/awesome-bash-cli), based on 🌀 [`blue_plugin-3.208.1`](https://github.com/kamangir/blue-plugin).
