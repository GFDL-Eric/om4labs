import intake
import argparse
from importlib.resources import files


def parse(cliargs=None):
    """parse the command line arguments"""
    parser = argparse.ArgumentParser(
        description="list observational datasets available"
    )

    parser.add_argument(
        "--platform",
        type=str,
        required=False,
        default="gfdl",
        help="computing platform, default is gfdl",
    )
    cmdLineArgs = parser.parse_args(cliargs)
    return cmdLineArgs


def run(dictArgs):
    cat_platform = "catalogs/obs_catalog_" + dictArgs["platform"] + ".yml"
    mysource = files("om4labs").joinpath(cat_platform)
    if mysource.is_file():
        cat = intake.open_catalog(mysource)
        return cat
    else:
        print("Platform not available")


def parse_and_run(cliargs=None):
    cmdLineArgs = parse(cliargs)
    dictArgs = vars(cmdLineArgs)
    catobs = run(dictArgs)
    if catobs is not None:
        for obs in list(catobs):
            print(f"{obs}: {catobs[obs].description}")


if __name__ == "__main__":
    parse_and_run()
