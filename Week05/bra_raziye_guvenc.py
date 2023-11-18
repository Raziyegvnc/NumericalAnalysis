from flask import Flask, request, jsonify

class BinaryRepresentation:
    def __init__(self, numb):
        if not isinstance(numb , float):
            raise ValueError("You must be a float")
        self.numb = numb

    def to_binary_int(self):
        integer_x = int(self.numb)
        int_binary = ""

        while integer_x > 0:
            reminder_int = integer_x % 2
            integer_x = integer_x // 2
            int_binary = str(reminder_int) + int_binary

        if int_binary == "":
            int_binary = "0"
        return int_binary

    def to_binary_frac(self):
        frac_x = self.numb - int(self.numb)
        frac_binary = ""

        for _ in range(10):
            frac_x = frac_x * 2
            bit = int(frac_x)
            frac_binary = str(bit) + frac_binary
            frac_x = frac_x - bit
        return frac_binary[::-1]

app = Flask(__name__)
@app.route('/binary', methods=['GET'])
def get_binary_representation():
    number = request.args.get('number')

    if number is None:
        return jsonify({"error": "Number parameter is missing."}), 400

    try:
        number = float(number)
    except ValueError:
        return jsonify({"error": "Invalid number format."}), 400

    binary_converter = BinaryRepresentation(number)
    int_binary = binary_converter.to_binary_int()
    frac_binary = binary_converter.to_binary_frac()

    response_data = {"Binary Number": f"{int_binary}.{frac_binary}"}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)



