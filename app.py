from flask import Flask, jsonify, request


from Models import  Customer, customers

app = Flask(__name__)
'''
Test
@app.route("/hi")
def hi():
    return jsonify({"message": "Bye!"})
'''

@app.route("/")
def welcome():
    return "<h1>Take-home Project : Customer Relationship Management API</h1>"

@app.route("/customers")
def getCustomers():
    return jsonify({"customers": [customer.serialize() for customer in customers], "message": "Customer's List"})


@app.route("/customers/<customer_id>")
def getCustomerById(customer_id):
    customer_found = [
        customer for customer in customers if customer.id == int(customer_id)]

    if (len(customer_found) > 0):
        return jsonify({"customer": customer_found[0].serialize()})
    return jsonify({"message": "Customer Not Found!"})


@app.route("/customers", methods=["POST"])
def createCustomer():
    new_customer = Customer(request.json["id"],
        request.json["name"], request.json["surname"], request.json["email"], request.json["birthdate"])
    customers.append(new_customer)
    return jsonify({"message": "Customer Successfully Created and Added.", "new customer": new_customer.serialize()})


@app.route("/customers/<customer_id>", methods=["PUT"])
def editCustomerById(customer_id):
    customer_found = [
        customer for customer in customers if customer.id == int(customer_id)]
    if (len(customer_found) > 0):
        customer_found[0].id = request.json["id"]
        customer_found[0].name = request.json["name"]
        customer_found[0].surname = request.json["surname"]
        customer_found[0].email = request.json["email"]
        customer_found[0].birthdate = request.json["birthdate"]
        return jsonify({"message": "Customer Updated", "customer": customer_found[0].serialize()})
    return jsonify({"message": "Customer Not Found!"})


@app.route("/customers/<customer_id>", methods=["DELETE"])
def deleteCustomerById(customer_id):
    customer_found = [
        customer for customer in customers if customer.id== int(customer_id)]
    if (len(customer_found) > 0):
        customers.remove(customer_found[0])
        return jsonify({"message": "Customer Deleted", "customer": [customer.serialize() for customer in customers]})
    return jsonify({"message": "Customer Not Found!"})

if __name__ == "__main__":

    app.run(debug=True)
