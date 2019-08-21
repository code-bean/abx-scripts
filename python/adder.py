def handler(context, inputs):
    a = inputs["a"]
    b = inputs["b"]
    result = a + b

    outputs = {
        "result": result
    }
    
    print("new test1")
    print("test2")

    return outputs
