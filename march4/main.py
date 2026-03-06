from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Welcome to our app"}

products = [
    { 'id':1,
     'name':'wireless mouse',
     'price':499,
     'category':'Electronics',
     'in_stock':True
     },
    { 'id':2,
      'name':'Notebook',
      'price':900,
      'category':'Stationery',
      'in_stock':False
      },
    {' id':3,
     'name':'USB Hub',
     'price':750,
     'category':'Electronics',
     'in_stock':True},
    {'id':4,
     'name':'Pen Set',
     'price':599,
     'category':'Stationery',
     'in_stock':False}
]

@app.get('/products')
def get_all_products():
    return list_products(),get_count()

def get_count():
    return {'total': len(products)}
def list_products():
    return {'products': products}


new_product = {
    'id': 5,
    'name': 'Keyboard',
    'price': 1200,
    'category': 'Electronics',
    'in_stock': True
}
products.append(new_product)

products[4].update({'name':'Mouse'})