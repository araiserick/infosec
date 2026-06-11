Запрос от client1 > server1 (запрос)

PUT /users HTTP/1.1
Host: localhost:9001
User-Agent: Go-http-client/1.1
Content-Length: 26
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip

login=user&password=111111HTTP/1.1 200 OK
Content-Type: application/json
Date: Thu, 11 Jun 2026 10:59:10 GMT
Content-Length: 496

{"token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIsImxvZ2luIjoidXNlciIsInJvbGVzIjpbIlVTRVIiXSwiaWF0IjoxNzgxMTc1NTUwLCJleHAiOjE3ODExNzkxNTB9.gTLLN8-5yAkCx46nVdoIcTaGnqmFptbZnpBXK4agTVakRtjooy9AW-DukgDiH2Los0Cz8YwG0lgCH1NjabylbQ5H7PiSqI0xz-mKSFeA3rRLCs9V2rKRZAiKh4J4tavuJFxlambmOkDqBJE9D46QkPnVF7Qt70ESk_oKped4j5cSJnUmWgGIgNEeVVUbgwYrwDn8oIhuFpNRTLBaO-He60x_4G5KDltswtb513L_KNgvC7Ah02qJODtOWyqojgz2obd4ndBzK8K8mtmACoV1Dh4rUJb1cMEfk_157hmcHhiR2aMPuSeSVcZFbwdBnQy0Z4fK55VI5tqaoSQilvQODw"}

server1 > client1 (получили токен)

PUT /users HTTP/1.1
Host: localhost:9001
User-Agent: Go-http-client/1.1
Content-Length: 26
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip

login=user&password=111111HTTP/1.1 200 OK
Content-Type: application/json
Date: Thu, 11 Jun 2026 10:59:10 GMT
Content-Length: 496

{"token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIsImxvZ2luIjoidXNlciIsInJvbGVzIjpbIlVTRVIiXSwiaWF0IjoxNzgxMTc1NTUwLCJleHAiOjE3ODExNzkxNTB9.gTLLN8-5yAkCx46nVdoIcTaGnqmFptbZnpBXK4agTVakRtjooy9AW-DukgDiH2Los0Cz8YwG0lgCH1NjabylbQ5H7PiSqI0xz-mKSFeA3rRLCs9V2rKRZAiKh4J4tavuJFxlambmOkDqBJE9D46QkPnVF7Qt70ESk_oKped4j5cSJnUmWgGIgNEeVVUbgwYrwDn8oIhuFpNRTLBaO-He60x_4G5KDltswtb513L_KNgvC7Ah02qJODtOWyqojgz2obd4ndBzK8K8mtmACoV1Dh4rUJb1cMEfk_157hmcHhiR2aMPuSeSVcZFbwdBnQy0Z4fK55VI5tqaoSQilvQODw"}

client1 > server2 (запрос)

GET /api/transactions HTTP/1.1
Host: localhost:9002
User-Agent: Go-http-client/1.1
Authorization: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIsImxvZ2luIjoidXNlciIsInJvbGVzIjpbIlVTRVIiXSwiaWF0IjoxNzgxMTc1NTUwLCJleHAiOjE3ODExNzkxNTB9.gTLLN8-5yAkCx46nVdoIcTaGnqmFptbZnpBXK4agTVakRtjooy9AW-DukgDiH2Los0Cz8YwG0lgCH1NjabylbQ5H7PiSqI0xz-mKSFeA3rRLCs9V2rKRZAiKh4J4tavuJFxlambmOkDqBJE9D46QkPnVF7Qt70ESk_oKped4j5cSJnUmWgGIgNEeVVUbgwYrwDn8oIhuFpNRTLBaO-He60x_4G5KDltswtb513L_KNgvC7Ah02qJODtOWyqojgz2obd4ndBzK8K8mtmACoV1Dh4rUJb1cMEfk_157hmcHhiR2aMPuSeSVcZFbwdBnQy0Z4fK55VI5tqaoSQilvQODw
Accept-Encoding: gzip

HTTP/1.1 200 OK
Content-Type: application/json
Date: Thu, 11 Jun 2026 10:59:10 GMT
Content-Length: 291

{"transactions":[{"id":1,"userId":2,"category":"auto","amount":1000000,"created":1781174529},{"id":2,"userId":2,"category":"auto","amount":100000,"created":1781174529},{"id":3,"userId":2,"category":"food","amount":100000,"created":1781174529}],"categoryStats":{"auto":1100000,"food":100000}}


server2 > server4 (запрос)

GET /api/transactions HTTP/1.1
Host: localhost:9002
User-Agent: Go-http-client/1.1
Authorization: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIsImxvZ2luIjoidXNlciIsInJvbGVzIjpbIlVTRVIiXSwiaWF0IjoxNzgxMTc1NTUwLCJleHAiOjE3ODExNzkxNTB9.gTLLN8-5yAkCx46nVdoIcTaGnqmFptbZnpBXK4agTVakRtjooy9AW-DukgDiH2Los0Cz8YwG0lgCH1NjabylbQ5H7PiSqI0xz-mKSFeA3rRLCs9V2rKRZAiKh4J4tavuJFxlambmOkDqBJE9D46QkPnVF7Qt70ESk_oKped4j5cSJnUmWgGIgNEeVVUbgwYrwDn8oIhuFpNRTLBaO-He60x_4G5KDltswtb513L_KNgvC7Ah02qJODtOWyqojgz2obd4ndBzK8K8mtmACoV1Dh4rUJb1cMEfk_157hmcHhiR2aMPuSeSVcZFbwdBnQy0Z4fK55VI5tqaoSQilvQODw
Accept-Encoding: gzip

HTTP/1.1 200 OK
Content-Type: application/json
Date: Thu, 11 Jun 2026 10:59:10 GMT
Content-Length: 291

{"transactions":[{"id":1,"userId":2,"category":"auto","amount":1000000,"created":1781174529},{"id":2,"userId":2,"category":"auto","amount":100000,"created":1781174529},{"id":3,"userId":2,"category":"food","amount":100000,"created":1781174529}],"categoryStats":{"auto":1100000,"food":100000}}


server4 > server3 (запрос)

GET /api/transactions HTTP/1.1
Host: localhost:9003
User-Agent: Go-http-client/1.1
X-Userid: 2
Accept-Encoding: gzip

HTTP/1.1 200 OK
Content-Type: application/json
Date: Thu, 11 Jun 2026 10:59:10 GMT
Content-Length: 291

{"transactions":[{"id":1,"userId":2,"category":"auto","amount":1000000,"created":1781174529},{"id":2,"userId":2,"category":"auto","amount":100000,"created":1781174529},{"id":3,"userId":2,"category":"food","amount":100000,"created":1781174529}],"categoryStats":{"auto":1100000,"food":100000}}

server3 > server4 (ответ)

GET /api/transactions HTTP/1.1
Host: localhost:9004
User-Agent: Go-http-client/1.1
X-Userid: 2
Accept-Encoding: gzip

HTTP/1.1 200 OK
Content-Type: application/json
Date: Thu, 11 Jun 2026 10:59:10 GMT
Content-Length: 227

[{"id":1,"userId":2,"category":"auto","amount":1000000,"created":1781174529},{"id":2,"userId":2,"category":"auto","amount":100000,"created":1781174529},{"id":3,"userId":2,"category":"food","amount":100000,"created":1781174529}]

server4 > server2 (ответ)

GET /api/transactions HTTP/1.1
Host: localhost:9003
User-Agent: Go-http-client/1.1
X-Userid: 2
Accept-Encoding: gzip

HTTP/1.1 200 OK
Content-Type: application/json
Date: Thu, 11 Jun 2026 10:59:10 GMT
Content-Length: 291

{"transactions":[{"id":1,"userId":2,"category":"auto","amount":1000000,"created":1781174529},{"id":2,"userId":2,"category":"auto","amount":100000,"created":1781174529},{"id":3,"userId":2,"category":"food","amount":100000,"created":1781174529}],"categoryStats":{"auto":1100000,"food":100000}}

server2 > clien1 (ответ)

GET /api/transactions HTTP/1.1
Host: localhost:9002
User-Agent: Go-http-client/1.1
Authorization: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIsImxvZ2luIjoidXNlciIsInJvbGVzIjpbIlVTRVIiXSwiaWF0IjoxNzgxMTc1NTUwLCJleHAiOjE3ODExNzkxNTB9.gTLLN8-5yAkCx46nVdoIcTaGnqmFptbZnpBXK4agTVakRtjooy9AW-DukgDiH2Los0Cz8YwG0lgCH1NjabylbQ5H7PiSqI0xz-mKSFeA3rRLCs9V2rKRZAiKh4J4tavuJFxlambmOkDqBJE9D46QkPnVF7Qt70ESk_oKped4j5cSJnUmWgGIgNEeVVUbgwYrwDn8oIhuFpNRTLBaO-He60x_4G5KDltswtb513L_KNgvC7Ah02qJODtOWyqojgz2obd4ndBzK8K8mtmACoV1Dh4rUJb1cMEfk_157hmcHhiR2aMPuSeSVcZFbwdBnQy0Z4fK55VI5tqaoSQilvQODw
Accept-Encoding: gzip

HTTP/1.1 200 OK
Content-Type: application/json
Date: Thu, 11 Jun 2026 10:59:10 GMT
Content-Length: 291

{"transactions":[{"id":1,"userId":2,"category":"auto","amount":1000000,"created":1781174529},{"id":2,"userId":2,"category":"auto","amount":100000,"created":1781174529},{"id":3,"userId":2,"category":"food","amount":100000,"created":1781174529}],"categoryStats":{"auto":1100000,"food":100000}}