## Last Update
- Finished
- got app to work in the contrainer and tested with a prediction

## Next Steps





## Notes

scikit learn models return numpy data types
FastAPI/Json can only handle python native types: str, int, float
so we you are passing the model results to fastapi to reutnr you need to convert them first


use this command to send curl request to tests
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d '{"SepalLen": 5.1, "SepalWid": 3.5, "PetalLen": 1.4, "PetalWid": 0.2}'

curl -X POST http://127.0.0.1:80/predict -H "Content-Type: application/json" -d '{"SepalLen": 5.1, "SepalWid": 3.5, "PetalLen": 1.4, "PetalWid": 0.2}'
