def handler(context, inputs):
    a = inputs["a"]
    b = inputs["b"]
    result = a + b

    outputs = {
        "result": result
    }
    print("test1")

    return outputs