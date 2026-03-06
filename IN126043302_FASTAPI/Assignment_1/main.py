from fastapi import FastAPI

app = FastAPI()
#1
# product details
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 599, "category": "Electronics", "in_stock": False},
    {"id": 2, "name": "Notebook", "price": 49, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "Pen Set", "price": 149, "category": "Stationery", "in_stock": False},
    {"id": 4, "name": "Bluetooth Speaker", "price": 1299, "category": "Electronics", "in_stock": True},
]
#1 Add 3 More Products
new_products=[# adding next three products
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False},
]
products.extend(new_products)

@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }
 
#2 Add a Category Filter Endpoint
@app.get("/products/category/{category_name}")
def get_by_product(category_name: str):
    try:
        res = []
        for i in products:
            if i["category"].lower() == category_name.lower():
                res.append(i)

        if len(res) == 0:
            raise ValueError("No products found in this category")

        return {
            "category": category_name,
            "products": res,
            "total": len(res)
        }

    except ValueError as e:
        return {"error": str(e)}
    


#3 Show Only In-Stock Products
@app.get("/products/instock")
def get_instock():
    avail=[]
    for i in products:
        if i["in_stock"]==True:
            avail += [i]
    return {
        "in_stock_products":avail,
        "count":len(avail)
    }

#4 Build a Store Info Endpoint
def total_products():
    count=0
    for i in products:
        count += 1
    return count

def in_stock():
    avail=[]
    for i in products:
        if i["in_stock"]==True:
            avail += [i]
    return avail
def out_stock():
    out=[]
    cat=[]
    for i in products:
        if i["in_stock"]==False:
            out += [i]
            if i["category"] not in cat:
                cat.append(i["category"])
    return out,cat

@app.get('/store/summary')
def store_endpoint():
    
    return {
       "store_name": "My E-commerce Store",
       "total_products": total_products(),
       "in_stock":len(in_stock()),
       "out_stock":len(out_stock()[0]),
       "catgories":out_stock()[1]
    }



#5.Search Products by Name
@app.get("/products/search/{keyword}")
def search_products(keyword: str):

    results = []

    for i in products:
        name = i["name"].lower()
        key = keyword.lower()

        if key in name:
            results.append(i)

    if len(results) == 0:
        return {"message": "No products matched your search"}

    return {
        "keyword": keyword,
        "results": results,
        "total_matches": len(results)
    }
    
# bonus
@app.get("/products/deals")
def product_deals():

    cheapest = products[0]
    expensive = products[0]

    for i in products:
        if i["price"] < cheapest["price"]:
            cheapest = i

        if i["price"] > expensive["price"]:
            expensive = i

    return {
        "best_deal": cheapest,
        "premium_pick": expensive
    }