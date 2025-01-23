from abcli.tests.test_env import test_abcli_env
from blue_objects.tests.test_env import test_blue_objects_env

from palisades import env


def test_required_env():
    test_abcli_env()
    test_blue_objects_env()


def test_palisades_env():
    assert env.PALISADES_QUERY_OBJECT_PALISADES_MAXAR
    assert env.PALISADES_QUERY_OBJECT_PALISADES_MAXAR_TEST

    assert env.PALISADES_DEFAULT_FIRE_MODEL

    assert env.PALISADES_QGIS_TEMPLATE_PREDICT

    assert env.PALISADES_TEST_PREDICTION_OBJECT
