from flask import Flask, request, jsonify, Response
import json
import csv

app = Flask(__name__)
app.config["DEBUG"] = True
path_file = "csv/zadanie.csv"
ml = []
with open(path_file, "r") as f:
    ml = f.readlines()
@app.route('/<sku>', methods=['GET'])
def appearance(sku):
    rank = request.args.get('rank')
    if rank == None:
        rank = 0.0
    else:
        rank = float(rank)
        if rank < 0.0 or rank > 1.0:
            return Response("Неправильно ввели rank", status=400)
    lenght = len(ml)
    len_str = len(sku)
    z = lenght // 2
    left = 0
    right = lenght - 1
    while ml[z][0:len_str] != sku and left <= right:
        if ml[z][0:len_str] > sku:
            right = z - 1
        else:
            left = z + 1
        z = (left + right) // 2

    if left > right:
        return Response(f"Товара по имени {sku} не существует", status=400)
    else:
        result = {"recommend": []}
        if float(ml[z][-4:-1:]) >= rank:
            result['recommend'].append(ml[z][len_str + 1:-5:])
        if z == lenght - 1:
            z -= 1
            while ml[z][0:len_str] == sku:
                if float(ml[z][-4:-1:]) >= rank:
                    result['recommend'].append(ml[z][len_str + 1:-5:])
                z -= 1
        elif z == 0:
            z += 1
            while ml[z][0:len_str] == sku:
                if float(ml[z][-4:-1:]) >= rank:
                    result['recommend'].append(ml[z][len_str + 1:-5:])
                z += 1
        else:
            left_side, right_side = z - 1, z + 1
            while ml[left_side][0:len_str] == sku:
                if left_side == -1:
                    break
                if float(ml[left_side][-4:-1:]) >= rank:
                    result['recommend'].append(ml[left_side][len_str + 1:-5:])
                left_side -= 1
            while ml[right_side][0:len_str] == sku:
                if right_side == lenght:
                    break
                if float(ml[right_side][-4:-1:]) >= rank:
                    result['recommend'].append(ml[right_side][len_str + 1:-5:])
                right_side += 1
    return jsonify(result)

app.run(use_reloader=False)