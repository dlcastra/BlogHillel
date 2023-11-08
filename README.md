# BlogHillel

# How to run

1. Install dependencies:

```
 pip install -r requirements.txt
```

2. Apply migration:

```
 python manage.py migrate
 or 
 python3 manage.py migrate
```

3. Run Redis:

```
 docker run -p 6379:6379 redis
```

4. To generate fake blog pages use this command, using the command without specifying the number of titles will generate
   10 blog pages:

```
python manage.py generate_blog <your_number>
or
python3 manage.py generate_blog <your_number>
```

5. Run server

```
python manage.py runserver  
or 
python3 manage.py runserver  
```
