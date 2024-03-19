from src.add_weather import add_weather
import pytest
from unittest.mock import patch

Sample = {
          'put_item': 2
          }
    
def test_validate_prerequisite1():
   body = {"id": "1", "weather": "hot"}
   res = add_weather.validate_prerequisite(body)
   assert res[0]

def test_validate_prerequisite2():
   body = {"_id": "1", "weather": "hot"}
   res = add_weather.validate_prerequisite(body)
   assert res[1] == "id is missing or id is not in the format"

def test_validate_prerequisite3():
   body = {"id": 1, "weather": "hot"}
   res = add_weather.validate_prerequisite(body)
   assert res[1] == "id is missing or id is not in the format"

def test_validate_prerequisite4():
   body = {"id": "1", "weather": 2}
   res = add_weather.validate_prerequisite(body)
   assert res[1] == "weather is missing or weather is not in the format"

def test_validate_prerequisite5():
   body = {"id": "1", "weather_climate": "hot"}
   res = add_weather.validate_prerequisite(body)
   assert res[1] == "weather is missing or weather is not in the format"

def test_validate_prerequisite6():
   body = {"id": "1", "weather": "hot", "climate": "sunny"}
   res = add_weather.validate_prerequisite(body)
   assert res[1] == "Additional parameters were passed"
   
def test_lambda_handler1():
   event = {'body':{}}
   res = add_weather.lambda_handler(event, '')
   assert res['body'] == 'Request body is absent'

def test_lambda_handler2():
   event = {'body':{"id:1"}}
   res = add_weather.lambda_handler(event, '')
   assert res['body'] == 'Input is not in valid format'

