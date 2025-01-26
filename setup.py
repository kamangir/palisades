from palisades import NAME, VERSION, DESCRIPTION, REPO_NAME
from blueness.pypi import setup

setup(
    filename=__file__,
    repo_name=REPO_NAME,
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    packages=[
        NAME,
        f"{NAME}.analytics",
        f"{NAME}.buildings",
        f"{NAME}.geo",
        f"{NAME}.help",
        f"{NAME}.semseg",
        f"{NAME}.workflow",
    ],
    include_package_data=True,
    package_data={
        NAME: [
            "config.env",
            "sample.env",
            ".abcli/**/*.sh",
            "*.md",
        ],
    },
)
