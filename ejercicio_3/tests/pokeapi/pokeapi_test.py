import pytest
import requests

from helpers.ddt import DDTHelper

DATA_PATH = "data/poke_api/data.json"
ddt = DDTHelper(DATA_PATH)
data_tc1 = ddt.get_by_testid("pokeapi_case1")
data_tc2 = ddt.get_by_testid("pokeapi_case2")
data_tc3 = ddt.get_by_testid("pokeapi_case3")


@pytest.fixture(scope="session")
def api_client():
    session = requests.Session()
    yield session
    session.close()


@pytest.mark.pokeapi
@pytest.mark.pokeapi_tc1
@pytest.mark.parametrize("case", data_tc1)
def test_pokeapi_berry1(case, api_client):
    url_base = case.json_data["url_base"]
    resource = case.json_data["resource"]
    expectations = case.json_data["expectations"]

    url = f"{url_base}/{resource}"
    response = requests.get(url)

    assert response.status_code == 200

    data_response = response.json()

    assert data_response["size"] == expectations["size"]
    assert data_response["soil_dryness"] == expectations["soil_dryness"]
    assert data_response["firmness"]["name"] == expectations["firmness_name"]


@pytest.mark.pokeapi
@pytest.mark.pokeapi_tc2
@pytest.mark.parametrize("case", data_tc2)
def test_pokeapi_berry2(case, api_client):
    url_base = case.json_data["url_base"]
    resource = case.json_data["resource"]
    expectations = case.json_data["expectations"]

    url = f"{url_base}/{resource}"
    response = requests.get(url)

    assert response.status_code == 200

    data_response = response.json()

    assert data_response["size"] > expectations["size"]
    assert data_response["soil_dryness"] == expectations["soil_dryness"]
    assert data_response["firmness"]["name"] == expectations["firmness_name"]


@pytest.mark.pokeapi
@pytest.mark.pokeapi_tc3
@pytest.mark.parametrize("case", data_tc3)
def test_pokeapi_pikachu(case, api_client):
    url_base = case.json_data["url_base"]
    resource = case.json_data["resource"]
    expectations = case.json_data["expectations"]

    url = f"{url_base}/{resource}"
    response = requests.get(url)

    assert response.status_code == 200

    data_response = response.json()

    assert data_response["base_experience"] < expectations["base_experience_max"]
    assert data_response["base_experience"] > expectations["base_experience_min"]
    assert any(t["type"]["name"] == "electric" for t in data_response["types"])
