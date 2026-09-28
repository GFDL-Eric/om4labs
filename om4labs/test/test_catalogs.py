import intake
from importlib.resources import files


def test_catalogs_are_present():
    f = files("om4labs").joinpath("catalogs/obs_catalog_gfdl.yml")
    cat = intake.open_catalog(f)
    assert isinstance(cat, intake.catalog.local.YAMLFileCatalog)
