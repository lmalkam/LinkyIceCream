{
    "builds": [{
        "src": "vercel_app/wsgi.py",
        "use": "@ardnt/vercel-python-wsgi",
        "config": { "maxLambdaSize": "15mb" }
    }],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "vercel_app/wsgi.py"
        }
    ]
}