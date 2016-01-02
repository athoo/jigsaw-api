## API specification
test at
```
jigsaw-api.herokuapp.com
```

run with

``` python
python api_test.py
```

test whether run properly

```
get http://127.0.0.1:5000/
```

### end-point

#### form

get all the form generated

```
get http://127.0.0.1:5000/forms/
```

post a new form

```
post http://127.0.0.1:5000/forms/
Content-Type: application/json

body:
{"name":"behavior","description":"This is a a human behavior study ","notification":"2","start":"1/12/2016","end":"1/19/2016","question_set":[{"type":"text","title":"what do you want to eat?"},{"type":"text","title":"what do you want to search?"}]}
```

delete a form

```
delete http://127.0.0.1:5000/forms/form_id
```

check a form

```
get http://127.0.0.1:5000/forms/form_id
```

update a form

```
put http://127.0.0.1:5000/forms/form_id
Content-Type: application/json

body:
{"name":"behavior","description":"This is a a human behavior study ","notification":"2","start":"1/12/2016","end":"1/19/2016","question_set":[{"type":"text","title":"what do you want to eat?"},{"type":"text","title":"what do you want to search?"}]}
```

#### user

get all the experiment generated

```
get http://127.0.0.1:5000/users/
```

post a new experiment

```
post http://127.0.0.1:5000/users/
Content-Type: application/json

body:
{"name":"david","email":"david@mmms.com","gender":"F","job":"farmer","mobile_os":"iOS","mobile_name":"iPhone 6","pc_os":"MacOS"}
```

delete a experiment

```
delete http://127.0.0.1:5000/users/user_id
```

check a experiment

```
get http://127.0.0.1:5000/users/user_id
```

update a experiment

```
put http://127.0.0.1:5000/users/user_id
Content-Type: application/json

body:
{"name":"david","email":"david@mmms.com","gender":"F","job":"farmer","mobile_os":"iOS","mobile_name":"iPhone 6","pc_os":"MacOS"}
```

#### experiment

get all the experiment generated

```
get http://127.0.0.1:5000/experiments/
```

post a new experiment

```
post http://127.0.0.1:5000/experiments/
Content-Type: application/json

body:
{"form":"behavior","users":["david", "johnson"]}
```

delete a experiment

```
delete http://127.0.0.1:5000/experiments/experiment_id
```

check a experiment

```
get http://127.0.0.1:5000/experiments/experiment_id
```

update a experiment

```
put http://127.0.0.1:5000/experiments/experiment_id
Content-Type: application/json

body:
{"form":"behavior","users":["david", "johnson"]}
```

#### results

get all the results generated

```
get http://127.0.0.1:5000/results/
```

post a new result

```
post http://127.0.0.1:5000/results/
Content-Type: application/json

body:
{"user":"david","time":"13:30 1/12/2016","title":"what do you want to search?","content":"I want to know how to use Cortana."}
```

delete a result

```
delete http://127.0.0.1:5000/results/result_id
```

check a result

```
get http://127.0.0.1:5000/results/result_id
```

update a result

```
put http://127.0.0.1:5000/results/result_id
Content-Type: application/json

body:
{"user":"david","time":"13:30 1/12/2016","title":"what do you want to search?","content":"I want to know how to use Cortana."}
```
