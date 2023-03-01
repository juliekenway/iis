from src.serve.server import app


def test_index():
    request_body = {
        "CE Ljubljanska": 1,
        "CE bolnica": 0,
        "Hrastnik": 0,
        "Iskrba": 0,
        "Koper": 0,
        "Kranj": 0,
        "Krvavec": 0,
        "LJ Bežigrad": 0,
        "LJ Celovška": 0,
        "LJ Vič": 0,
        "MB Titova": 0,
        "MB Vrbanski": 0,
        "MS Cankarjeva": 0,
        "MS Rakičan": 0,
        "NG Grčna": 0,
        "Novo mesto": 0,
        "Otlica": 0,
        "Ptuj": 0,
        "Rečica v I.Bistrici": 0,
        "Trbovlje": 0,
        "Zagorje": 0,
        "benzen": 1.0405953021337635,        
        "co": 0.41126802884615377,        
        "ge_dolzina": 15.251062,        
        "ge_sirina": 46.235962,        
        "nadm_visina": 240,        
        "no2": 21.755218047783995,        
        "o3": 54.1503008255212,        
        "pm2.5": 31.185600847009,
        "so2": 2.176576196008026
    }
    response = app.test_client().post('/air/predict/', json=request_body)
    assert response.status_code == 200